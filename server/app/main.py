from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
from gtts import gTTS
import subprocess, uuid, pathlib

api = FastAPI()
TMP = pathlib.Path("/tmp")

@api.post("/enhance")
async def enhance(file: UploadFile = File(...)):
    raw = TMP/f"{uuid.uuid4()}.wav"
    enh = TMP/f"{uuid.uuid4()}_clean.wav"
    raw.write_bytes(await file.read())
    subprocess.run(["ffmpeg","-y","-i",raw,"-ar","16000","-ac","1",raw], check=True)
    subprocess.run(["/opt/rnnoise/examples/rnnoise_demo",raw,enh], check=True)
    return FileResponse(enh, media_type="audio/wav", filename="enhanced.wav")

@api.post("/tts")
async def tts(text: str = Form(...)):
    mp3 = TMP/f"{uuid.uuid4()}.mp3"
    gTTS(text=text, lang="bn").save(mp3)
    return FileResponse(mp3, media_type="audio/mpeg", filename="bn_tts.mp3")
