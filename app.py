from typing import Annotated
from fastapi import FastAPI, File
from fastapi.responses import FileResponse
from faster_whisper import WhisperModel
from io import BytesIO

model_size = "large-v2"

model = WhisperModel(model_size, device="cuda", compute_type="int8")

main = FastAPI()


@main.get("/")
def root():
    return FileResponse("./index.html")


@main.post("/api/whisper")
def transcribe(file: Annotated[bytes, File()]):
    (segs, info) = model.transcribe(BytesIO(file))
    print(info)
    text = ""
    for seg in segs:
        print(seg)
        text += seg.text

    return {"text": text}
