FROM python:3
#ENV PYTHON_VERSION 3.7.5
LABEL maintainer="juaneml@correo.ugr.es"
WORKDIR src/

COPY requirements.txt ./
COPY . .

RUN make dependences
RUN make start


EXPOSE 80
CMD make start_docker