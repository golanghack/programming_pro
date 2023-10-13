FROM python:3.8
ENV PETHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app_07
COPY Pipfile Pipfile.lock /app_07/
RUN pip install pipenv && pipenv install --system 
COPY . /app_07/