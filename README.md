# tiendaDjango
CRUD con Django, Zurb Foundation y MySQL

Instalación de Django en Windows:

Windows
Instalar el DBMS: PostgreSQL.
La mejor forma es seguir las instrucciones del sitio oficial para instalar PostgreSQL, disponible en: http://www.postgresql.org/download/windows/ 

Instalar Python y Django
Descargar Active Python, con este instalarás Python, pip y easy_install con un click.  Este es un archivo ejecutable para Windows que corresponde a un wizard típico para el mismo.  Disponible en: http://www.activestate.com/activepython/downloads 

Otra opción es: https://bitnami.com/stack/django

Creación del proyecto
Comencemos creando un proyecto llamado tienda.

django-admin startproject tienda

Veamos lo que creó startproject:

tienda/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py

Estos archivos son:

El directorio tienda/ de más afuera es sólo un contenedor para el proyecto. El nombre no afecta a Django; se puede renombrar libremente.
manage.py: Una utilidad de línea de comandos que permite interactuar con este proyecto Django de varias maneras. Se pueden leer todos los detalles sobre manage.py en /ref/django-admin.

El directorio tienda/ interno es el paquete Python para el proyecto que es utilizado de ejemplo en este proyecto. Su nombre, es el nombre de paquete Python que necesitará usar para importar cualquier cosa adentro del mismo (e.g. tienda.urls).

tienda/__init__.py: Un archivo vacío que le dice a Python que este directorio debe considerarse un paquete Python (puede leer más sobre paquetes en la documentación oficial de Python).

tienda/settings.py: Settings/configuración de este proyecto Django. /topics/settings describe cómo funcionan estos settings.

tienda/urls.py: Declaración de las URL de este proyecto Django; una “tabla de contenidos” del sitio Django. 

tienda/wsgi.py: Punto de entrada para servir el proyecto mediante servidores web compatibles con WSGI. Puede ver /howto/deployment/wsgi/index para más detalles.

Una vez creado el proyecto, desde la raíz del mismo crearemos dos app llamadas: proveedores y productos para almacenar toda la información de los proveedores y productos respectivamente.

python manage.py startapp productos
python manage.py startapp proveedores

A continuación, se instalan los siguientes requerimientos para el proyecto:

Pillow: librería para procesar imágenes, los formatos de las imágenes que se pueden procesar con pillow son los de uso más extendido (BMP, EPS, GIF, IM, JPEG, MSP, PCX, PNG, TIFF, PPM, WebP, ICO, PSD, PDF, entre otros).
pip install pillow

 

Argparse: se encarga de buscar los "flags" (ej --verbose, -v, -f, etc) y organizarlos de tal forma que se puede setiar si el argumento tiene que ser string o integrer y para luego crear un diccionario con los argumentos y sus variables.

pip install argparse

Distribute: para construir el paquete del proyecto, es un fork mantenido por la comunidad de un proyecto anterior, setuptools.

django-countries: lista de paises con django-countries

pip install django-countries

wsgiref: incluye funcionalidades para procesar variables.

pip install wsgiref

Agregar ‘productos’ y ‘proveedores’, además de algunas de las librerías instaladas en la variable INSTALLED_APPS dentro de tienda/settings.py:

django.contrib.admin – El sitio de administración. 
django.contrib.auth – Sistema de autenticación.
django.contrib.contenttypes – Un framework para tipos de contenido.
django.contrib.sessions – Un framework para manejo de sesiones.
django.contrib.messages – Un framework de mensajes.
django.contrib.staticfiles – Un framework para manejar los archivos estáticos.



