FROM python:3.10-slim

# -------- system libs (BLAS/Fortran & ffmpeg & libsndfile) ----------
RUN apt-get update -y && apt-get install -y --no-install-recommends \
        build-essential gcc gfortran libopenblas-dev liblapack-dev \
        libatlas-base-dev libsndfile1 ffmpeg curl && \
    rm -rf /var/lib/apt/lists/*

# -------- Python deps ----------
WORKDIR /app
COPY server/requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# -------- App code ----------
COPY server/app ./app

EXPOSE 8000
CMD ["uvicorn", "app.main:api", "--host", "0.0.0.0", "--port", "8000"]
