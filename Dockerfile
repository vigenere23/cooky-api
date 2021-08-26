FROM python:3.8.11-slim-bullseye

WORKDIR /app


RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt


EXPOSE 5000

CMD gunicorn src.app:flask_app --bind=0.0.0.0:5000 --workers=1 --log-level=debug --timeout=60
