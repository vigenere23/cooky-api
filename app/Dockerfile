# FROM python:3.8.11-apline
FROM python:3.8.11-slim-bullseye

WORKDIR /app

# RUN apk add gcc musl-dev libffi-dev openssl-dev cargo

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD gunicorn src.app:flask_app --bind=0.0.0.0:5000 --workers=1 --log-level=debug --timeout=60
