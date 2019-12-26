#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fabric.api import *

# Muestra el estado del DNS de nuestra app

def StatusDns():
    run('curl http://sinhumo1920.westeurope.cloudapp.azure.com/status')

# Funcion para mantener la version anterior del microservicio

def GuardaVersionAnterior():
    run('cp -r ./proyectoiv19 oldproyectoiv19')

# Funcion para eliminar la version anterior
def EliminarVersionAnterior():
    run('rm -rf ./oldproyectoiv19')

# Funcion para eliminar el microservicio
def EliminarVersion():
    run('rm -rf ./proyectoiv19')

# Funcion para instalar requirements
def InstallReq():
    run('pip3 install -r ./proyectoiv19/requirements.txt')

# Funcion para clonar el repositorio
def ClonRepo():
    run('git clone https://github.com/juaneml/IV_1920_Proyecto.git proyectoiv19/')

# Funcion que actualiza el microservicio guardando una version anterior
# Para ello hacemos la llamada de la funcion GuardaVersionAnterior
# Posteriormente clonamos el repositorio del microservicio con la funcion ClonRepo
# Por ultimo instalamos requirements haciendo uso de la funcion InstallReq

def MicroservicioSecure():
    ## Se guarda la version anterior
    GuardaVersionAnterior()
    # Eliminamos contenido
    EliminarVersion()
    # Clonamos nuestro respositorio de github
    ClonRepo()
    ## Instalamos requirements.txt
    InstallReq()

# Funcion que actualiza el microservicio  sin la version anterior
# Para ello hacemos la llamada de la funcion EliminarVersion
# Posteriormente clonamos el repositorio del microservicio con la funcion ClonRepo
# Por ultimo instalamos requirements haciendo uso de la funcion InstallReq

def MicroservicioClean():
    # Eliminamos la carpeta almacenada y hacemos una clonacion del
    # repositorio
    EliminarVersion()
    ClonRepo()
    ## Instalamos requirements.txt
    InstallReq()

# Funcion para iniciar el microservicio
def LanzarApp():
    run('cd ./proyectoiv19/src/ && sudo gunicorn proyecto-dep-app:__hug_wsgi__ -b 0.0.0.0:80 --name proyecto')

# Funcion para parar el microservicio
def StopApp():
    run('pm2 stop proyecto')