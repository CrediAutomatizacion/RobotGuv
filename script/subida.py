# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:49:09 2020

@author: rvescobar

Editado por Melina Urruchua
"""

import logging, random, time
from Reemplazo import Configuracion, createSSHClient
from scp import SCPClient

def subida_crecer(dir, str_mes, str_dia):
    # Inicializa la configuracion del log
    logging.basicConfig(filename='error.log',level=logging.INFO)
    
    try:
        #Copia los archivos generados al cliente remoto por ssh
        ssh = createSSHClient("10.6.17.88","22","mbuv","dGPZXy09")
        scp = SCPClient(ssh.get_transport())
        scp.put("./CH0" + str_dia + "072.191", "/opt/guv/coelsa/enviados/CH0" + str_dia + "072.191")
        scp.put("./CH1" + str_dia + "288.191", "/opt/guv/coelsa/enviados/CH1" + str_dia + "288.191")
        scp.put("./CRN" + str_dia + "129.191", "/opt/guv/coelsa/enviados/CRN" + str_dia + "129.191")
        scp.put("./CR0" + str_dia + "002.191", "/opt/guv/coelsa/enviados/CR0" + str_dia + "002.191")
        scp.put("./CR1" + str_dia + "352.191", "/opt/guv/coelsa/enviados/CR1" + str_dia + "352.191")
        
        time.sleep(5)
        print("Ha finalizado la ejecución. Presione enter para salir.")
        input()
    except Exception as e:
        logging.exception('Error occurred ' + str(e))
        print('Ha ocurrido un error. Presione enter para salir.')
        input()