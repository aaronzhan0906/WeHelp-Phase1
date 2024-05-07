from fastapi import FastAPI, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
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
    mycursor.execute("SELECT id, user, username , password FROM member WHERE username = %s AND password = %s", (username, password))
    member = mycursor.fetchone()  

    if member:
        session = request.session
        session["SIGNED-IN"] = True
        session["id"] = {"user": member[0]}
        session["user"] = {"user": member[1]}
        session["username"] = {"user": member[2]}
        return RedirectResponse(url="/member", status_code=status.HTTP_302_FOUND)
    else:
        error_message = "Username or password is not correct"
        return RedirectResponse(url=f"/error?message={error_message}", status_code=status.HTTP_302_FOUND)
    

# Success Page
@app.get("/member", response_class=HTMLResponse)
async def success_page(request: Request):
    session = request.session
    if session.get("SIGNED-IN", False):
        user = session.get("user", "") 
        return templates.TemplateResponse("member.html", {"request": request, "user": user["user"]})
    else:
        return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)


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
    session.pop("user", None)
    session.pop("username", None)
    print(request.session)
    return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)



# Signup
@app.post("/signup", response_class=HTMLResponse)
async def signup(request: Request):
    form_data = await request.form()
    user = form_data.get("signup-user", "")
    username = form_data.get("signup-username", "")
    password = form_data.get("signup-password", "")
    print (user, username, password)

    # check if user exists
    mycursor.execute("SELECT * FROM member WHERE username = %s", (username,))
    check_result = mycursor.fetchone()

    if check_result:
        error_message = "Repeated username"
        return RedirectResponse(url=f"/error?message={error_message}", status_code=status.HTTP_302_FOUND)
    else:
        mycursor.execute("INSERT INTO member (user, username, password) VALUES (%s, %s, %s)", (user, username, password))
        database.mydb.commit()
        return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)




