FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/myapp

COPY requirements.txt /usr/myapp

RUN pip install -r requirements.txt


EXPOSE 8000