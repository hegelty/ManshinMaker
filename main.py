from fastapi import FastAPI
from fastapi.responses import FileResponse
from PIL import Image,ImageDraw,ImageFont

app = FastAPI()

def generate(first, second):
    origin = Image.open("origin.jpg")

    font = 0
    fnt = ImageFont.truetype("NanumGothicBold.ttf", 50, encoding="UTF-8")
    w, h = origin.size
    ftw, fth = fnt.getsize(first)
    if ftw>300 and ftw<400:
        font = 5
        fnt = ImageFont.truetype("NanumGothicBold.ttf", 40, encoding="UTF-8")
    elif ftw>=400 and ftw<600 :
        font = 10
        fnt = ImageFont.truetype("NanumGothicBold.ttf", 30, encoding="UTF-8")
    ftw, fth = fnt.getsize(first)
    draw = ImageDraw.Draw(origin)
    draw.text((int(w / 2) - ftw / 2, 80+font), first, font=fnt, fill="black")

    font = 0
    fnt = ImageFont.truetype("NanumGothicBold.ttf", 50, encoding="UTF-8")
    stw, sth = fnt.getsize(second)
    if stw>300 and stw<400:
        font = 5
        fnt = ImageFont.truetype("NanumGothicBold.ttf", 40, encoding="UTF-8")
    elif stw>=400 and stw<600 :
        font = 10
        fnt = ImageFont.truetype("NanumGothicBold.ttf", 30, encoding="UTF-8")
    stw, sth = fnt.getsize(second)
    draw = ImageDraw.Draw(origin)
    draw.text((int(w / 2) - stw / 2, h-(155-font)), second, font=fnt, fill="black")

    origin.save("output.png")


@app.get("/manshin")
async def say_hello(first: str = "", second: str = ""):
    generate(first,second)
    return FileResponse(path="output.png", filename="output.png", media_type='text/png')
