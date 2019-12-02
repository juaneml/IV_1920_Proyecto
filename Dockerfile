FROM python:3.7.5-slim-stretch

LABEL maintainer="juaneml@correo.ugr.es"

WORKDIR /proyecto_iv-19
COPY . .
COPY requirements.txt /proyecto_iv-19

RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list

RUN pip3 install --no-cache-dir -r requirements.txt


EXPOSE 8000

CMD cd /src gunicorn proyecto_app:__hug_wsgi__ -
