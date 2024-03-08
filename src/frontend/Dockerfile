FROM python:3.11


COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -U pip && pip install -r requirements.txt

RUN pip install -r requirements.txt
COPY . /frontend
WORKDIR /frontend

EXPOSE 8501

# ENTRYPOINT ["streamlit","run"]

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
# CMD ["python3", "-m", "streamlit", "run", "app.py"]


