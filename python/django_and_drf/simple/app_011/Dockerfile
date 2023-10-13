FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app_011
COPY Pipfile Pipfile.lock /app_011/
RUN pip install pipenv && pipenv install --system
COPY . /app_011/