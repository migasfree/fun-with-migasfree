.. _`Migasfree en producción`:

=======================
Migasfree en producción
=======================

 .. epigraph::

   El valor del producto se halla en la producción.

   -- Albert Einstein

Si te has decidido a instalar en producción el servidor migasfree debes cambiar
las contraseñas a los usuarios que vienen por defecto, y preparar un
backup de la base de datos y de la carpeta /var/migasfree.

Obtención de los paquetes de migasfree
--------------------------------------

Si en http://migasfree.org/repo/dists no están los paquetes de migasfree
para la Distribución que vas a emplear puedes generarlos tú mismo.

En :ref:`Empaquetando migasfree` tienes instrucciones de cómo obtenerlos.

Configuración del servidor
--------------------------

Crea el fichero ``/etc/migasfree-server/settings.py`` con el siguiente
contenido (no te olvides de sustituir la password por la del usuario
migasfree de Postgresql):

  .. code-block:: none

    MIGASFREE_ORGANIZATION="My Organization"
    DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.postgresql_psycopg2",
                "NAME": "migasfree",
                "USER": "migasfree",
                "PASSWORD": "mipassword",
                "HOST": "",
                "PORT": "",
           }
        }

Este es el fichero de configuración del servidor migasfree. Hay diversas
variables que se pueden configurar aquí para modificar el comportamiento
de migasfree.

Si necesitas cambiar la password del usuario migasfree en postgresql haz esto:

  .. code-block:: none

    # su postgres
    # psql
    # ALTER USER migasfree WITH PASSWORD 'mipassword';

.. note::

      Para una personalización más avanzada mira los
      :ref:`Ajustes del servidor migasfree`.


Cambiando las contraseñas
=========================

* Accede a ``Configuracion-Usuarios`` y verás los perfiles de
  usuarios.

* Edita el usuario ``admin``. Cámbiale la contraseña y guárdalo.

* Edíta el resto de perfiles de usuario y deshabilítalos o cámbiales la
  contraseña.

La explicación de los usuarios y sus grupos lo has visto ya en
:ref:`La configuración del sistema migasfree`


Servicio de caché de paquetes
-----------------------------

Montar un caché de paquetes para disminuir el tráfico de internet es habitual.
Su funcionamiento es muy sencillo. Cuando un equipo necesita descargar un
paquete de internet lo solicita al caché. Si el servicio de caché no lo tiene
ya almacenado lo descargará de internet, lo almacenará y se lo ofrecerá al
equipo. Si otro equipo necesita ese mismo paquete, como ya está en el caché
ya no se producirá tráfico internet sino que el servicio de caché lo ofrecerá
directamente al equipo.

.. only:: not latex

   .. figure:: graphics/chapter12/apt-cacher-ng.png
      :scale: 60
      :alt: Servicio de caché de paquetes.

.. only:: latex

   .. figure:: graphics/chapter12/apt-cacher-ng.png
      :scale: 60
      :alt: Servicio de caché de paquetes.


Puedes instalar el servicio de caché de paquetes en el equipo donde has
instalado el servidor migasfree, o en otro servidor.

Por ejemplo puedes instalar ``apt-cacher-ng``.

  .. code-block:: none

    # apt-get install apt-cacher-ng

Configura el usuario para la administración del servicio.

  .. code-block:: none

    # nano /etc/apt-cacher-ng/security.conf

Descomenta la línea que empieza por AdminAuth y modifica el usuario y la
contraseña:

  .. code-block:: none

    AdminAuth: <usuario>:<contraseña>

Reinicia el servicio.

  .. code-block:: none

    #service apt-cacher-ng restart

Por defecto el puerto del servicio apt-cacher-ng es el 3142. Accede a la
página http:<miservidor>:3142 para la administración del servicio de caché.

Hasta aquí hemos instalado y configurado el caché en el servidor.

