#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:57:22 2026

@author: j
"""

#from MetodosOrdenamiento import  metodo_burbuja
import MetodosOrdenamiento
import random as rn
import copy
from time import time

def crear_lista(longitud):
    lista= []
    for i in range(0, longitud):
        lista.append(rn.randint(0, 200))
    return lista

if __name__ == "__main__":  
    archivo= open("m2.csv", "w")
    archivo.write("N;Tiempo\n")
    lista = crear_lista(10000)
    x=100
    
    for i in range(100, 10010, 100):
        lista_nueva = copy.deepcopy(lista[:x])
        inicio_tiempo=time()
        MetodosOrdenamiento.metodo_quicksort(lista_nueva)
        transcurrido=time()-inicio_tiempo
        archivo.write(str(x) + ";" +format(transcurrido, '.5f')+"\n")
        x=x+100
    archivo.close()
    
