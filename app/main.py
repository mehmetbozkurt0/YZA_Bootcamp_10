from fastapi import FastAPI, HTTPException, Form
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse, RedirectResponse
from app import crud
from fastapi.requests import Request
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.add_middleware(SessionMiddleware, secret_key="grup-10")

@app.post("/login")
async def login(request: Request = None, email: str = Form(...), password: str = Form(...)):
    print("Login denemesi:", email, password)
    user = crud.check_user(email, password)

    if not user:
        return HTMLResponse(content="❌ Geçersiz email veya şifre!", status_code=401)

    request.session["user_id"] = user["UserId"]
    print("Giriş başarılı: ", user)

    return RedirectResponse(url="/", status_code=302)

@app.get("/login")
async def redirect_login(request: Request):
    if request.session.get("user_id"):
        return RedirectResponse(url="/")
    return templates.TemplateResponse("login.html",{"request": request})

@app.get("/logout")
async def logout(request:Request):
    request.session.clear()
    return RedirectResponse(url="/login")

@app.get("/")
async def landing_page(request: Request):
    return templates.TemplateResponse("landing_page.html",{"request": request})