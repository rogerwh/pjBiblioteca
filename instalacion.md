## Paso 1: Ejegir carpeta para el proyecto y el entorno
## Paso 2: En la carpeta para el proyecto hacer git clone
    git clone https://github.com/miguelsantos-wh/pjBiblioteca.git
## Paso 3: Crear entorno en la carpeta para el entorno
    mkvirtualenv biblioteca -p=2.7
#### Confirmar que sea en python 2.7
    python -V
## Paso 4: Desactivar e iniciar entorno
#### Para desactivar podemos hacer:
    deactivate
#### Para iniciar podemos hacer
    workon biblioteca
#### o estando en la carpeta del entorno
    source bin/activate
## Paso 5: instalamos dependencias con el entorno iniciado
    pip install  -r requeriments.txt
## Paso 6: Crear base de datos
    sudo -u postgres createdb biblioteca
## Paso 7: Cambiar contraseña del usuario postgres (por defecto):
    sudo -u postgres psql template1
    ALTER USER postgres PASSWORD "newPassword"
#### para salir usar:
    \q
## Paso 8: Crear migraciones desde la carpeta del proyecto
    ./runserver makemigrations
## Paso 9: Hacer la migracion
    ./runserver migrate
## Paso 10: Iniciar el proyecto:
    ./manage.py runserver
## Paso 11: Para desactivar el proyecto:
    Ctrl+c
## Pasos opcionales si existe problema de decodificación
## Paso 1: Ir a la carpeta /usr/lib/python2.7/site.py
## Paso 2: Cambiar lo que hay en la Linea 493:
#### Linea 493: encoding = "ascii" cambiar a "utf-8"