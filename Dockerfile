FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .
COPY train.py .
COPY model ./model 

CMD [ "uvicorn","main:app","--host","0.0.0.0","--port","8080" ]