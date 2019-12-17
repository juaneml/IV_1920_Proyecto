# IV_1920_Proyecto
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docu: Docu](https://img.shields.io/static/v1?label=Documentación&message=si&color=success)](https://juaneml.github.io/doc_IV-1920_Proyecto/)
[![Build Status](https://travis-ci.org/juaneml/IV_1920_Proyecto.svg?branch=master)](https://travis-ci.org/juaneml/IV_1920_Proyecto)
[![CircleCI](https://circleci.com/gh/juaneml/IV_1920_Proyecto.svg?style=svg)](https://circleci.com/gh/juaneml/IV_1920_Proyecto)
[![codecov](https://codecov.io/gh/juaneml/IV_1920_Proyecto/branch/master/graph/badge.svg)](https://codecov.io/gh/juaneml/IV_1920_Proyecto)
[![Coverage Status](https://coveralls.io/repos/github/juaneml/IV_1920_Proyecto/badge.svg?branch=master)](https://coveralls.io/github/juaneml/IV_1920_Proyecto?branch=master)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-360/)

- Repositorio para el proyecto de Infraestructura Virtual.

## Descripción

- El proyecto que se va a realizar es sobre un microservicio para dejar de fumar.
  
- El microservicio proporcionará los días que un usuario lleva sin fumar a partir del día que se indique que ha empezado a dejar de fumar.
  
- El usuario podrá ver el dinero que lleva ahorrado a partir del día que se indique que ha dejado de fumar, para ello el usuario deberá introducir el tipo de tabaco, tabaco de liar o industrial,la marca y los cigarrillos que fumaba diariamente, el microservicio a partir de esos datos proporcinará la cantidad de dinero en euros.

## Motivación

- La creación de este microservicio es por interés personal ya que veo que en la sociedad las personas no son conscientes de la gravedad de fumar y el gasto que produce fumar.

## Test
[Test](https://github.com/juaneml/IV_1920_Proyecto/tree/master/test)

## Herramienta de construcción
[Makefile](/doc/herramienta_construcción.md)


## Rutas
[Rutas](/doc/doc_clases.md)

~~~
buildtool: Makefile
~~~

## PaaS [Heroku](https://www.heroku.com)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://proyecto-iv-19.herokuapp.com/)

- Despliegue enla plataforma Heroku

- [Documentación Heroku](doc/heroku.md)

## Paas [Azure](https://azure.microsoft.com)
- Desplieque en la plataforma Azure.
  
- [Documentación Azure](doc/azure.md)

## Despliegue

~~~~
Despliegue: https://proyecto-iv-19.herokuapp.com/

Despliegue 2: https://proyecto-iv-19.azurewebsites.net/
~~~~

## Despliegue con Docker

Contenedor: https://proyecto-iv-19-docker.herokuapp.com/

Contenedor: https://docker-proyecto-iv-19.azurewebsites.net/


- [Documentación Docker](doc/docker.md)

## [Docker Hub](https://hub.docker.com)
Dockerhub: https://hub.docker.com/r/juaneml/proyecto-iv-19


## Provisionamiento
provision: provision/playbook.yml

- [Documentación provisionamiento](doc/doc_provision.md)
## Documentación
- Para más información consulta: [Documentación](https://github.com/juaneml/IV_1920_Proyecto/tree/master/doc).


