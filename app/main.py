from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

from app.segmenter import segment_text
from app.prompt import enhance_prompt
from app.image_generator import generate_image

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


class StoryRequest(BaseModel):
    text: str
    style: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "form.html",
        {"request": request}
    )


@app.post("/generate")
async def generate(data: StoryRequest):

    segments = segment_text(data.text)

    scenes = []

    for s in segments:

        prompt = enhance_prompt(s + ", " + data.style)

        image = generate_image(prompt)

        scenes.append({
            "panel_number": len(scenes) + 1,
            "text": s,
            "prompt": prompt,
            "image_path": image.replace("static/", "")
        })

    return {"storyboard": scenes}