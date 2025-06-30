FROM python:3.12-slim

RUN apt-get update -y && apt-get install -y ffmpeg git autoconf automake libtool build-essential

COPY server/requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

RUN git clone https://github.com/xiph/rnnoise.git /opt/rnnoise \
 && cd /opt/rnnoise && ./autogen.sh && ./configure && make

COPY server/app /app
WORKDIR /app

CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "8080"]
