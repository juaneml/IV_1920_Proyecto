#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hug
import json



from principal import Servicio
from principal import Usuario
import sys
import os
sys.path.append('../src/')

import requests

with open('../json/datos.json','r') as usuarios:
    lista_usuarios = json.load(usuarios)
    
    usuario = Usuario()
    usuario.crea_usu(lista_usuarios)

    for i in range(usuario.get_numUsuarios()):
       lista_usuarios.append(usuario.to_s(i))

with open('../json/datos_tabaco.json','r') as marcas:
    lista_tabaco = json.load(marcas)

    serv = Servicio() 
    serv.crea_sistema(usuario,usuario.get_numUsuarios(),lista_tabaco)

    for i in range(serv.get_numUsuarios()):
       lista_tabaco.append(serv.to_Simple(i,usuario))
    

@hug.cli()
# @hug.get('/')
# def getEstado():
#     salida = {"status": "OK"}
#     return salida

@hug.get('/status')
def status():
    status = {"status": "OK"
    }
    return status

# rutas para comprobación

@hug.get('/lista_usuarios')
def lista_usus():
    
    salida = lista_usuarios
    return str(salida)

@hug.get('/datos_calculados')
def lista_tab():
    salida = lista_tabaco
    
    return salida

@hug.get('/moneda')
def moneda():
    #print(serv.to_Simple(1))
    salida = serv.get_moneda()
    return str({"Euro",salida})

@hug.post()
def method_post():
    salida={'Sistema': 'versión 0.5'}
    return str(salida)

@hug.get('/version')
def post():
    return method_post()
if __name__ == '__main__':

    una.interface.cli()
    all.interface.cli()