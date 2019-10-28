#!/usr/bin/env python
# -*- coding: utf-8 -*-
# usuario.py

import json
import os

from datetime import datetime, date, time, timedelta, timezone
import calendar

""" Clase usuario
    Tiene los atributos:
    - nombre: nombre del usuario
    - password: passwod del usuario
    - num_cigar: tiempo sin fumar
    

    En esta clase definiremos los datos para el usuario como el nombre la contraseña, numero de cigarillos diarios
"""

class Usuario:
    nombre = []
    password = []
    #progreso = 0
    num_cigar  = []
    num_usuarios = []
    marca = []
    lista_usuarios = []
    din_sin = []
    tipo = []

    def __init__(self):
        self.nombre = []    # nombre de cada usuario
        self.password = []  # contraseña de cada usuario
        self.progreso = []  # progreso de cada usuario
        self.marca = [] # marca de tabaco de cada usuario
        self.num_cigar = [] # número de cigarillos de cada usuario
        self.tipo = []
        self.lista_usuarios = [] # lista de usuarios

    """ Devuelve el nombre """
    def get_nombre(self,string):
        try:
            return self.nombre[string]
        except:
            return False

    """ Add el nombre  """
    def add_nombre(self,string):

        if(type(string) != int):
            self.nombre.append(string)
            return True
        else:
            return False
    
    """ Devuelve el progreso """
    def get_progreso(self,string):

        try:
            return (self.progreso[string])
        except:
            return False


    """ Devuelve días sin fumar """
    def get_diaSin(self,string):

        try:
            return (self.get_progreso(string)[0])
        except:
            return False

    """ Add el progreso """
    def add_progreso(self,string):

        if(type(string) != datetime):
            self.progreso.append(string)
            return True
        else:
            return False

    """ Devuelve el número de cigarros que fumaba por día  """

    def get_cigar(self,string):
        return self.num_cigar[string]  

    """ Add número de cigarros """
    def add_numCigar(self,int):

        if(type(int) != str):
            self.num_cigar.append(int)
            return True
        else:
            return False


    """ Devuelve la contraseña"""

    def get_password(self,string):
        return self.password[string]
    

    """ Cambia la contraseña """

    def set_password(self,string):

        if(type(string) != self):
            self.password = string
            return True
        else:
            return False

    """ Add password """
    def add_password(self,string):

        if(string != " "):
            self.password.append(string)
            return True
        
        else:
            return False


    """ Devuelve la marca """
    def get_marca(self,string):
        return self.marca[string]

    """ Añade la marca"""
    def add_marca(self,string):

        if(type(string) != int):
            self.marca.append(string)
            return True
        else:
            return False

    """ Devuelve el número de usuarios """
    def get_numUsuarios(self):
        return self.num_usuarios

    """ Devuelve el tipo de tabaco """

    def get_tipo(self,string):
        return self.tipo[string]


    """ Add tipo de tabaco """
    def add_tipo(self,string):

        if(type(string) != int):
            self.tipo.append(string)
            return True

        else:
            return False

    """ Cambia el nombre """
    def set_nombre(self,usu,string):
        self.nombre[usu] = string
    
    """ Cambia el número de cigarros """
    def set_numCigar(self,usu,int):
        self.num_cigar[usu] = int

    """ Cambia el progreso """
    def set_progreso(self,usu,string):
        self.progreso[usu] = string


    """ Cambia la marca """
    def set_marca(self,usu,string):
        self.marca[usu] = string


    """ Cambia el numero de usuarios """
    def set_numUsu(self,int):
        self.num_usuarios = int


    """ Cambia el tipo de tabaco """
    def set_tipo(self,string):
        self.tipo = string

        
    """ Crea usuarios """

    def crea_usu(self,lista):

        dic = lista
        self.num_usuarios = 0 # numero de usuarios

        for i in dic:
            if(i['name'] != None):
                self.lista_usuarios.append(self.add_nombre(i['name']))
            else:
                self.lista_usuarios.append(self.set_nombre(" "))

            if(i['password'] != None):
                self.lista_usuarios.append(self.add_password(i['password']))
            else:
                self.lista_usuarios.append(self.set_password(" "))

            if(i['n_cigar'] != None):
                self.lista_usuarios.append(self.add_numCigar(i['n_cigar']))
            else:
               self.lista_usuarios.append(self.add_numCigar(" "))

            if(i['marca'] != None):
                self.lista_usuarios.append(self.add_marca(i['marca']))
            
            else:
                self.lista_usuarios.append(self.add_marca(" "))
            
            if (i['tipo'] != None):
                self.lista_usuarios.append(self.add_tipo(i['tipo']))
            
            else:
                self.lista_usuarios.append(self.add_tipo(" "))

            if(i['progres'] != None):
                
                fecha1 = datetime.now()
                diferencia = fecha1 - datetime.strptime(i['progres'],'%Y-%m-%dT%H:%M:%S')

                self.progreso.append([diferencia.days, "días",str("{0:.2f}").format(diferencia.seconds/60), "minutos y",diferencia.seconds, "seg."])

            else:
                self.lista_usuarios.append(self.set_progreso(" "))

            
            
            self.num_usuarios+=1
            self.set_numUsu(self.num_usuarios)
            

    def to_s(self,i):
        var = {"Nombre": self.get_nombre(i),"Password": self.get_password(i),"Num. cigarillos": self.get_cigar(i),"Marca": self.get_marca(i),"Progreso": self.get_progreso(i)}
        return var
       
