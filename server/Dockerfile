# পূর্ণ python ইমেজ ব্যবহার করি—বিল্ড টুল আগে থেকেই আছে
FROM python:3.10

# সিস্টেম লাইব্রেরি; libsndfile -> soundfile কাজ করবে
RUN apt-get update -y && apt-get install -y ffmpeg libsndfile1 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# requirements কপি ও ইনস্টল
COPY server/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# অ্যাপের কোড কপি
COPY server/app ./app

EXPOSE 8000
CMD ["uvicorn", "app.main:api", "--host", "0.0.0.0", "--port", "8000"]
