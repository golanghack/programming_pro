FROM python:3.8-slim
ENV PYTHOMDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app_04
COPY . ./

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]