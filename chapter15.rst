=======================
Resolución de problemas
=======================

 .. epigraph::

   Un problema deja de serlo si no tiene solución.

   -- Eduardo Mendoza

A menudo, puede ocurrir que migasfree no esté funcionando como se espera. Para
obtener más información y averiguar qué te puede estar ocurriendo, puedes poner
tanto al cliente como al servidor en modo ``DEBUG``.


Cliente en modo DEBUG
=====================

Simplemente debes poner el ajuste ``Debug`` a **True** en los
:ref:`Ajustes del cliente migasfree`.

Cuando ejecutes ``migasfree --update`` en este modo desde una consola, verás en
la salida estándar más información de la habitual.

También puede serte útil consultar la información que se va generando en
``/var/tmp/migasfree.log``.


Servidor en modo DEBUG
======================

Al estar el servidor realizado con Django, puedes usar el ajuste `DEBUG`__ a
``True``. Este ajuste del servidor debes ponerlo en el fichero
``/etc/migasfree-server/settings.py`` y después reiniciar el servidor web.

__ https://docs.djangoproject.com/en/dev/ref/settings/#debug

Al hacer esto, la página del servidor migasfree que te está fallando te
mostrará, en vez de una página de error escueta, otra página de error con
información muy extensa y que te permitirá ver qué está ocurriendo.

  .. note::

    Nunca dejes el modo DEBUG en un entorno de producción por seguridad.

Activar el sistema de logging en el servidor
============================================

El servidor utiliza el módulo de `logging`__ de Python.

__ https://docs.djangoproject.com/en/dev/topics/logging/

Para activar el sistema de logging en el servidor de migasfree añade el
ajuste `LOGGING`__ en /etc/migasfree-server/settings.py:

__ https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-LOGGING

  .. code-block:: none

    LOGGING = {
        'version': 1,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d
    %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': '/tmp/migasfree.log',
                'formatter': 'verbose',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'migasfree': {
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
            }
        }
    }

Esto hará que en el fichero indicado (/tmp/migasfree.log) se almacenen
los logs.
