from fastapi import FastAPI, Request, Form, status, Path
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
import database
mycusor = database.mydb.cursor()



app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
app.add_middleware(SessionMiddleware, secret_key="your_secret_key")


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
    form_data = await request.form()
    username = form_data.get("username", "")
    password = form_data.get("password", "")
    
    if username == "test" and password == "test":
        session = request.session
        session["SIGNED-IN"] = True
        session["user"] = "user" # 等下要從資料庫拿
        return RedirectResponse(url="/member", status_code=status.HTTP_302_FOUND)
    elif not username or not password:
        error_message = "請輸入帳號、密碼"
        return RedirectResponse(url=f"/error?message={error_message}", status_code=status.HTTP_302_FOUND)
    else:
        error_message = "帳號、密碼輸入錯誤"
        return RedirectResponse(url=f"/error?message={error_message}", status_code=status.HTTP_302_FOUND)


# Signup
@app.post("/signup", response_class=HTMLResponse)
async def signup(request: Request):
    form_data = await request.form()
    user = form_data.get("signup-user", "")
    username = form_data.get("signup-username", "")
    password = form_data.get("signup-password", "")
    print (user, username, password)

    # check if user exists
    mycusor.execute("SELECT * FROM member WHERE username = %s", (username,))
    check_result = mycusor.fetchall()
    if check_result:
        error_message = "Repeated username"
        return RedirectResponse(url=f"/error?message={error_message}", status_code=status.HTTP_302_FOUND)
    else:
        #補完

    return RedirectResponse(url="/member", status_code=status.HTTP_302_FOUND)


# Success Page
@app.get("/member", response_class=HTMLResponse)
async def success_page(request: Request):
    session = request.session
    if session.get("SIGNED-IN", False):
        user = session.get("user", "") 
        return templates.TemplateResponse("member.html", {"request": request, "user": user})
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
    return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)


