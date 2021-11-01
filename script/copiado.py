# -*- coding: utf-8 -*-
"""
Autor: Ricardo Vera Escobar

Este script automatiza la copia de los archivos ACREDITACION y ACREDITACIONRECHAZOS

Editado por Melina Urruchua - 22 Enero 2021
"""
import time, os, logging, json, xlrd, pyperclip, time, random, datetime
from Reemplazo import dia_valido, mes_valido, Configuracion, generar, renombradoFecha, createSSHClient
from scp import SCPClient

# Inicializa la configuracion del log
logging.basicConfig(filename='error.log',level=logging.INFO)

try:
    #tomo el path donde esta ubicado el script
    dir_path = os.path.dirname(os.path.realpath(__file__))
        
    #ingresar Mes proceso
    str_mes = input("Ingrese mes proceso:")
    while not mes_valido(str_mes):
        print("Ingrese un valor de mes correcto de 1 a 12")
        str_mes = input("Ingrese mes proceso:")
    if (len(str_mes) == 1):
        str_mes = '0' + str_mes
        
    #ingresar dia proceso
    str_dia = input("Ingrese día proceso:")
    while not dia_valido(str_dia, int(str_mes)):
        print("Ingrese un valor de dia correcto")
        str_dia = input("Ingrese día proceso:")
    if (len(str_dia) == 1):
        str_dia = '0' + str_dia

    # ingresar numero de paquete
    pkg = input("Ingrese nro PKG:")
    
    #cargo la baseline desde el json de datos para luego preguntar si hay que cambiarla
    try:
        with open('datos_entrada.json', 'r') as file:
            config = json.load(file)
    except Exception as err:
        print("Ocurrió un error al abrir archivo de configuración: ", err)
    baseline = config.get('BASELINE', '') 
    cambiarBaseline = input("La baseline actual es: " + baseline +', desea cambiarla? S/N\n')
    if cambiarBaseline == 'S' or cambiarBaseline == 's':
        baseline = input("Escriba la nueva baseline: \n")
    
    year = datetime.datetime.now().strftime("%y")
    #guardo el json con los datos actualizados
    data = {'FECHA': str_dia+'/'+str_mes+'/'+year,
            'BASELINE': baseline,
            'EXCEL': 'MR Col Ext V.'+baseline[22:27].replace('-','.')+'.xls',
            'SHEET': str_dia+'_'+str_mes,
            'PATH': dir_path,
            'CABECERA_ARCH': r'101 019101910 0000000102002071808C094101CREDICOP              1COEL S.A.                     0',
            'CABECERA_LOTE': r'5200                                              TRCREVERSAL  2002062002070001028502850000002',
            'CTRL_FIN_LOTE': r'82000000240045844733000000000000000083875313                                   028502850000002',
            'CTRL_FIN_ARCH': r'9000064000192000017811874315503003399086856002172843477                                      0',
            'CABECERA_ARCH_D': r'101 069101910 0500000102002071808N094101CREDICOP               COELSA                        0',
            'CABECERA_LOTE_D': r'5200                                    0000000000TRC          2002062002070001069101910000001',
            'CTRL_FIN_LOTE_D': r'82000000000000000000000000000000000000000000                                   069101910000001',
            'CTRL_FIN_ARCH_D': r'9000001000001000000000000000000000000000000000000000000                                      0',
            'STR_CR0': 'CR0'+str_dia+'002.191',
            'STR_CR1': 'CR1'+str_dia+'352.191',
            'STR_CH0': 'CH0'+str_dia+'072.191',
            'STR_CH1': 'CH1'+str_dia+'288.191',
            'STR_CRN': 'CRN'+str_dia+'129.191'
            }
    with open('datos_entrada.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)
        
    print("Aguarde un momento hasta que finalice el robot.")
    
    #Obtiene archivos de cliente remoto por ssh
    ssh = createSSHClient("10.6.17.88","22","mbuv","dGPZXy09")
    scp = SCPClient(ssh.get_transport())
    scp.get('/opt/guv/coelsa/enviados/CRD'+str_mes+str_dia+'1.191')
    scp.get('/opt/guv/coelsa/enviados/CRD'+str_mes+str_dia+'3.191')
    scp.get('/opt/guv/coelsa/enviados/CRP'+str_mes+str_dia+'1.191')
    scp.get('/opt/guv/coelsa/enviados/CRP'+str_mes+str_dia+'2.191')
    scp.get('/opt/guv/coelsa/enviados/CRP'+str_mes+str_dia+'3.191')
    
    renombradoFecha(str_mes, str_dia, dir_path)
    time.sleep(1)
    generar(int(str_mes), int(str_dia), pkg)
    time.sleep(1)
    from subida import subida_crecer
    subida_crecer(dir_path, str_mes, str_dia)

except Exception as e:
    logging.exception(time.ctime() + str(e))
    print('Ha ocurrido un error. Presione enter para salir.')
    input()
    