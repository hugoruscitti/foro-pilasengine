foro-pilasengine
================

Este repositorio contiene el código base para brindar
el foro de la comunidad pilas-engine.

Puedes ver este foro en funcionamiento en:

http://foro-pilasengine.com.ar


Pruebas locales
---------------

Si quieres probar el foro en tu propio equipo, ejecuta los siguientes
comandos. El foro está configurado inicialmente para funcionar usando
sqlite:

    mkvirtualenv foro-pilasengine
    pip install -r requirements.txt

    python manage.py syncdb --noinput --migrate
    python manage.py createsuperuser

    python manage.py runserver


Deploy en modo producción
-------------------------

Con el mismo entorno, si quieres mejorar el rendimiento del sistema puedes
usar gunicorn:

    pip install gunicorn
    pip install gunicorn-console

    gunicorn_django -b 0.0.0.0:9999 -D -n "foro-pilasengine.com.ar"
    gunicorn-console

y tendrías que crear un archivo *local_settings.py* con la configuración
de la base de datos de producción. Por ejemplo mysql:

    import os

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'foro_db_name',
            'USER': 'user_pepe',
            'PASSWORD': 'p134556',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
