FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app_014
COPY Pipfile Pipfile.lock /app_014/
RUN pip install pipenv && pipenv install --system
COPY . /app_014/