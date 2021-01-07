# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:39:02 2020

@author: eduardo.vitcop

Script que reemplaza datos de los archivos CRDdd041, CRDdd043, CRPdd041, CRPdd042
y CRPdd043 (donde dd es la fecha del día) y además los renombra y rediseña.


"""
import json
import sys, xlrd, random
from random import randint

class Configuracion:
    """Clase que toma los distintos valores para de la aplicacion desde el
        archivo datos_entrada.json"""

    def __init__(self):
        """Inicializa la clase tomando los valores desde el archivo
            datos_entrada.json"""

        try:
            with open('datos_entrada.json', 'r') as file:
                config = json.load(file)
        except Exception as err:
            print("Ocurrió un error al abrir archivo de configuración: ", err)

        self.fecha = config.get('FECHA', '')
        self.baseline = config.get('BASELINE', '')
        self.excel = config.get('EXCEL', '')
        self.sheet = config.get('SHEET', '')
        self.path = config.get('PATH','')
        self.cab_arch = config.get('CABECERA_ARCH', '')
        self.cab_lote = config.get('CABECERA_LOTE', '')
        self.fin_lote = config.get('CTRL_FIN_LOTE', '')
        self.fin_arch = config.get('CTRL_FIN_ARCH', '')
        self.str_cr0 = config.get('STR_CR0', '')
        self.str_cr1 = config.get('STR_CR1', '')
        self.str_ch0 = config.get('STR_CH0', '')
        self.str_ch1 = config.get('STR_CH1', '')
        self.str_crn = config.get('STR_CRN', '')
        self.cab_arch_d = config.get('CABECERA_ARCH_D', '')
        self.cab_lote_d = config.get('CABECERA_LOTE_D', '')
        self.fin_lote_d = config.get('CTRL_FIN_LOTE_D', '')
        self.fin_arch_d = config.get('CTRL_FIN_ARCH_D', '')
        
        
def mes_valido(mes):
    """ Valida que el mes sea un numero entre 1 y 12 """
    if not mes:
        return False
    if mes.isdigit():
        return 0 < int(mes) < 13
    return False

def dia_valido(dia, mes):
    """ Valida que el dia sea un numero entre 1 y 29/30/31 segun mes  """
    dias_x_mes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not dia:
        return False
    if dia.isdigit():
        return 0 < int(dia) <= dias_x_mes[mes - 1]
    return False

def renombradoFecha(int_mes, int_dia, dir_path):
    
    path = dir_path
    int_dia = int(int_dia)
    int_mes = int(int_mes)
    
    for i in range(0,4):
        ## Abrir archivo de texto
        str_dia = str(int_dia)
        if len(str_dia) == 1:
            str_dia = "0" + str_dia
        
        str_mes = str(int_mes)
        if len(str_mes) == 1:
            str_mes = "0" + str_mes
        
        if(i==0):
            #str_archivo_entrada = path + r'\\' + "CH0" + str_dia + "072.191"
            str_archivo_entrada = path + r'\\' + "CH007072.191"
            #print(str_archivo_entrada)
            
            try:
                with open(str_archivo_entrada, 'r') as infile:
                    data = infile.read()
                    my_list = data.splitlines()
            except Exception as err:
                print("Ocurrió un error al abrir archivo de entrada: ", err)
                sys.exit()
            
            str_archivo_salida = path + r'\\' + "CH0" + str_dia + "072.191"
            
            try:
                outfile = open(str_archivo_salida, 'w')
            except Exception as err:
                print("Ocurrió un error al crear archivo de salida: "+ str_archivo_salida + err)
                sys.exit()
                
            for line in range(len(my_list)):
                if line==0:
                    outfile.write(my_list[0][0:25] + str_mes + str_dia + my_list[0][29:] + '\n')
                if line==1:
                    outfile.write(my_list[1][0:65] + str_mes + '0'+ str(int_dia-1) + my_list[1][69:71] + str_mes + str_dia + my_list[1][75:] + '\n')
                if line>1: 
                    outfile.write(my_list[line] + '\n')
    
            outfile.close() 
            
        if(i==1):
            #str_archivo_entrada = path + "CH1" + str_dia + "288.191"
            str_archivo_entrada = path + r'\\' + "CH107288.191"
            #print(str_archivo_entrada)            
            
            try:
                with open(str_archivo_entrada, 'r') as infile:
                    data = infile.read()
                    my_list = data.splitlines()
            except Exception as err:
                print("Ocurrió un error al abrir archivo de entrada: ", err)
                sys.exit()
            
            str_archivo_salida = path + r'\\' + "CH1" + str_dia + "288.191"
            
            try:
                outfile = open(str_archivo_salida, 'w')
            except Exception as err:
                print("Ocurrió un error al crear archivo de salida: "+ str_archivo_salida + err)
                sys.exit()
                
            for line in range(len(my_list)):
                if line==0:
                    outfile.write(my_list[0][0:25] + str_mes + str_dia + my_list[0][29:] + '\n')
                if line==1:
                    outfile.write(my_list[1][0:65] + str_mes + '0'+ str(int_dia-1) + my_list[1][69:71] + str_mes + str_dia + my_list[1][75:] + '\n')
                if line>1:
                    outfile.write(my_list[line] + '\n')
          
            outfile.close()
                    
        if(i==2):
            #str_archivo_entrada = path + "CRN" + str_dia + "129.191"
            str_archivo_entrada = path + r'\\' + "CRN07129.191"
            #print(str_archivo_entrada)          
            
            try:
                with open(str_archivo_entrada, 'r') as infile:
                    data = infile.read()
                    my_list = data.splitlines()
            except Exception as err:
                print("Ocurrió un error al abrir archivo de entrada: ", err)
                sys.exit()
            
            str_archivo_salida = path + r'\\' + "CRN" + str_dia + "129.191"           
            
            try:
                outfile = open(str_archivo_salida, 'w')
            except Exception as err:
                print("Ocurrió un error al crear archivo de salida: "+ str_archivo_salida + err)
                sys.exit()
                
            for line in range(len(my_list)):
                if line==0:
                    outfile.write(my_list[0][0:25] + str_mes + str_dia + my_list[0][29:] + '\n')
                if line==1:
                    outfile.write(my_list[1][0:65] + str_mes + '0'+ str(int_dia-1) + my_list[1][69:71] + str_mes + str_dia + my_list[1][75:] + '\n')
                if line>1: 
                    outfile.write(my_list[line] + '\n')
    
            outfile.close()
    
def generar(int_mes, int_dia):
    # TODO: cambiar datos hardcodeados por variables
    
    data_conf = Configuracion()
    barra = r'\\'
    
    # Abro el excel para leer num de cheques y motivos de rechazo
    try:
        excel_path = r'\\sfs-1\\Testing\\Tareas en curso\\GUV\\Pruebas\\2020\\'       
        workbook = xlrd.open_workbook(excel_path+data_conf.baseline+barra+data_conf.excel)
        #workbook = xlrd.open_workbook(r'\\sfs-1\Testing\Tareas en curso\GUV\Pruebas\2020\BSLN_UV_AP_TEST_01-00-80-06_20200204-1900\MR Col Ext V.80.07.xls')
    except Exception as err:
                print("El documento: "+ data_conf.excel + " no existe", err)
                sys.exit()
    # el nombre de esta hoja cambia con el dia en que se ejecuta el robot
    try:
        worksheet = workbook.sheet_by_name(data_conf.sheet)
    except Exception as err:
                print("La hoja: "+ data_conf.sheet + " no existe",err)
    num_rows = worksheet.nrows - 1

    # Inicializo listas de numeros de cheque y de motivos de rechazo
    lista_num_cheque_excel_dep=['']
    lista_num_cheque_excel_gir=['']
    lista_mrdep_excel=['']
    lista_mrgir_excel=['']
    
    # Pueblo las listas de numeros de cheque y de motivos de rechazo
    curr_row = -1
    while curr_row < 82:
            curr_row += 1
            if curr_row < 40:
                if worksheet.cell(curr_row, 1).ctype == 2:
                    if worksheet.cell(curr_row, 0).value != 'AJUSTE 001':
                        lista_num_cheque_excel_dep.append(int(worksheet.cell(curr_row,1).value))
                        lista_mrdep_excel.append(int(worksheet.cell(curr_row,5).value))
                    else:
                        lista_num_cheque_excel_dep.append(88888888)
                        lista_mrdep_excel.append(int(worksheet.cell(curr_row,5).value))
            if curr_row > 39:
                if worksheet.cell(curr_row, 1).ctype == 2 and worksheet.cell(curr_row, 6).value != '':
                    lista_num_cheque_excel_gir.append(int(worksheet.cell(curr_row,1).value))
                    lista_mrgir_excel.append(int(worksheet.cell(curr_row,6).value))
    
    # Borro el indice 0 de listas de cheque y mr
    lista_num_cheque_excel_dep.remove('')
    lista_num_cheque_excel_gir.remove('')
    lista_mrdep_excel.remove('')
    lista_mrgir_excel.remove('')
     
    #Inicializo listas
    listade622 = ['']
    listade626 = ['']
    traceback622 = ['']
    traceback626 = ['']
  
    # Pueblo las listas de datos 622 y 626 CRDmmdd1 y CRDmmdd3
    for i in range(0,2):
        # Abrir archivo de texto
        str_dia = str(int_dia)
        if len(str_dia) == 1:
            str_dia = "0" + str_dia
        
        str_mes = str(int_mes)
        if len(str_mes) == 1:
            str_mes = "0" + str_mes
        
        if (i==0): #622 CRDmmdd1
            str_archivo_entrada = data_conf.path + barra + 'CRD' + str_mes + str_dia +'1.191'
            #str_archivo_entrada = r"D:\Users\rvescobar\Documents\python\robot recibidas enviadas\script\CRP02071.191"
            #print(str_archivo_entrada)      
            
            try:
                with open(str_archivo_entrada, 'r') as infile:
                    data = infile.read()
                    my_list = data.splitlines()
            except Exception as err:
                print("Ocurrió un error al abrir archivo de entrada: ", err)
                sys.exit()
            
            
            for line in range(len(my_list)):
                if "622" in my_list[line][0:3]:
                    listade626.append(my_list[line][3:64])
                    traceback626.append(my_list[line][79:])
            listade626.remove('')
            traceback626.remove('')
            
        if (i==1): #626 CRDmmdd3
            str_archivo_entrada = data_conf.path + barra + 'CRD' + str_mes + str_dia + '3.191'
            #str_archivo_entrada = r"D:\Users\rvescobar\Documents\python\robot recibidas enviadas\script\CRP02073.191"
            #print(str_archivo_entrada)      
            
            try:
                with open(str_archivo_entrada, 'r') as infile:
                    data = infile.read()
                    my_list = data.splitlines()
            except Exception as err:
                print("Ocurrió un error al abrir archivo de entrada: ", err)
                sys.exit()
            
            for line in range(len(my_list)):
                if "626" in my_list[line][0:3]:
                    listade622.append(my_list[line+1][27:35]+my_list[line][11:64])
                if "799" in my_list[line][0:3]:
                    traceback622.append(my_list[line][6:21])
            listade622.remove('')
            traceback622.remove('')  
            
    #----------------INICIO DE LA GENERACION DEL ARCHIVO CR1dd352.191----------------#
    # Creo el archivo de salida
    str_archivo_salida2 = data_conf.path + barra + 'CR1' + str_dia + "352.191"
    try:
        outfile = open(str_archivo_salida2, 'w')
    except Exception as err:
        print("Ocurrió un error al crear archivo: {}, {} "
              .format(str_archivo_salida2, err))
        sys.exit()
    
    dia_menos = str(int(int_dia)-1)
    if len(dia_menos)<2:
        dia_menos = '0'+dia_menos
    
    # Escribo los encabezados de lote y archivo con la fecha cambiada
    outfile.write(data_conf.cab_arch_d[:25]+str_mes+str_dia+data_conf.cab_arch_d[29:]+'\n')
    outfile.write(data_conf.cab_lote_d[:65]+str_mes+dia_menos+'20'+str_mes+str_dia+data_conf.cab_lote_d[75:]+'\n')
    
    # Inicializo los contadores para las listas
    linea622 = 0
    linea626 = 0
    linea_traceback622 = 0
    linea_traceback626 = 0
    mrdep = 0
    mrgir = 0
    indexdep = 0
    indexgir = 0
    int_t_num_id = randint(0,20000)
    tracenum626 = '00100340024'
    espacios799 = r'                                            '
    mrdep_line = 5
    
    # Escribo los 622     
    for line in range(len(listade622)):
        if int(listade622[linea622][43:51]) in lista_num_cheque_excel_dep:
            indexdep = lista_num_cheque_excel_dep.index(int(listade622[linea622][43:51]))
            mrdep = str(lista_mrdep_excel[indexdep])
            if len(mrdep) == 1:
                mrdep = "0" + mrdep
            outfile.write("622"+str(listade622[linea622])+str(mrdep)+"00        000"+str(traceback622[linea_traceback622])+'\n')
        if int(listade622[linea622][43:51]) not in lista_num_cheque_excel_dep:         
            mrdep = my_list[mrdep_line][4:6]
            outfile.write("622"+str(listade622[linea622])+str(mrdep)+"00        000"+str(traceback622[linea_traceback622])+'\n')
            mrdep_line+=2
        linea_traceback622+=1
        linea622+=1

    # Escribo los 626
    for line in range(len(listade626)): 
        
        str_t_num_id = str(int_t_num_id)
        
        if int(listade626[linea626][43:51]) in lista_num_cheque_excel_gir:
            indexgir = lista_num_cheque_excel_gir.index(int(listade626[linea626][43:51]))
            mrgir = str(lista_mrgir_excel[indexgir])
            if len(mrgir) == 1:
                mrgir = "0" + mrgir
                
            while (len(str(str_t_num_id))<7):
                str_t_num_id = '0'+str_t_num_id
            
            outfile.write("626"+str(listade626[linea626])+'            '+tracenum626+str_t_num_id+'\n')
            outfile.write("799R"+str(mrgir)+str(traceback626[linea_traceback626])+'      '+str(listade626[linea626][0:8])+espacios799+tracenum626[3:]+str_t_num_id+'\n')
            int_t_num_id = int_t_num_id+1
        linea626+=1
        linea_traceback626+=1
    
    outfile.write(data_conf.fin_lote_d+'\n')
    outfile.write(data_conf.fin_arch_d+'\n')
    outfile.close()        
    
    #----------------FIN DE LA GENERACION DEL ARCHIVO CR1dd352.191-------------------#
    
    # Reinicio listas
    listade622 = ['']
    listade626 = ['']
    traceback622 = ['']
    traceback626 = ['']
    
    # Pueblo las listas de datos 622 y 626 CRPmmdd1 y CRPmmdd3
    for i in range(0,2):
        # Abrir archivo de texto
        str_dia = str(int_dia)
        if len(str_dia) == 1:
            str_dia = "0" + str_dia
        
        str_mes = str(int_mes)
        if len(str_mes) == 1:
            str_mes = "0" + str_mes
        
        if (i==0): #622 CRPmmdd1
            str_archivo_entrada = data_conf.path + barra + 'CRP' + str_mes + str_dia +'1.191'
            #str_archivo_entrada = r"D:\Users\rvescobar\Documents\python\robot recibidas enviadas\script\CRP02071.191"
            #print(str_archivo_entrada)      
            
            try:
                with open(str_archivo_entrada, 'r') as infile:
                    data = infile.read()
                    my_list = data.splitlines()
            except Exception as err:
                print("Ocurrió un error al abrir archivo de entrada: ", err)
                sys.exit()
            
            
            for line in range(len(my_list)):
                if "622" in my_list[line][0:3]:
                    listade626.append(my_list[line][3:64])
                    traceback626.append(my_list[line][79:])
            listade626.remove('')
            traceback626.remove('')
        
        if (i==1): #626 CRPmmdd3
            str_archivo_entrada = data_conf.path + barra + 'CRP' + str_mes + str_dia + '3.191'
            #str_archivo_entrada = r"D:\Users\rvescobar\Documents\python\robot recibidas enviadas\script\CRP02073.191"
            #print(str_archivo_entrada)      
            
            try:
                with open(str_archivo_entrada, 'r') as infile:
                    data = infile.read()
                    my_list = data.splitlines()
            except Exception as err:
                print("Ocurrió un error al abrir archivo de entrada: ", err)
                sys.exit()
            
            for line in range(len(my_list)):
                if "626" in my_list[line][0:3]:
                    listade622.append(my_list[line+1][27:35]+my_list[line][11:64])
                if "799" in my_list[line][0:3]:
                    traceback622.append(my_list[line][6:21])
            listade622.remove('')
            traceback622.remove('')    
        
    ## Genero los archivos
    
    #----------------INICIO DE LA GENERACION DEL ARCHIVO CR0dd002.191----------------#
    
    # Creo el archivo de salida
    str_archivo_salida2 = data_conf.path + barra + 'CR0' + str_dia + "002.191"
    try:
        outfile = open(str_archivo_salida2, 'w')
    except Exception as err:
        print("Ocurrió un error al crear archivo: {}, {} "
              .format(str_archivo_salida2, err))
        sys.exit()
    
    dia_menos = str(int(int_dia)-1)
    if len(dia_menos)<2:
        dia_menos = '0'+dia_menos
    
    # Escribo los encabezados de lote y archivo con la fecha cambiada
    outfile.write(data_conf.cab_arch[:25]+str_mes+str_dia+data_conf.cab_arch[29:]+'\n')
    outfile.write(data_conf.cab_lote[:65]+str_mes+dia_menos+'20'+str_mes+str_dia+data_conf.cab_lote[75:]+'\n')
    
    # Inicializo los contadores para las listas
    linea622 = 0
    linea626 = 0
    linea_traceback622 = 0
    linea_traceback626 = 0
    mrdep = 0
    mrgir = 0
    indexdep = 0
    indexgir = 0
    int_t_num_id = randint(0,20000)
    tracenum626 = '00100720237'
    espacios799 = r'                                            '
    mrdep_line = 5
    
    # Escribo los 622     
    for line in range(len(listade622)):
        if int(listade622[linea622][43:51]) in lista_num_cheque_excel_dep:
            indexdep = lista_num_cheque_excel_dep.index(int(listade622[linea622][43:51]))
            mrdep = str(lista_mrdep_excel[indexdep])
            if len(mrdep) == 1:
                mrdep = "0" + mrdep
            outfile.write("622"+str(listade622[linea622])+str(mrdep)+"00        000"+str(traceback622[linea_traceback622])+'\n')
        if int(listade622[linea622][43:51]) not in lista_num_cheque_excel_dep:         
            mrdep = my_list[mrdep_line][4:6]
            outfile.write("622"+str(listade622[linea622])+str(mrdep)+"00        000"+str(traceback622[linea_traceback622])+'\n')
            mrdep_line+=2
        linea_traceback622+=1
        linea622+=1

    # Escribo los 626
    for line in range(len(listade626)): 
        
        str_t_num_id = str(int_t_num_id)
        
        if int(listade626[linea626][43:51]) in lista_num_cheque_excel_gir:
            indexgir = lista_num_cheque_excel_gir.index(int(listade626[linea626][43:51]))
            mrgir = str(lista_mrgir_excel[indexgir])
            if len(mrgir) == 1:
                mrgir = "0" + mrgir
                
            while (len(str(str_t_num_id))<7):
                str_t_num_id = '0'+str_t_num_id
            
            outfile.write("626"+str(listade626[linea626])+'            '+tracenum626+str_t_num_id+'\n')
            outfile.write("799R"+str(mrgir)+str(traceback626[linea_traceback626])+'      '+str(listade626[linea626][0:8])+espacios799+tracenum626[3:]+str_t_num_id+'\n')
            int_t_num_id = int_t_num_id+1
        linea626+=1
        linea_traceback626+=1
    
    outfile.write(data_conf.fin_lote+'\n')
    outfile.write(data_conf.fin_arch+'\n')
    outfile.close()
    
    #----------------FIN DE LA GENERACION DEL ARCHIVO CR0dd002.191-------------------#