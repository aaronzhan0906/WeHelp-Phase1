from fastapi import FastAPI, Request, Form, status
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
import database


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
app.add_middleware(SessionMiddleware, secret_key="your_secret_key")
mycursor = database.mydb.cursor()


# Home
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"request": request}
    )


# Signin
@app.post("/signin")
async def signin(request: Request):
    # Get form data
    form_data = await request.form()
    username = form_data.get("signin-username", "")
    password = form_data.get("signin-password", "")

    # Check if user exists by username and password
    mycursor.execute("SELECT id, name, username , password FROM member WHERE username = %s AND password = %s", (username, password))
    member = mycursor.fetchone()  
    if member:
        session = request.session
        session["SIGNED-IN"] = True
        session["id"] = {"id": member[0]}
        session["name"] = {"name": member[1]}
        session["username"] = {"username": member[2]}
        print(session["id"], session["name"] ,session["username"])
        return RedirectResponse(url="/member", status_code=status.HTTP_302_FOUND,)
    else:
        error_message = "Username or password is not correct"
        return RedirectResponse(url=f"/error?message={error_message}", status_code=status.HTTP_302_FOUND)
    

# Member Page
@app.get("/member", response_class=HTMLResponse)
async def success_page(request: Request):
    session = request.session
    if session.get("SIGNED-IN", False):
        name = session.get("name", "")
        mycursor.execute("SELECT message.content, member.name FROM member JOIN message ON member.id = message.member_id")
        messages = mycursor.fetchall()
        return templates.TemplateResponse("member.html", {
            "request": request,
            "name": name["name"],
            "messages": messages,
            })
    else:
        return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    
# pass JSON to frontend
@app.get("/api/messages")
async def get_messages_api(request: Request):
    session = request.session
    username = session.get("username", "")
    mycursor.execute("SELECT member.name, message.content, member.username FROM member JOIN message ON member.id = message.member_id")
    messages = mycursor.fetchall()
    return JSONResponse(content={"messages": messages,"current_username": username["username"]})
    

# createMessage
@app.post("/createMessage")
async def create_message(request: Request):
    form_data = await request.form()
    member_id = request.session.get("id", "").get("id", "")
    message_content = form_data.get("message-input", "")

    # Insert the new message into table message
    mycursor.execute("INSERT INTO message (member_id, content) VALUES (%s, %s)", (member_id, message_content))
    database.mydb.commit()

    return RedirectResponse(url="/member", status_code=status.HTTP_302_FOUND)

# deleteMessage
@app.post("/deleteMessage")
async def delete_message(request: Request):
    print("deleteMessage")


# Error Page
@app.get("/error", response_class=HTMLResponse)
async def error_page(request: Request, message: str = None):
    error_message = request.query_params.get("message", "")
    return templates.TemplateResponse("error.html", {"request": request, "error_message": error_message})


# Signout
@app.get("/signout", response_class=HTMLResponse)
async def signout(request: Request):
    session = request.session
    session.pop("SIGNED-IN", False)  
    session.pop("id", None)
    session.pop("name", None)
    session.pop("username", None)
    print(request.session)
    return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)


# Signup
@app.post("/signup", response_class=HTMLResponse)
async def signup(request: Request):
    form_data = await request.form()
    name = form_data.get("signup-name", "")
    username = form_data.get("signup-username", "")
    password = form_data.get("signup-password", "")
    print (name, username, password)

    # check if user exists
    mycursor.execute("SELECT * FROM member WHERE username = %s", (username,))
    check_result = mycursor.fetchone()

    if check_result:
        error_message = "Repeated username"
        return RedirectResponse(url=f"/error?message={error_message}", status_code=status.HTTP_302_FOUND)
    else:
        mycursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)", (name, username, password))
        database.mydb.commit()
        return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)




