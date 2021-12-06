import pathlib


from fastapi import FastAPI, Request

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


BASE_DIR = pathlib.Path(__file__).parent

app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR / "template"))

@app.get("/")
def home_view():
    return {"Welcome" : "on my app"}

@app.get("/home", response_class=HTMLResponse)
def read_home(request: Request):

    return templates.TemplateResponse("home.html", {"request": request, "arg": "Variable"})