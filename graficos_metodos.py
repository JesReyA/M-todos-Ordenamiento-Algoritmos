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