FROM python:3.11-slim

# Dependencias del sistema que suelen necesitar opencv/mediapipe
RUN apt-get update && apt-get install -y \
    libgl1 libglib2.0-0 ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code
ENV PYTHONUNBUFFERED=1

# Instala requirements primero para cachear
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Para que los imports "app/..." funcionen
ENV PYTHONPATH=/code
