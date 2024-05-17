# Dockerfile
FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

# �ʿ��� ��Ű�� ��ġ
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    && apt-get clean

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
