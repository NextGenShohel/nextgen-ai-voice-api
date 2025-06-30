FROM python:3.10-slim

# Update & install system dependencies
RUN apt-get update -y && apt-get install -y \
    ffmpeg git autoconf automake libtool pkg-config build-essential \
 && rm -rf /var/lib/apt/lists/*

# Clone and build rnnoise from old commit (has autogen.sh)
RUN git clone https://github.com/xiph/rnnoise.git /opt/rnnoise \
 && cd /opt/rnnoise \
 && git checkout 7d56d1bf1e4c49aba2d3393e2f4f20413a5e6204 \
 && ./autogen.sh && ./configure --enable-shared=no && make \
 && cp .libs/librnnoise.a /usr/local/lib/ && cp src/rnnoise.h /usr/local/include/

# Set working directory
WORKDIR /app

# Copy app code to container
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port
EXPOSE 8000

# Run FastAPI with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
