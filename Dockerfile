# syntax=docker/dockerfile:1
FROM python:3.11.5-slim-bookworm

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python init_db.py

EXPOSE 8000

CMD ["python", "main.py"]
