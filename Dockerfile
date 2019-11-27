FROM python:3
#ENV PYTHON_VERSION 3.7.5
LABEL maintainer="juaneml@correo.ugr.es"
WORKDIR src/

COPY requirements.txt ./
COPY . .

RUN apt-get update
RUN apt-get -y install curl gnupg
RUN curl -sL https://deb.nodesource.com/setup_11.x  | bash -
RUN apt-get -y install nodejs

RUN make dependences
RUN make start


EXPOSE 80
CMD make start_docker