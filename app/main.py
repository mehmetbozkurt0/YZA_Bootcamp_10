from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.requests import Request
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
async def landing_page(request: Request):
    return templates.TemplateResponse("landing_page.html",{"request": request})