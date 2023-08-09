FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app_06

COPY Pipfile Pipfile.lock /app_06/

RUN pip3 install pipenv && pipenv install 

COPY . /app_06/