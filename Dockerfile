FROM python:3.7-slim-stretch

LABEL maintainer="juaneml@correo.ugr.es"

WORKDIR /proyecto_iv-19

COPY .. /proyecto_iv-19

COPY requirements.txt /proyecto_iv-19


ENV PYTHON_VERSION 3.7.5

RUN make docker

EXPOSE 8000
CMD cd /src gunicorn proyecto_app:__hug_wsgi__ -
