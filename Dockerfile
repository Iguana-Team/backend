# syntax=docker/dockerfile:1

# COPY mtslink.sql /app/migrations/versions
FROM python:3.11-slim
RUN apt-get update && apt-get install -y \
    libpq-dev gcc
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000