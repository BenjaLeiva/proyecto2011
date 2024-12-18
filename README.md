# proyecto2011

Proyecto Django: Sistema de Ejercicios y Rutinas
Este proyecto es una aplicación web creada con Django que permite gestionar rutinas de ejercicios, usuarios y ejercicios en sí mismos. Los usuarios pueden agregar, editar y eliminar rutinas, ejercicios y perfiles de usuarios. Esta aplicación es ideal para gestionar un plan de entrenamiento físico.

Requisitos
Antes de comenzar, asegúrate de tener instalado lo siguiente:

Python/django

de no tener django instalado utilice el comando pip install django

Configuración inicial

1. Crear un entorno virtual
Un entorno virtual es una herramienta que ayuda a mantener las dependencias del proyecto aisladas
Para crear y activar el entorno virtual:

En la terminal, navega a la carpeta de tu proyecto (en mi caso "C:\Users\acer\Desktop\proyectos" donde aloje tanto el proyecto como el entorno virtual)

Ejecuta el siguiente comando para crear el entorno virtual:
python -m venv venv

Activa el entorno virtual
venv\Scripts\activate

2. Instalar las dependencias
Una vez activado el entorno virtual, instala las dependencias necesarias el proyecto.
pip install django djangorestframework

3. Configurar el proyecto
Clona o descarga este repositorio en tu máquina
Una vez descargado, accede a la carpeta de tu proyecto desde la terminal
Ejecuta el siguiente comando para aplicar las migraciones de la base de datos:

python manage.py makemigrations
python manage.py migrate
Esto creará las tablas necesarias en la base de datos.

4. Ejecutar el servidor de desarrollo
Una vez configurado el entorno y aplicadas las migraciones, puedes ejecutar el servidor de desarrollo de Django con el siguiente comando:

python manage.py runserver
Esto iniciará un servidor local en http://127.0.0.1:8000/.

5. Acceder a la aplicación
Abre un navegador web y dirígete a:
http://127.0.0.1:8000/

Esto te llevará a la página de inicio del proyecto, donde podrás navegar entre las diferentes funcionalidades:

Ejercicios: Ver, agregar, editar y eliminar ejercicios.
Rutinas: Ver, agregar, editar y eliminar rutinas.
Usuarios: Ver, agregar, editar y eliminar usuarios.
Estructura del Proyecto
La estructura de archivos del proyecto es la siguiente:

proyecto2011/
├── gitapp/                       # Aplicación principal
│   ├── migrations/               # Migraciones de la base de datos
│   ├── static/                   # Archivos estáticos como CSS
│   ├── templates/                # Plantillas HTML
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── views.py                  # Vistas para la API y frontend
│   ├── urls.py                   # Rutas de la app
│   ├── serializers.py            # Serializadores
│   └── models.py                 # Modelos de la base de datos
├── proyecto2011/                 # Archivos del proyecto Django
│   ├── settings.py               # Configuración del proyecto
│   ├── urls.py                   # Rutas principales
│   ├── wsgi.py                   # Configuración para el servidor
│   ├── asgi.py                   # Configuración para WebSockets
│   └── manage.py                 # Script para administrar el proyecto
└── README.md                     # Este archivo

6. Uso de la Aplicación
La aplicación tiene funcionalidades CRUD (Crear, Leer, Actualizar, Eliminar) para los siguientes modelos:

Ejercicios: Se pueden agregar, editar y eliminar ejercicios, que son actividades físicas que los usuarios pueden realizar.

Rutinas: Puedes crear rutinas que contienen una lista de ejercicios. Cada rutina tiene un nombre, duración y una lista de ejercicios asociados.

Usuarios: Los usuarios pueden tener un perfil con su nombre, nivel de condición física y las rutinas que han completado.

Los formularios para agregar, editar y eliminar elementos son accesibles desde las páginas correspondientes de la aplicación.

7. Personalización
Puedes personalizar la aplicación cambiando los siguientes archivos:

Modelos (models.py): Si deseas agregar más campos o funcionalidades a los modelos.
Vistas (views.py): Si deseas modificar la lógica de las vistas.
Plantillas HTML (templates/): Si deseas cambiar la apariencia de la interfaz de usuario.
Estilos CSS (static/): Para personalizar el diseño de la página web.

link del repositorio
<!--https://github.com/BenjaLeiva/proyecto2011.git-->