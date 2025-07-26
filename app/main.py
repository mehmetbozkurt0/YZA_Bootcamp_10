from fastapi import FastAPI, Form, Request
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
    return templates.TemplateResponse("landing_page.html", {"request": request, "user_name": user_name})

from fastapi import Body

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
