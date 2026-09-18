#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:52:04 2026

@author: j
"""

def metodo_burbuja(lista):
    for i in range (1,len(lista)):
        for j in range (0,len(lista)-i):
            if(lista[j] > lista[j+1]):
                tmp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = tmp

def metodo_insercion(lista):
    for i in range (1, len(lista)):
        valor_actual = lista[i]
        j = i-1
        while(j >= 0 and lista[j]>valor_actual):
            lista[j+1] = lista[j]
            j-=1
        lista[j+1]= valor_actual
        
                
    
def metodo_seleccion(lista):
    for i in range(len(lista)-1):
        menor = i
        for j in range(i+1, len(lista)):
            if(lista[j] < lista[menor]):
                menor = j
        tmp = lista[i]
        lista[i] = lista[menor]
        lista[menor] = tmp
                
    
def metodo_mezcla(lista):
    if(len(lista) <= 1):
        return
    mitad = len(lista) //2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    metodo_mezcla(izquierda)
    metodo_mezcla(derecha)
    
    i = 0 #izquierda
    j = 0 #derecha
    k= 0 #principal
    
    while (i < len(izquierda) and j< len(derecha)):
        if(izquierda[i] <= derecha[j]):
            lista[k] = izquierda[i]
            i +=1
            k+=1
        else:
            lista[k] = derecha[j]
            j +=1
            k+=1
        
    while(i < len(izquierda)):
        lista[k] = izquierda[i]
        i +=1
        k+=1
    
    while(j < len(derecha)):
        lista[k] = derecha[j]
        j +=1
        k+=1
            
        
def metodo_quicksort(lista):
    import random as rn
    if(len(lista) <= 1):
        return lista
    else:
        indice_pivote = rn.randint(0, len(lista)-1)
        pivote = lista[indice_pivote]
        sobrante = lista[:indice_pivote] + lista[indice_pivote+1:]
        menores_pivote = [i for i in sobrante if i <= pivote]
        mayores_pivote = [i for i in sobrante if i > pivote]
        return metodo_quicksort(menores_pivote) + [pivote] + metodo_quicksort(mayores_pivote)
    
        