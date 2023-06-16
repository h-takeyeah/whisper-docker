FROM python:3.9-slim

WORKDIR /workspace

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    git \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir \
    torch==2.0.1+cpu \
    --find-links https://download.pytorch.org/whl/torch_stable.html
RUN pip install --no-cache-dir openai-whisper==20230314
