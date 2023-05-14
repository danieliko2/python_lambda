FROM python:alpine3.17

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY templates ./templates/
COPY app2.py .

CMD python3 app2.py