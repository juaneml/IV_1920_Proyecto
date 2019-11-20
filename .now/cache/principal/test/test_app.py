#!/usr/bin/env python
# -*- coding: utf-8 -*-
# test.py

import sys
import pytest
import unittest
import json
import requests

sys.path.append('../src/')
from principal import *
from usuario import *

from proyecto_app import *

url = 'http://localhost:8000/'

# '/lista_usuarios'
# '/datos_calculados'
# '/moneda'
# '/version'

class TestMethods(unittest.TestCase):

    ''' url raiz '''

    def test_url_raiz(self):
        response = requests.get(url)
        self.assertEqual(response.json()['status'],'OK', "Aplicación con status OK")
    
    ''' url status '''

    def test_url_status(self):
        path = url + 'status'
        response = requests.get(path)
        self.assertEqual(response.json()['status'],'OK', "Aplicación con status OK")

    ''' url lista usuarios '''

    def test_lista_usu(self):
        path = url + 'lista_usuarios'
        response = requests.get(path)
        self.assertEqual(response.status_code, 200, "Url existente, status 200")

    ''' url datos calculados '''

    def test_datos_cal(self):
        path = url + 'datos_calculados'
        response = requests.get(path)
        self.assertEqual(response.status_code, 200, "Url existente, status 200")
    
    ''' url moneda '''

    def test_moneda(self):
        path = url + 'moneda'
        response = requests.get(path)
        self.assertEqual(response.status_code, 200, "Url existente, status 200")

    ''' url versión '''

    def test_version(self):
        path = url + 'version'
        response = requests.get(path)
        self.assertEqual(response.status_code, 200, "Url existente, status 200")


    

if __name__ == '__main__':
    unittest.main()
    

    
