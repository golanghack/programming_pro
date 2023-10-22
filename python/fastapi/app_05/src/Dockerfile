FROM python:3.11.0-alpine

WORKDIR /app_05/src/app 

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /app_05/src/app/requirements.txt 

RUN set -eux \
     python3-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /app_05/src/app/requirements.txt \
    && rm -rf /root/.cache/pip 

COPY . /app_05/src/app/