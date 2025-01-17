FROM python:3.11-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libxml2-dev \
    libxslt-dev \
    curl \
    gnupg2 \
    vim \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir "poetry==1.8.2"
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-interaction --no-ansi
ENV PYTHONPATH=/app
ENV HF_HUB_CACHE=/root/.cache/hugs