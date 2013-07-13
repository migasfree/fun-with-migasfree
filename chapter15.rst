=======================
Resolución de problemas
=======================

 .. epigraph::

   Un problema deja de serlo si no tiene solución.

   -- Eduardo Mendoza

A menudo puede ocurrir que migasfree no esté funcionando como se espera. Para
obtener mas información y averiguar que te puede estar ocurriendo puedes poner
tanto al cliente como al servidor en modo ``DEBUG``.


Cliente en modo DEBUG
=====================

Simplemente debes poner el ajuste ``Debug`` a True en los
:ref:`Ajustes del cliente migasfree`

Cuando ejecutes ``migasfree --update`` en este modo desde una consola, verás en
la salida estándar más información de la habitual.

Tambien puede serte útil consultar la información que se va generando en
/etc/var/migasfree.log


Servidor en modo DEBUG
======================

Al estar el servidor realizado con Django, puedes usar el ajuste `DEBUG`__ a
``True``. Este ajuste del servidor debes ponerlo en el fichero
/etc/migasfree-server/settings.py y despues reiniciar el servidor web.

__ https://docs.djangoproject.com/en/dev/ref/settings/#debug

Al hacer esto, la página del servidor migasfree que te está fallando te
mostrará, en vez de una página de error escueta, otra página de error con
información muy extensa y que te permitirá ver que está ocurriendo.

  .. note::

    Nunca dejes el modo DEBUG en un entorno de producción por medida de
    seguridad.

