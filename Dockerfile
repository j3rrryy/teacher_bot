FROM python:3.11.3-slim-bullseye

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app
COPY requirements.txt .

RUN pip3 install -U pip
RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 8080
