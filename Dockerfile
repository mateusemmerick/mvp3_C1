# syntax=docker/dockerfile:1

FROM python:3.11.5

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000
CMD [ "flask", "run", "--host=0.0.0.0"]
