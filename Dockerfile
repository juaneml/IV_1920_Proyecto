FROM python:3.7.5-slim-stretch

LABEL maintainer="juaneml@correo.ugr.es"

WORKDIR /proyecto_iv-19
COPY . /proyecto_iv-19

RUN export PATH=/usr/lib/postgresql/X.Y/bin/:$PATH
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip install psycopg2-binary


EXPOSE 8000

CMD cd src gunicorn proyecto_app:__hug_wsgi__ -
