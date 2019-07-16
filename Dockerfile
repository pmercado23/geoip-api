FROM python:3.6-slim
MAINTAINER Peter Mercado <peter.mercado255@gmail.com>

ENV PROJECT_ROOT /app
WORKDIR $PROJECT_ROOT

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD python setup_db.py
CMD python manage.py test
CMD python manage.py runserver 0.0.0.0:8000