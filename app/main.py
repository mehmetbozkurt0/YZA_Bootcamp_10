from fastapi import FastAPI, Form, Request, Body
from fastapi.params import Query
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import RedirectResponse, HTMLResponse, JSONResponse
from starlette.templating import Jinja2Templates
from app import crud
from app.models import TaskModel, TaskUpdateModel

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="grup-10")
templates = Jinja2Templates(directory="app/templates")

@app.get("/login")
async def login_page(request: Request):
    if request.session.get("user_id"):
        return RedirectResponse(url="/")
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(request: Request, email: str = Form(...), password: str = Form(...)):
    print("Login denemesi:", email, password)
    user = crud.check_user(email, password)
    if not user:
        return HTMLResponse(content="❌ Geçersiz email veya şifre!", status_code=401)

    request.session["user_id"] = user["UserId"]
    request.session["user_name"] = user["UserName"]
    print("Giriş başarılı:", user)
    return RedirectResponse(url="/", status_code=302)

@app.get("/logout")
async def logout(request: Request):
    print("Çıkış yapılıyor, oturum temizleniyor")
    request.session.clear()
    return RedirectResponse(url="/login")

@app.get("/")
async def home(request: Request):
    user_id = request.session.get("user_id")
    user_name = request.session.get("user_name")
    if not user_id:
        return RedirectResponse(url="/login")

    quote = crud.get_daily_quote()
    reflection = crud.get_reflection(user_id)
    mood = reflection[0] if reflection else ""
    feedback = reflection[1] if reflection else ""

    return templates.TemplateResponse("landing_page.html", {
        "request": request,
        "user_name": user_name,
        "quote": quote,
        "mood": mood,
        "feedback": feedback
    })


@app.post("/add-task")
async def add_task(request: Request, task: TaskModel = Body(...)):
    user_id = request.session.get("user_id")
    if not user_id:
        return JSONResponse(content={"error": "Oturum bulunamadı!"}, status_code=401)

    crud.add_task(user_id, task.text, task.completed)
    return JSONResponse(content={"message": "Görev kaydedildi!"})

@app.get("/get-tasks")
async def get_tasks(request: Request):
    user_id = request.session.get("user_id")
    if not user_id:
        return JSONResponse(content={"error": "Oturum bulunamadı!"})

    tasks = crud.get_tasks(user_id)
    return JSONResponse(content={"tasks": tasks})

@app.delete("/delete-task")
async def delete_task(request: Request, id: int = Query(...)):
    user_id = request.session.get("user_id")
    if not user_id:
        return JSONResponse(content={"error": "Oturum bulunmadı!"})

    crud.delete_task_by_id(user_id,id)
    return JSONResponse(content={"message": "Görev silindi!"})

@app.put("/update-task")
async def update_task(request: Request, update: TaskUpdateModel):
    user_id = request.session.get("user_id")
    if not user_id:
        return JSONResponse(content={"error": "Oturum bulunamadı!"})
    crud.update_task_by_id(user_id, update.task_id, update.completed)
    return JSONResponse(content={"message": "Görev güncellendi!"})

@app.get("/register")
async def redirect_register(request: Request):
    return templates.TemplateResponse("register.html",{"request": request})

@app.post("/register")
async def register(email: str = Form(...), password:str = Form(...), username: str = Form(...)):
    if crud.check_user_exist(email):
        return HTMLResponse(content="Bu email ile zaten bir hesap var!", status_code=400)

    crud.register_user(email,password,username)
    return RedirectResponse(url="/login", status_code=302)

@app.post("/save-reflections")
async def save_reflections(request: Request, mood: str = Form(...), feedback: str = Form(...)):
    user_id = request.session.get("user_id")
    if not user_id:
        return JSONResponse(content={"error":"Oturum bulunamadı!"}, status_code=401)

    crud.save_or_update_reflection(user_id,mood,feedback)
    return RedirectResponse("/",status_code=302)












