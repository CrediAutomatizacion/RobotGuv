# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:49:09 2020

@author: rvescobar
"""

import pywinauto, time, pyperclip, logging
from Reemplazo import Configuracion

def subida_crecer(dir, str_mes, str_dia):
    
    data_conf = Configuracion()
    
    # Inicializa la configuracion del log
    logging.basicConfig(filename='error.log',level=logging.INFO)
    
    try:
        dir_path = dir
        
        from pywinauto.application import Application
        # Inicio un nuevo proceso especificandole la ruta
        
        app = Application(backend='uia').start(dir_path+r'\winscp429\WinSCP.exe', timeout=10)
        #app = Application(backend='uia').connect(path=r'D:\winscp429\WinSCP.exe')
        
        # Instanciado de ventana "Iniciar sesión"
        app_init_sesion = app.top_window()
        
        # Instanciado de botones de "Iniciar sesión"
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
        #app = Application().connect(path=dir_path+r'\winscp429\WinSCP.exe')
        app.top_window().wait('visible').maximize()
        
        # Tomo la ventana principal
        app_ventana_main = app.top_window()
        time.sleep(1)
        # Abro la ventana de abrir directorio
        pywinauto.mouse._perform_click_input(button='left', coords=(890,490))
        time.sleep(1)
        app_ventana_main.type_keys('^o')
        # Tomo la ventana de abrir directorio
        time.sleep(1)
        app_ventana_abrir = app.top_window()
        time.sleep(1)
        # Seteo la ruta
        app_ventana_abrir.Edit2.set_text(r'/opt/guv/coelsa/enviados')
        # Presiono boton ok
        time.sleep(1)
        app_ventana_abrir.OKButton.click()
        
        for i in range (0,5):
            
            # Activo la ventana
            if (i>0):
                app.top_window().wait('visible',14,2).set_focus()
                
            time.sleep(1)
            # Tomo la ventana principal y presiono nuevo archivo
            app.top_window().type_keys('+{F4}')
            time.sleep(1)
            
            # Tomo la ventana de nuevo archivo y la maximizo
            app_ventana_nuevo = app.top_window()
            time.sleep(1)
            # Identificadores de ventana nuevo archivo
            #app_ventana_nuevo.print_control_identifiers(filename=r'D:\nuevo.txt')
            
            # Seteo la ruta y presiono buscar
            if (i==0):
                text_file = open(data_conf.str_cr0,'r')
                string = data_conf.str_cr0
            if (i==1):
                text_file = open(data_conf.str_cr1,'r')
                string = data_conf.str_cr1
            if (i==2):
                text_file = open(data_conf.str_ch0,'r')
                string = data_conf.str_ch0
            if (i==3):
                text_file = open(data_conf.str_ch1,'r')
                string = data_conf.str_ch1
            if (i==4):
                text_file = open(data_conf.str_crn,'r')
                string = data_conf.str_crn
                
            time.sleep(1)
            #app_ventana_nuevo.Edit.set_text(r'robot.CRUV.BAT.INT.ACRED.GUV.CR.CRT2.DLNX')
            app_ventana_nuevo.Edit.set_text(string)
            time.sleep(1)
            app_ventana_nuevo.type_keys('{ENTER}')
            
            time.sleep(3)
            app_ventana_editor = Application().connect(title_re=r'/opt/guv/coelsa/enviados.*', class_name='TEditorForm')
            
            app_ventana_editor = app_ventana_editor.top_window()
            app_ventana_editor.maximize()
            
            time.sleep(1)
            pywinauto.mouse._perform_click_input(button='left', coords=(490,490))
            time.sleep(1)
            app_ventana_editor.type_keys('^a')
            time.sleep(1)
            app_ventana_editor.type_keys('{BACK}')
            
            #leemos el archivo
            line_list = text_file.read();
            time.sleep(1)
            #copiamos el contenido del archivo
            pyperclip.copy(line_list)
            time.sleep(1)
            app_ventana_editor.type_keys('^v')
            text_file.close() #don't forget to close the file
            
            time.sleep(1)
            app_ventana_editor.type_keys('{BACK}')
            time.sleep(1)
            app_ventana_editor.type_keys('^s')
            time.sleep(5)
            app_ventana_editor.close()
            time.sleep(1)
        
        #app = Application(backend='uia').connect(path=dir_path+r'\winscp429\WinSCP.exe')
        #time.sleep(1)
        app.top_window().set_focus()
        app.top_window().type_keys('+^d')
        time.sleep(1)
        app.top_window().close()
    #    app.top_window().set_focus()
    #    time.sleep(1)
    #    app.top_window().close()
    #    time.sleep(1)
    #    
    #    if app.window().child_window(title="Confirm", class_name="TMessageForm").exists():
    #            app_ventana_cerrar = app.window().child_window(title="Confirm", class_name="TMessageForm")
    #            time.sleep(1)
    #            app_ventana_cerrar.type_keys('{ENTER}')
    #            time.sleep(1)
        time.sleep(1)
        app.kill()
        print("Ha finalizado la ejecución. Presione enter para salir.")
        input()
    except Exception as e:
        logging.exception('Error occurred ' + str(e))
        print('Ha ocurrido un error. Presione enter para salir.')
        input()