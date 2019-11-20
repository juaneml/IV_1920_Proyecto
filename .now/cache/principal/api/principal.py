#!/usr/bin/env python
# -*- coding: utf-8 -*-
# principal.py


from api.usuario import Usuario
import json
import os
import sys

""" Clase principal para el servicio en esta clase se va a definir
    Los atributos:
    - day: para los contar los días
    - din_aho: dinero ahorrado
    - tipo_tab: tipo de tabaco
    - marca: marca del tabaco
    - num_cigar: número de cigarrillos diarios
    - logs: los logs para cada usuario

    Obtendremos los datos que tenemos almacenados del usuario de nuestra base de datos
    que ya han sido facilitados por el usuario
 """
 
class Servicio:
    day = []
    din_aho = []
    tipo_tab = []
    marca  = []
    num_cigar = []
    precio = 0
    lista_tabaco = []
    num_usuarios = 0
    logs = []
    progres = []
    moneda = " "

    def __init__(self):
        self.tipo_tab = []
        self.day = []
        self.din_aho = []
        self.marca = []
        self.num_cigar = []
        self.lista_tabaco = []
        self.precio = []
        self.num_usuarios = 0
        self.progres = []
        self.moneda = " "

    
    """ Devuelve el número de días que el usuario lleva sin fumar"""
    def get_day(self,int):
        try:
            return self.day[int]
        except:
            return False

    """ Devuelve el dinero ahorrado en euros """
    def get_dinAho(self,string):
        try:
            return self.din_aho[string]
        except:
            return False


    """ Devuelve la marca """
    def get_marca(self,string):
        try:
            return self.marca[string]
        except:
            return False

    """ Devuelve el numero de cigarrillos """
    def get_Ncigar(self,string):
        #try:
        return self.num_cigar[string]
        #except:
        #    return False

    """ Devuelve los logs de los usuarios """
    def get_logs(self):
        #try:
        return self.logs
        #except:
        #    return False
    
    """ Devuelve el número de usuarios """
    def get_numUsuarios(self):
        #try:
        return self.num_usuarios
        #except:
        #    return False

    """ Devuelve la moneda """

    def get_moneda(self):
        #try:
        return self.moneda
        #except:
        #    return False

    """ Cambia la moneda """
    def set_moneda(self,string):
        if(type(string) != int):
            self.moneda = string
            return True
        else:
            return False

    """ Add nombre marca """
    def add_marca(self,string):
       
        if(type(string) != int):
            self.marca.append(string)
            return True
        #else:
        #    return False

    
    """ Add tipo de tabaco """

    def add_tipo(self,string):

        if(type(string) != int):

            self.tipo_tab.append(string)
            return True
        
        #else:
        #    return False
    
    """ Devuelve el tipo de tabaco"""
    def get_tipo(self,int):
        return self.tipo_tab[int]


    """ Add número de cigarros """

    def add_numCigar(self,int):

        if(type(int) != str):
            self.num_cigar.append(int)
            return True

        #else:
        #    return False

    """ add Dinero ahorrado
        num: numero de cigarros
        marca: marca del tabaco
        tipo: tipo de tabaco, liar o industrial
        dias: dias que el usuario lleva sin fumar
    """ 
    def add_dinAho(self,num,marca,tipo,dias):
        num_cigar = num 
        marca = marca 
        tipo = tipo     
        precio_uno = 0   
        dinAho_dia = 0  
        dinAho = 0.0    
        if(type(num) != str and type(marca) != int and type(dias) != str):
            if (marca == "MarcaA" and tipo == "Industrial"):
                precio_uno = 4.50 / 20.0
                dinAho_dia = precio_uno * num_cigar
                dinAho = dinAho_dia * dias
            
            if (marca == "MarcaB" and tipo == "Industrial"):
                precio_uno = 4.80 / 20.0
                dinAho_dia = precio_uno * num_cigar
                dinAho = dinAho_dia * dias
                
            if (marca == "MarcaC" and tipo == "Industrial"):
                precio_uno = 5.0 / 20.0
                dinAho_dia = precio_uno * num_cigar
                dinAho = dinAho_dia * dias 
            
            
            if (marca == "MarcaD" and tipo == "Liar"):
                precio_uno = 3.5 / 30.0
                dinAho_dia = precio_uno * num_cigar
                dinAho = dinAho_dia * dias 
            
            if (marca == "MarcaE" and tipo == "Liar"):
                precio_uno = 3.75 / 30.0
                dinAho_dia = precio_uno * num_cigar
                dinAho = dinAho_dia * dias 
        
            self.din_aho.append(dinAho)
        return True
        #else:
        #    return False
       

    """ Add progress """
    def add_progreso(self, string):
            self.progres.append(string)

    """ Devuelve el progreso """

    def get_progreso(self,string):
        if(string < self.get_numUsuarios()):
            return self.progres[string]

    """ Cambia el número de usuarios """
    def set_numUsuarios(self,int):
        self.num_usuarios = int
    
    """ Cambia el nombre """
    #def set_marca(self,string):
    #    self.marca = string
    
    """ Cambia el tipo """
    #def set_tipo(self,string):
    #    self.tipo_tab = string

    """ Cambia la capacidad """
    #def set_capa(self,int):
    #    self.num_cigar = int

    """ Cambia el precio """
    #def set_precio(self,int):
    #    self.precio = int

    """ Cambia el numero de cigarros """
    #def set_cigar(self,int):
    #    self.num_cigar = int


    """ Imprime la lista de los usuarios:
        - Nombre usuario
        - Marca de tabaco
        - Tipo
        - Num. cigarros
        - Progreso y dinero ahorrado 
    """

    def to_s(self,i,lista):
        if(type(i) != str):
            var = {"Nombre":lista.get_nombre(i),"marca": self.get_marca(i),"Tipo": self.get_tipo(i),"Num. cigarillos": lista.get_cigar(i),
            "Progreso": self.get_progreso(i),"Dinero Ahorrado": str(self.get_dinAho(i))+self.get_moneda() }
            return var
        #else:
        #    return False

    """ Imprime Nombre,progreso y dinero ahorrado """
    def to_Simple(self,i,lista):
        if(type(i) != str and i< self.get_numUsuarios()):
            var = {"Nombre" : lista.get_nombre(i),"Progreso": self.get_progreso(i),
            "Dinero Ahorrado": str(self.get_dinAho(i))+self.get_moneda()}
        return var

    """ crea sistema """
    def crea_sistema(self,usuario,num_usu,lista):
        self.set_numUsuarios(num_usu)
        if(type(lista) == list):
            dic = lista
            
            usuarios = self.set_numUsuarios(num_usu)

            for i in dic:
                if(i['name'] != None):
                    self.lista_tabaco.append(self.add_marca(i['name']))
                
                if(i['tipo'] != None):
                    self.lista_tabaco.append(self.add_tipo(i['tipo']))

                if(i['capacidad'] != None):
                    self.lista_tabaco.append(self.add_numCigar(i['capacidad']))
                
                if(i['precio'] != None):
                    self.lista_tabaco.append(self.add_marca(i['precio']))

                if(i['moneda'] != None):
                    self.set_moneda(i['moneda'])
   
        
            for j in range(self.num_usuarios):
                self.lista_tabaco.append(self.add_dinAho(usuario.get_cigar(j),usuario.get_marca(j),usuario.get_tipo(j),usuario.get_diaSin(j)))
                self.lista_tabaco.append(self.add_progreso(usuario.get_progreso(j)) )

                self.set_numUsuarios(num_usu)
                self.get_day(0)
                self.get_dinAho(0)
                self.get_Ncigar(0)
                self.get_logs()
                self.get_moneda()
                self.to_s(0,usuario)
                self.to_Simple(0,usuario)
                #self.get_progreso(0)
            return True
        #else:
        #    return False
