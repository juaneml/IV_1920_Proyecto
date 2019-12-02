FROM python:3.7-alpine

LABEL maintainer="juaneml@correo.ugr.es"

WORKDIR /proyecto_iv-19
COPY . /proyecto_iv-19

RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  && pip install psycopg2 \
  && apk del build-deps
  
RUN pip3 install --no-cache-dir -r requirements.txt

CMD cd src
CMD ["gunicorn","-b","0.0.0.0:8000","proyecto_app"]
EXPOSE 8000/tcp
