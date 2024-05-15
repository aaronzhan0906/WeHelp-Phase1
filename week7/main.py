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
        error_message = "帳號或密碼輸入錯誤"
        return RedirectResponse(url=f"/error?message={error_message}", status_code=status.HTTP_302_FOUND)
    

# Member Page
@app.get("/member", response_class=HTMLResponse)
async def success_page(request: Request):
    session = request.session
    if session.get("SIGNED-IN", False):
        name = session.get("name", "").get("name", "")
        mycursor.execute("SELECT message.content, member.name FROM member JOIN message ON member.id = message.member_id")
        messages = mycursor.fetchall()
        return templates.TemplateResponse("member.html", {
            "request": request,
            "messages": messages,
            })
    else:
        return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)


# Welcome Name
# pass JSON to frontend
@app.get("/api/messages")
async def get_messages_api(request: Request):
    session = request.session
    member_id = session.get("id", "").get("id", "")
    mycursor.execute("SELECT member.name FROM member WHERE id = %s", (member_id,))
    name = mycursor.fetchone()[0]
    print(name)
    username = session.get("username", "").get("username", "")
    mycursor.execute("SELECT message.id, member.name, message.content, member.username FROM member JOIN message ON member.id = message.member_id")
    messages = mycursor.fetchall()
    return JSONResponse(content={"messages": messages,"current_username": username, "name": name})
    

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
    request_data = await request.json()
    frontend_current_username = request_data.get("current_username")
    message_id = request_data.get("message_id")    
    backend_current_username = request.session.get("username", "").get("username", "")
    if frontend_current_username == backend_current_username:
        mycursor.execute("DELETE FROM message WHERE id = %s", (message_id,))
        database.mydb.commit()

    return RedirectResponse(url="/member", status_code=status.HTTP_302_FOUND)


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
    session.pop("user" , None)
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
        error_message = "帳號已經被註冊"
        return RedirectResponse(url=f"/error?message={error_message}", status_code=status.HTTP_302_FOUND)
    else:
        mycursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)", (name, username, password))
        database.mydb.commit()
        return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    

# Member Query API
@app.get("/api/member")
async def query_member(request: Request, username: str = None):
    if username:
        print(username)
        mycursor.execute("SELECT id, name, username FROM member WHERE username = %s" ,(username,))
        member = mycursor.fetchone()

        if member:
            return JSONResponse(content={"data": {"id": member[0], "name": member[1], "username": member[2]}})
        else:
            return JSONResponse(content={"data": None})
        
    else:
        print ("NO USERNAME")


@app.patch("/api/member")
async def update_name(request: Request):
    request_data = await request.json()
    new_name = request_data.get("name")
    session = request.session
    member_id = session.get("id", "").get("id", "")

    if session.get("SIGNED-IN", False):
        mycursor.execute("UPDATE member SET name = %s WHERE id= %s", (new_name, member_id))
        database.mydb.commit()
        mycursor.execute("SELECT name FROM member WHERE id = %s", (member_id,))
        mycursor.fetchone()
        print(mycursor.fetchone())
        return JSONResponse(content={"ok": True}) 
    else: 
        return JSONResponse(content={"error": True})
  
