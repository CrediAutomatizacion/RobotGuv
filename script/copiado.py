# -*- coding: utf-8 -*-
"""
Autor: Ricardo Vera Escobar

Este script automatiza la copia de los archivos ACREDITACION y ACREDITACIONRECHAZOS
"""
import pywinauto, time, os, logging, json, xlrd, pyperclip, time, random
from Reemplazo import dia_valido, mes_valido, Configuracion, generar, renombradoFecha
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
    
    #guardo el json con los datos actualizados
    data = {'FECHA': str_dia+'/'+str_mes+'/'+'20',
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
        
    print("No utilizar la computadora hasta que finalice el robot.")
    
    # Importo la clase Application de pywinauto
    from pywinauto.application import Application
    # Inicio un nuevo proceso especificandole la ruta
    app = Application(backend='uia').start(dir_path+r'\winscp429\WinSCP.exe', timeout=10)
    #app = Application(backend='uia').connect(path=r'D:\winscp429\WinSCP.exe')
    
    # Instanciado de ventana "Iniciar sesión"
    app_init_sesion = app.top_window()
    
    
    #app_init_sesion.print_control_identifiers(filename=r'D:\hola2.txt')
    #print(app_init_sesion.TreeView.print_items())
    
    # Instanciado de botones de "Iniciar sesión"
    #sitio_guv = app_init_sesion.TreeView.get_item(r'\Guv')
    boton_new = app_init_sesion.NewButton
    boton_login = app_init_sesion.LoginButton
    
    #Flujo "Iniciar sesión"
    boton_new.click()
    app_ventana_new = app.top_window()
    
    # Escribo los datos de config
    app_ventana_new.Edit5.set_text(r'10.6.17.88')
    app_ventana_new.Edit4.set_text(r'mbuv')
    app_ventana_new.Edit3.set_text(r'dGPZXy09')
    
    # Click en login
    boton_login.click()
    
    time.sleep(3)
    
    # Obtengo propiedades de ventana de autenticacion si existe y presiono continue
    aut_form_dict = app.top_window().get_properties()
    if aut_form_dict['class_name'] == r'TAuthenticateForm':
        app_autenticacion = app.top_window()
        boton_continue = app_autenticacion.ContinueButton
        boton_continue.click()
    
    # Maximizo la ventana
    app.top_window().maximize()
    
    app = Application().connect(path=dir_path+r'\winscp429\WinSCP.exe')
    
    # Tomo la ventana principal
    app_ventana_main = app.top_window()
    # Abro la ventana de abrir directorio
    #app_ventana_main.print_control_identifiers(filename=r'D:\hola3.txt')
    pywinauto.mouse._perform_click_input(button='left', coords=(890,490))
    time.sleep(0.7)
    app_ventana_main.type_keys('^o')
    # Tomo la ventana de abrir directorio
    time.sleep(1)
    app_ventana_abrir = app.top_window()
    time.sleep(0.7)
    # Seteo la ruta
    app_ventana_abrir.Edit2.set_text(r'/opt/guv/coelsa/enviados')
    #pyperclip.copy(r'/opt/guv/crecer/enviados')
    #pyperclip.paste()
    # Presiono boton ok
    time.sleep(0.7)
    app_ventana_abrir.OKButton.click()
    
    # Identificadores de ventana abrir
    #app.top_window().print_control_identifiers(filename='D:\hola3.txt')
    
    # For desde aca
    for i in range (0,5):
    
        if (i==1):
            app.top_window().set_focus()
            #    a = app.top_window()
        time.sleep(1)
        # Tomo la ventana principal y presiono buscar
        
        app.top_window().type_keys('%{F7}')
        time.sleep(1)
        # Tomo la ventana de busqueda y la maximizo
        app_ventana_buscar = app.top_window()
        app_ventana_buscar.maximize()
        # Identificadores de ventana buscar
        #app_ventana_buscar.print_control_identifiers(filename=r'D:\buscar.txt')
        
        # Seteo la ruta y presiono buscar
        # TODO: cambiar variables de documentos a descargar
        if (i==0): #CRDmmdd1
            time.sleep(1)
            app_ventana_buscar.Edit.set_text(r'CRD'+str_mes+str_dia+'1.191')
            time.sleep(1)
            app_ventana_buscar.type_keys('{TAB}')
            time.sleep(1)
            app_ventana_buscar.type_keys('{S}')
            #app_ventana_buscar.StartButton.click()
        if (i==1): #CRDmmdd3
            time.sleep(1)
            app_ventana_buscar.Edit.set_text(r'CRD'+str_mes+str_dia+'3.191')
            time.sleep(1)
            app_ventana_buscar.type_keys('{TAB}')
            time.sleep(1)
            app_ventana_buscar.type_keys('{S}')
            #app_ventana_buscar.StartButton.click()
        if (i==2): #CRPmmdd1
            time.sleep(1)
            app_ventana_buscar.Edit.set_text(r'CRP'+str_mes+str_dia+'1.191')
            time.sleep(1)
            app_ventana_buscar.type_keys('{TAB}')
            time.sleep(1)
            app_ventana_buscar.type_keys('{S}')
            #app_ventana_buscar.StartButton.click()
        if (i==3): #CRPmmdd3
            time.sleep(1)
            app_ventana_buscar.Edit.set_text(r'CRP'+str_mes+str_dia+'3.191')
            time.sleep(1)
            app_ventana_buscar.type_keys('{TAB}')
            time.sleep(1)
            app_ventana_buscar.type_keys('{S}')
            #app_ventana_buscar.StartButton.click()
        if (i==4): #CRPmmdd2
            time.sleep(1)
            app_ventana_buscar.Edit.set_text(r'CRP'+str_mes+str_dia+'2.191')
            time.sleep(1)
            app_ventana_buscar.type_keys('{TAB}')
            time.sleep(1)
            app_ventana_buscar.type_keys('{S}')
            #app_ventana_buscar.StartButton.click()
                
        
        # Hago click en medio de la ventana de busqueda y presiono abajo para seleccionar el item
        time.sleep(1)
        #pywinauto.mouse._set_cursor_pos((490,490))
        pywinauto.mouse._perform_click_input(button='left', coords=(490,490))
        time.sleep(1)
        pywinauto.keyboard.send_keys('{DOWN}')
        # Presiono focus para que muestre el item en la otra lista
        time.sleep(1)
        app_ventana_buscar.FocusButton.click()
        time.sleep(1)
        #app_ventana_buscar.ListItem.click_input(button='left', coord=(lista.ListItem.rectangle().left + 30,lista.ListItem.rectangle().top + 30))
        # Abro ventana de copiar
        app.top_window().set_focus()
        time.sleep(0.5)
        app_ventana_main = app.top_window()
        app_ventana_main.type_keys('{SPACE}')
        time.sleep(1)
        app_ventana_main.type_keys('{F5}')
        # Tomo la ventana de copiar
        time.sleep(1)
        app_ventana_copiar = app.top_window()
        # Seteo la ruta donde sera copiado el archivo
        app_ventana_copiar.Edit.set_text(dir_path+r'\*.*')
        time.sleep(1)    
        # Hago click en copiar
        app_ventana_copiar.type_keys('{ENTER}')
        time.sleep(1.5)
        # Si existe el archivo, reemplazar
        # Tomo la ventana de reemplazar
        app_ventana_reemplazar = app.top_window().get_properties()
        
        if app_ventana_reemplazar['class_name'] == r'TMessageForm':
            app_ventana_reemplazar = app.top_window()
            time.sleep(1)
            app_ventana_reemplazar.Button9.click()
            time.sleep(1)
        
    #reemplazo(str_dia, str_mes)
    
    time.sleep(1)
    app.top_window().set_focus()
    time.sleep(1)
    app.top_window().type_keys('+^d')
    time.sleep(1)
    #app.top_window().close()
    app.kill()
    #app = Application(backend='uia').connect(path=dir_path+r'\winscp429\WinSCP.exe')
    #time.sleep(1)
    #app.top_window().set_focus()
    #time.sleep(1)
    #app.top_window().close()
    #time.sleep(1)
    #
    #if app.window().child_window(title="Confirm", class_name="TMessageForm").exists():
    #        app_ventana_cerrar = app.window().child_window(title="Confirm", class_name="TMessageForm")
    #        app_ventana_cerrar.type_keys('{ENTER}')
    #        time.sleep(1)
    renombradoFecha(str_mes, str_dia, dir_path)
    time.sleep(1)
    generar(int(str_mes), int(str_dia))
    time.sleep(1)
    from subida import subida_crecer
    subida_crecer(dir_path, str_mes, str_dia)

except Exception as e:
    logging.exception(time.ctime() + str(e))
    print('Ha ocurrido un error. Presione enter para salir.')
    input()
    