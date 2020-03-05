# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 11:27:35 2020

@author: rvescobar
"""


import os
from xlrd import cellname
from Reemplazo import renombradoFecha, mes_valido, dia_valido, generar, Configuracion
from subida import subida_crecer

# TODO: pedir datos baseline y guardar en json, luego preguntar si la version es correcta
#       para cambiar el dato o no

int_mes = input("Ingrese mes proceso:")
while not mes_valido(int_mes):
    print("Ingrese un valor de mes correcto de 1 a 12")
    int_mes = input("Ingrese mes proceso:")

#ingresar dia proceso
int_dia = input("Ingrese día proceso:")
while not dia_valido(int_dia, int(int_mes)):
    print("Ingrese un valor de dia correcto")
    int_dia = input("Ingrese día proceso:")

    
dir_path = os.path.dirname(os.path.realpath(__file__))

subida_crecer(dir_path, int_mes, int_dia)

generar(int_mes,int_dia)





 
