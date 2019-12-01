FROM python:3.7-slim-stretch

LABEL maintainer="juaneml@correo.ugr.es"


COPY .. /proyecto_iv-19

COPY requirements.txt /proyecto_iv-19

RUN make docker

WORKDIR /proyecto_iv-19


EXPOSE 8000
CMD cd /src gunicorn proyecto_app:__hug_wsgi__ -
