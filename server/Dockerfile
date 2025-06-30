FROM python:3.10-slim

# only basic tools
RUN apt-get update -y && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY server/requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY server/app /app/app
EXPOSE 8000
CMD ["uvicorn", "app.main:api", "--host", "0.0.0.0", "--port", "8000"]
