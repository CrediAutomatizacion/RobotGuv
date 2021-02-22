## ¿Qué hace 'robot.exe'?
Es un script python en forma de ejecutable que genera 5 archivos de texto necesarios para pasar numeros de cheques de girados a depositados y viceversa. 
A partir de archivos que están en un servidor remoto.
Los archivos que se generan se nombraran CH0dd072.191, CH1dd288.191, CR0dd002.191, CR1dd352.191 y CRNdd129.191. (dd corresponde a la fecha del día ingresado en la consola).
Se conecta por SCP al servidor, copia los archivos generados desde la web de Crecer, los modifica acorde y genera algunos nuevos que se copiaran al servidor nuevamente.
*¿Por qué se genera un archivo .exe?*
Para que lo puedan ejecutar las personas que trabajan para el banco sin instalar ningún paquete.

**IMPORTANTE:** Si ya tenés python instalado, verificar la versión con
		```bash
		python --version
		```
y pip debe estar en la version 20.2.4, chequear con 
		```bash
		pip --version
		```

1. Instalar [Python 3.7.4 32 bits](https://www.python.org/ftp/python/3.7.4/python-3.7.4.exe).

2. NO ACTUALIZAR pip, aunque así lo sugiera (porque causa problemas con el proxy de la máquina del banco).

3. Agregar el path de Python a las variables de entorno del sistema y de usuario, en PATH agregar {path}\Programs\Python\Python37-32 y {path}\Programs\Python\Python37-32\Scripts

4. Clonar el repositorio del proyecto guv en gitlab
	1. En caso de ser necesario generar SSH Key, usando el siguiente comando: 
		```bash
		ssh-keygen
		cat ~/.ssh/id_rsa.pub
		```
	2. Copiar el contenido de la clave ssh y agregarla en gitlab.


5. Una vez clonado el repositorio, abrir la terminal bash en la carpeta donde se encuentre el archivo requirements.txt y ejecutar el siguiente comando:
		```bash
		pip install -r requirements.txt
		```
   este comando instalará las dependencias necesarias para que el proyecto python robot guv funcione. NO ACTUALIZAR ninguno de estos paquetes.

6. Se puede ver y correr el proyecto desde IDLE (IDE por defecto de python) o se puede ver y editar desde cualquier editor de texto.
   Instalar Anaconda es opcional, con él se instala el IDE Spyder. Desde Anaconda se puede generar un environment con python 3.7, que sirve para poder correr el proyecto.
	1. Si se está trabajando en varios proyectos de python usar venv para instalar los paquetes necesarios en el virtual environment que el proyecto esté usando.

7. Una vez realizados los cambios necesarios, se debe volver a generar el archivo .exe, el cual se ejecuta para poder modificar los archivos del servidor remoto.
   Se ejecutará el siguiente comando desde la carpeta del proyecto:
		```bash
		pyinstaller --onefile copiado.py
		```
   Como este archivo se crea a partir de 'copiado.py', va a tener el nombre 'copiado.exe' (se alamacena dentro de las carpeta '/dist'), se debe cambiar a 'robot.exe'

8. Copiar la nueva "versión" en la carpeta compartida '\\sfs-1\Testing\Tareas en curso\GUV\Documentacion\robot guv' (reemplazar el existente)

### Cosas a mejorar:
- En el futuro, se podría reemplazar el excel por otro tipo de archivo.
- Usar archivos de configuración para generar los archivos necesarios.
