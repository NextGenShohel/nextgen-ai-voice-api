from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
import uuid, tempfile, soundfile as sf, numpy as np, noisereduce as nr
from gtts import gTTS
import subprocess
from pathlib import Path

TMP = Path(tempfile.gettempdir())
api = FastAPI()

@api.post("/enhance")
async def enhance(file: UploadFile = File(...)):
    raw = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    raw.write(await file.read()); raw.close()

    data, sr = sf.read(raw.name)
    reduced = nr.reduce_noise(y=data, sr=sr, y_noise=data[:sr//2])

    out_path = raw.name.replace(".wav", "_clean.wav")
    sf.write(out_path, reduced.astype(np.float32), sr)
    return FileResponse(out_path, media_type="audio/wav", filename="enhanced.wav")


@api.post("/tts")
async def tts(text: str = Form(...), voice: str = Form("f1")):
    # base voice তৈরি
    tmp_in  = TMP / f"{uuid.uuid4()}.mp3"
    tmp_out = TMP / f"{uuid.uuid4()}_v.mp3"
    gTTS(text=text, lang="bn").save(tmp_in)

    # পিচ-ম্যাপ
    pitch = {"f1": 1.00, "f2": 1.12, "m1": 0.90, "m2": 0.80}.get(voice, 1.00)

    # FFmpeg পিচ শিফট
    subprocess.run([
        "ffmpeg", "-y", "-i", str(tmp_in),
        "-filter:a", f"asetrate=44100*{pitch},atempo={1/pitch}",
        str(tmp_out)
    ], check=True)

    return FileResponse(tmp_out, media_type="audio/mpeg", filename="bn_tts.mp3")
