FROM python:3.10-slim

# ---------- system deps ----------
RUN apt-get update -y && \
    apt-get install -y ffmpeg curl autoconf automake libtool \
        pkg-config build-essential && \
    rm -rf /var/lib/apt/lists/*

# ---------- build rnnoise ----------
WORKDIR /opt
RUN curl -L -o rnnoise.tar.gz \
    https://github.com/xiph/rnnoise/archive/refs/heads/master.tar.gz && \
    tar -xzf rnnoise.tar.gz && \
    cd rnnoise-master && \
    ./autogen.sh && ./configure --enable-shared=no && make && \
    cp .libs/librnnoise.a /usr/local/lib/ && \
    cp src/rnnoise.h /usr/local/include/

# ---------- python ----------
WORKDIR /app
COPY server/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# ---------- app code ----------
COPY server/app /app/app

EXPOSE 8000
CMD ["uvicorn","app.main:api","--host","0.0.0.0","--port","8000"]
