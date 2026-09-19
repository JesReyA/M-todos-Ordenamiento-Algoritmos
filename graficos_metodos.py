#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 11:50:26 2026
"""

import pandas as pd
import matplotlib.pyplot as plt

if __name__=="__main__":
    datos=pd.read_csv("burbuja_tiempo.csv",sep=";")
    datosDos=pd.read_csv("insercion_tiempo.csv",sep=";")
    x=datos.N
    y=datos.Tiempo
    yy=datosDos.Tiempo
    plt.plot(x,y,x,yy)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.title("Burbuja Vs Insercion")
    plt.legend(('burbuja', 'insercion'),prop={'size':10},loc='upper right')
    plt.grid()
    plt.show()
    
    datos=pd.read_csv("burbuja_tiempo.csv",sep=";")
    datosDos=pd.read_csv("seleccion_tiempo.csv",sep=";")
    x=datos.N
    y=datos.Tiempo
    yy=datosDos.Tiempo
    plt.plot(x,y,x,yy)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.title("Burbuja Vs Seleccion")
    plt.legend(('burbuja', 'seleccion'),prop={'size':10},loc='upper right')
    plt.grid()
    plt.show()
    
    datos=pd.read_csv("burbuja_tiempo.csv",sep=";")
    datosDos=pd.read_csv("mezcla_tiempo.csv",sep=";")
    x=datos.N
    y=datos.Tiempo
    yy=datosDos.Tiempo
    plt.plot(x,y,x,yy)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.title("Burbuja Vs Mezcla")
    plt.legend(('burbuja', 'mezcla'),prop={'size':10},loc='upper right')
    plt.grid()
    plt.show()
    
    #Logaritmica
    datos=pd.read_csv("burbuja_tiempo.csv",sep=";")
    datosDos=pd.read_csv("mezcla_tiempo.csv",sep=";")
    x=datos.N
    y=datos.Tiempo
    yy=datosDos.Tiempo
    plt.plot(x,y,x,yy)
    plt.yscale("symlog", linthresh=1e-4)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.title("Burbuja Vs Mezcla")
    plt.legend(('burbuja', 'mezcla'),prop={'size':10},loc='upper right')
    plt.grid()
    plt.show()
    
    datos=pd.read_csv("burbuja_tiempo.csv",sep=";")
    datosDos=pd.read_csv("quicksort_tiempo.csv",sep=";")
    x=datos.N
    y=datos.Tiempo
    yy=datosDos.Tiempo
    plt.plot(x,y,x,yy)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.title("Burbuja Vs Quicksort")
    plt.legend(('burbuja', 'quicksort'),prop={'size':10},loc='upper right')
    plt.grid()
    plt.show()
    
    #Comparacion con y de forma logaritmica en casos donde hay mucha diferencia y no se aprecia, se harán ambos tipos de grafica
    datos=pd.read_csv("burbuja_tiempo.csv",sep=";")
    datosDos=pd.read_csv("quicksort_tiempo.csv",sep=";")
    x=datos.N
    y=datos.Tiempo
    yy=datosDos.Tiempo
    plt.plot(x,y,x,yy)
    plt.yscale("symlog", linthresh=1e-4)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.title("Burbuja Vs Quicksort")
    plt.legend(('burbuja', 'quicksort'),prop={'size':10},loc='upper right')
    plt.grid()
    plt.show()
    
    datos=pd.read_csv("insercion_tiempo.csv",sep=";")
    datosDos=pd.read_csv("seleccion_tiempo.csv",sep=";")
    x=datos.N
    y=datos.Tiempo
    yy=datosDos.Tiempo
    plt.plot(x,y,x,yy)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.title("Insercion Vs Seleccion")
    plt.legend(('insercion', 'seleccion'),prop={'size':10},loc='upper right')
    plt.grid()
    plt.show()
    
    datos=pd.read_csv("insercion_tiempo.csv",sep=";")
    datosDos=pd.read_csv("mezcla_tiempo.csv",sep=";")
    x=datos.N
    y=datos.Tiempo
    yy=datosDos.Tiempo
    plt.plot(x,y,x,yy)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.title("Insercion Vs Mezcla")
    plt.legend(('insercion', 'mezcla'),prop={'size':10},loc='upper right')
    plt.grid()
    plt.show()
    
    #Logaritmica
    datos=pd.read_csv("insercion_tiempo.csv",sep=";")
    datosDos=pd.read_csv("mezcla_tiempo.csv",sep=";")
    x=datos.N
    y=datos.Tiempo
    yy=datosDos.Tiempo
    plt.plot(x,y,x,yy)
    plt.yscale("symlog", linthresh=1e-4)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.title("Insercion Vs Mezcla")
    plt.legend(('insercion', 'mezcla'),prop={'size':10},loc='upper right')
    plt.grid()
    plt.show()
    
    datos=pd.read_csv("insercion_tiempo.csv",sep=";")
    datosDos=pd.read_csv("quicksort_tiempo.csv",sep=";")
    x=datos.N
    y=datos.Tiempo
    yy=datosDos.Tiempo
    plt.plot(x,y,x,yy)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.title("Insercion Vs Quicksort")
    plt.legend(('insercion', 'quicksort'),prop={'size':10},loc='upper right')
    plt.grid()
    plt.show()
    
    #Logaritmica
    datos=pd.read_csv("insercion_tiempo.csv",sep=";")
    datosDos=pd.read_csv("quicksort_tiempo.csv",sep=";")
    x=datos.N
    y=datos.Tiempo
    yy=datosDos.Tiempo
    plt.plot(x,y,x,yy)
    plt.yscale("symlog", linthresh=1e-4)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.title("Insercion Vs Quicksort")
    plt.legend(('insercion', 'quicksort'),prop={'size':10},loc='upper right')
    plt.grid()
    plt.show()
    
    datos=pd.read_csv("seleccion_tiempo.csv",sep=";")
    datosDos=pd.read_csv("mezcla_tiempo.csv",sep=";")
    x=datos.N
    y=datos.Tiempo
    yy=datosDos.Tiempo
    plt.plot(x,y,x,yy)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.title("Seleccion Vs Mezcla")
    plt.legend(('seleccion', 'mezcla'),prop={'size':10},loc='upper right')
    plt.grid()
    plt.show()
    
    #Logaritmica
    datos=pd.read_csv("seleccion_tiempo.csv",sep=";")
    datosDos=pd.read_csv("mezcla_tiempo.csv",sep=";")
    x=datos.N
    y=datos.Tiempo
    yy=datosDos.Tiempo
    plt.plot(x,y,x,yy)
    plt.yscale("symlog", linthresh=1e-4)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.title("Seleccion Vs Mezcla")
    plt.legend(('seleccion', 'mezcla'),prop={'size':10},loc='upper right')
    plt.grid()
    plt.show()
    
    datos=pd.read_csv("seleccion_tiempo.csv",sep=";")
    datosDos=pd.read_csv("quicksort_tiempo.csv",sep=";")
    x=datos.N
    y=datos.Tiempo
    yy=datosDos.Tiempo
    plt.plot(x,y,x,yy)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.title("Seleccion Vs Quicksort")
    plt.legend(('seleccion', 'quicksort'),prop={'size':10},loc='upper right')
    plt.grid()
    plt.show()
    
    #Logaritmica
    datos=pd.read_csv("seleccion_tiempo.csv",sep=";")
    datosDos=pd.read_csv("quicksort_tiempo.csv",sep=";")
    x=datos.N
    y=datos.Tiempo
    yy=datosDos.Tiempo
    plt.plot(x,y,x,yy)
    plt.yscale("symlog", linthresh=1e-4)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.title("Seleccion Vs Quicksort")
    plt.legend(('seleccion', 'quicksort'),prop={'size':10},loc='upper right')
    plt.grid()
    plt.show()
    
    datos=pd.read_csv("mezcla_tiempo.csv",sep=";")
    datosDos=pd.read_csv("quicksort_tiempo.csv",sep=";")
    x=datos.N
    y=datos.Tiempo
    yy=datosDos.Tiempo
    plt.plot(x,y,x,yy)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.title("Mezcla Vs Quicksort")
    plt.legend(('mezcla', 'quicksort'),prop={'size':10},loc='upper right')
    plt.grid()
    plt.show()