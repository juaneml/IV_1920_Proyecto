#!/usr/bin/env python
# -*- coding: utf-8 -*-
# usuario.py

import json
import os

""" Clase usuario
    Tiene los atributos:
    - nombre: nombre del usuario
    - password: passwod del usuario
    - progreso: tiempo sin fumar
    - ahorro: dinero en euros ahorrado 

    En esta clase definiremos los datos para el usuario como el nombre la contraseña, progreso y dinero ahorrado
"""

class Usuario:
    nombre = []
    password = []
    progreso = 0
    ahorro  = 0

    def __init__(self):
        self.nombre = []
        self.password = []
        self.progreso = 0
        self.ahorro = 0

    """ Devuelve el nombre """
    def get_nombre(self,string):
        try:
            return self.nombre[string]
        except:
            return False
    
    """ Devuelve el progreso """
    def get_progreso(self,string):
        try:
            return self.progreso
        except:
            return False

    """ Devuelve el ahorro del dinero en euros """

    def get_ahorro(self,string):
            return self.ahorro  


    """ Cambia la contraseña """

    def set_password(self,string):

        if(type(string) != self):
            self.password = string
            return True
        else:
            return False         
        


    