FROM python:3.9.5-slim-buster

RUN apt-get update
RUN apt-get install -y unixodbc-dev g++ default-libmysqlclient-dev

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /app
WORKDIR /app

RUN python3 manage.py collectstatic --no-input

ENTRYPOINT ["./run.sh"]



