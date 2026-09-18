#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:57:22 2026
"""

import MetodosOrdenamiento
import random as rn
from time import time

def crear_lista(longitud):
    lista= []
    for i in range(0, longitud):
        lista.append(rn.randint(0, 200))
    return lista

if __name__ == "__main__":  
    lista = crear_lista(10000)
    
    
    archivo_burbuja= open("burbuja_tiempo.csv", "w")
    archivo_burbuja.write("N;Tiempo\n")
    for i in range(100, 10010, 100):
        lista_burbuja = lista[:i]
        inicio_tiempo=time()
        MetodosOrdenamiento.metodo_burbuja(lista_burbuja)
        transcurrido=time()-inicio_tiempo
        archivo_burbuja.write(str(i) + ";" +format(transcurrido, '.5f')+"\n")
        archivo_burbuja.flush()
    archivo_burbuja.close()
    

    archivo_insercion= open("insercion_tiempo.csv", "w")
    archivo_insercion.write("N;Tiempo\n")
    for i in range(100, 10010, 100):
        lista_insercion = lista[:i]
        inicio_tiempo=time()
        MetodosOrdenamiento.metodo_insercion(lista_insercion)
        transcurrido=time()-inicio_tiempo
        archivo_insercion.write(str(i) + ";" +format(transcurrido, '.5f')+"\n")
        archivo_insercion.flush()
    archivo_insercion.close()
    
    
    archivo_seleccion= open("seleccion_tiempo.csv", "w")
    archivo_seleccion.write("N;Tiempo\n")
    for i in range(100, 10010, 100):
        lista_seleccion = lista[:i]
        inicio_tiempo=time()
        MetodosOrdenamiento.metodo_seleccion(lista_seleccion)
        transcurrido=time()-inicio_tiempo
        archivo_seleccion.write(str(i) + ";" +format(transcurrido, '.5f')+"\n")
        archivo_seleccion.flush()
    archivo_seleccion.close()
    
    
    archivo_mezcla= open("mezcla_tiempo.csv", "w")
    archivo_mezcla.write("N;Tiempo\n")
    for i in range(100, 10010, 100):
        lista_mezcla = lista[:i]
        inicio_tiempo=time()
        MetodosOrdenamiento.metodo_mezcla(lista_mezcla)
        transcurrido=time()-inicio_tiempo
        archivo_mezcla.write(str(i) + ";" +format(transcurrido, '.5f')+"\n")
        archivo_mezcla.flush()
    archivo_mezcla.close()
    
    
    archivo_quicksort= open("quicksort_tiempo.csv", "w")
    archivo_quicksort.write("N;Tiempo\n")
    for i in range(100, 10010, 100):
        lista_quicksort =lista[:i]
        inicio_tiempo=time()
        lista_quicksort = MetodosOrdenamiento.metodo_quicksort(lista_quicksort)
        transcurrido=time()-inicio_tiempo
        archivo_quicksort.write(str(i) + ";" +format(transcurrido, '.5f')+"\n")
        archivo_quicksort.flush()
    archivo_quicksort.close()
    