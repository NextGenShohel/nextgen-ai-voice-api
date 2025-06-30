from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
import uuid, tempfile, soundfile as sf, numpy as np, noisereduce as nr
from gtts import gTTS

api = FastAPI()

@api.post("/enhance")
async def enhance(file: UploadFile = File(...)):
    # ইনপুট WAV পড়া
    raw = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    raw.write(await file.read()); raw.close()

    # ডেটা ও স্যাম্পল রেট লোড
    data, sr = sf.read(raw.name)
    # প্রথম ½ সেকেন্ডকে noise হিসেবে ধরা
    reduced = nr.reduce_noise(y=data, sr=sr, y_noise=data[:sr//2])

    # আউটপুট ফাইল
    out_path = raw.name.replace(".wav", "_clean.wav")
    sf.write(out_path, reduced.astype(np.float32), sr)
    return FileResponse(out_path, media_type="audio/wav", filename="enhanced.wav")

@api.post("/tts")
async def tts(text: str = Form(...)):
    mp3_path = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3").name
    gTTS(text=text, lang="bn").save(mp3_path)
    return FileResponse(mp3_path, media_type="audio/mpeg", filename="bn_tts.mp3")
