# syntax=docker/dockerfile:1
# FROM python:3.12.2
#FROM python:3.10-alpine
FROM python:3.12.2-slim-bullseye

ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000
# ENV FLASK_RUN_PORT=5000
# ENV FLASK_RUN_PORT=80

WORKDIR .
RUN apt-get update && apt-get install build-essential -y

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -U pip && pip install -r requirements.txt

COPY . /backend
WORKDIR /backend

EXPOSE 8000
# EXPOSE 5000
# EXPOSE 8501
# EXPOSE 80

# CMD ["python3", "server.py"]
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000" ,"--reload"]

#HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health