FROM ubuntu:latest
LABEL authors="Aibek Zhenisbekov"

FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN apt-get update && \
    apt-get install -y apache2 libapache2-mod-wsgi-py3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY apache/flask-app.conf /etc/apache2/sites-available/

RUN a2enmod headers
RUN a2enmod wsgi
RUN a2ensite flask-app

EXPOSE 80

CMD ["apache2ctl", "-D", "FOREGROUND"]
