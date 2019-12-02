FROM python:3.7.5-slim-stretch

LABEL maintainer="juaneml@correo.ugr.es"

WORKDIR /proyecto_iv-19
COPY . .
COPY requirements.txt /proyecto_iv-19

RUN pip3 install --no-cache-dir -r requirements.txt


EXPOSE 8000

CMD cd /src gunicorn proyecto_app:__hug_wsgi__ -
