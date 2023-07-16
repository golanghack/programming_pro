FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

WORKDIR /code
RUN pip3 install pipenv 
COPY requirements.txt /code/
CMD ["pipenv", "install", "-r", "requirements.txt"] 
RUN pipenv run python /code/app/manage.py runserver


COPY . /code/