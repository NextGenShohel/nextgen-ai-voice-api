FROM python:3.10-slim

# ---------- system deps ----------
RUN apt-get update -y && apt-get install -y \
    ffmpeg curl autoconf automake libtool pkg-config build-essential \
 && rm -rf /var/lib/apt/lists/*

# ---------- build rnnoise ----------
WORKDIR /opt
# সরাসরি tarball ডাউনলোড (সুইচ গিট সমস্যা বাদ)
ADD https://github.com/xiph/rnnoise/archive/refs/tags/v0.4.tar.gz rnnoise.tar.gz
RUN tar -xzf rnnoise.tar.gz && \
    cd rnnoise-0.4 && \
    ./autogen.sh && ./configure --enable-shared=no && make && \
    cp .libs/librnnoise.a /usr/local/lib/ && cp src/rnnoise.h /usr/local/include/

# ---------- python ----------
WORKDIR /app
COPY server/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# ---------- copy app ----------
COPY server/app /app/app

EXPOSE 8000
CMD ["uvicorn","app.main:api","--host","0.0.0.0","--port","8000"]
