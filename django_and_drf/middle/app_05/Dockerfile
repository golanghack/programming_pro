FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app_05
COPY Pipfile Pipfile.lock /app_05/
RUN pip install pipenv && pipenv install --system
COPY . /app_05/