#!/usr/bin/env python
# -*- coding: utf-8 -*-
# principal.py

import usuario
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
    day = 0
    din_aho = 0
    tipo_tab = []
    marca  = []
    num_cigar = 0
    logs = []

    def __init__(self):
        self.day = 0
        self.din_aho = 0
        self.marca = []
        self.num_cigar = 0

    
    """ Devuelve el número de días que el usuario lleva sin fumar"""
    def get_day(self):
        return self.day

    """ Devuelve el dinero ahorrado en euros """
    def get_diner(self):
        return self.din_aho

    """ Devuelve el tipo de tabaco """
    def get_tab(self):
        return self.tipo_tab

    """ Devuelve la marca """
    def get_marca(self):
        return self.marca

    """ Devuelve el numero de cigarrillos """
    def get_Ncigar(self):
        return self.num_cigar

    """ Devuelve los logs de los usuarios """

    def get_logs(self):
        return self.logs
