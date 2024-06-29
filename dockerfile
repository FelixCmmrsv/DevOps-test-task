FROM python:3.11.2-slim-bullseye

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y apache2 libapache2-mod-wsgi-py3

RUN a2enmod wsgi

WORKDIR /var/www/flask-app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

COPY apache/flask-app.conf /etc/apache2/sites-available/
RUN ln -s /etc/apache2/sites-available/flask-app.conf /etc/apache2/sites-enabled/

EXPOSE 8080

CMD ["apache2ctl", "-D", "FOREGROUND"]
