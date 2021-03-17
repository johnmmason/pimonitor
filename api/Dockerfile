FROM ubuntu:latest

RUN apt-get update -y &&\
    apt-get install -y python3-dev python3-pip build-essential

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "3", "--umask", "007", "wsgi:app"]