Para la configuración de los clientes, debes crear el fichero
``/etc/apt/apt.conf.d/02proxy`` con el siguiente contenido:

  .. code-block:: none

    Acquire::http { Proxy "http://<miservidor>:3142"; };

Para hacerlo correctamente  modifica el paquete acme-migasfree-client
añadiéndo este fichero al paquete.

Otra manera de configurar los clientes es haciendo uso del ajuste
``Package_Proxy_Cache`` de los :ref:`Ajustes del cliente migasfree`. La
diferencia entre éste método y el anterior es que el primero hará uso del
servicio del caché de paquetes tanto cuando ejecutes el comando migasfree
en los clientes, como cuando ejecutes el gestor de paquetes (apt-get).
En cambio en el segundo método sólo usará el servicio de caché al ejecutar el
comando migasfree.

Puede consultar el `manual de apt-cacher-ng`__ para una configuración más
avanzada del servicio de caché.

__ http://www.unix-ag.uni-kl.de/~bloch/acng/html/index.html


Backups
-------

A continuación te sugiero un manera de hacer los backups.

Dump de la base de datos
========================

Para hacer el dump de la base de datos, crea el fichero
``/var/migasfree/dump/migasfree-dump.sh`` (deberás modificar
"mipassword" por la del usuario migasfree en posgresql):

  .. code-block:: none

    #!/bin/bash
    export PGPASSWORD=mipassword
    pg_dump migasfree -U migasfree > /var/migasfree/dump/migasfree.sql


Crea tambien el fichero ``/var/migasfree/dump/migasfree-restore.sh``
para el caso que tengas que restaurar un dump de la Base:

  .. code-block:: none

    #!/bin/bash

    if [ ! "$UID" = "0" ] ; then
      echo "debes ejecutar como root"
    fi

    /etc/init.d/apache2 stop

    echo "borrando BD..."
    echo "DROP DATABASE migasfree;" | su postgres -c psql -

    echo "creando BD migasfree..."
    su postgres -c "createdb -W -E utf8 -O migasfree migasfree" -

    echo "restore dump..."
    su postgres -c "psql -U migasfree -f /var/migasfree/dump/migasfree.sql" -

    /etc/init.d/apache2 start

Finalmente ponemos permisos de ejecución a los scripts:

  .. code-block:: none

    chmod 700 /var/migasfree/dump/migasfree-dump.sh
    chmod 700 /var/migasfree/dump/migasfree-restore.sh

Tarea periódica
===============

Para programar una tarea que se ejecute periódicamente realizando el
dump de la base de datos y la copia de los ficheros de los
repositorios, crea el fichero ``/var/migasfree/dump/migasfree-backup.sh``
con el siguiente contenido:

  .. code-block:: none

    # DUMP de la BD postgresql de migasfree
    /var/migasfree/dump/migasfree-dump.sh

    # BACKUP FICHEROS
    # (aqui se debe programar el backup de /var/migasfree con rsync p.e.)

Cámbiale los permisos:

  .. code-block:: none

    chmod 700 /var/migasfree/dump/migasfree-backup.sh

Edita como root crontab:

  .. code-block:: none

    crontab -e

y programa la tarea para que se ejecute diariamente a las 23:30 p.e.
añadiendo la siguiente línea a crontab:

  .. code-block:: none

    30 23 * * * /var/migasfree/dump/migasfree-backup.sh


Etiquetando los clientes
------------------------

Para facilitar la atención a los usuarios cuando tengan un problema, es
conveniente imprimir y pegar físicamente la etiqueta que identifica
inequívocamente a cada equipo ejecutando desde el cliente el comando:

  .. code-block:: none

    migasfree-label

Consulta el ajuste ``MIGASFREE_HELP_DESK`` de los :ref:`Ajustes del servidor migasfree`

  .. note::

    Tambien puedes imprimir la etiqueta desde otro equipo si conoces su UUID
    accediendo desde un explorador web a la siguiente dirección:

    http://<miservidormigasfree>/computer_label/?uuid=<UUID_DEL_ORDENADOR>
