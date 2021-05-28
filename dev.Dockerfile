FROM python:3.8

ENV DJANGO_ENV="dev"
ENV PYTHONUNBUFFERED 1

WORKDIR /backend

COPY requirements /backend/requirements

RUN apt update -y && apt install gettext -y &&\
    pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements/$DJANGO_ENV.txt