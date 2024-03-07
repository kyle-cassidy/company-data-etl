from python:3.12.2-slim-bullseye

COPY src/ src/
WORKDIR /src

RUN apt-get update && apt-get install build-essential -y


RUN pip install --upgrade pip
RUN pip install -U pip && pip install -r requirements.txt

