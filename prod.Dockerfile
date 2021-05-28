FROM python:3.8

ENV DJANGO_ENV="prod"
ENV PYTHONUNBUFFERED 1

WORKDIR /backend

COPY requirements /backend/requirements

RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements/$DJANGO_ENV.txt

CMD gunicorn api_droids.wsgi:application --bind 0.0.0.0:8000