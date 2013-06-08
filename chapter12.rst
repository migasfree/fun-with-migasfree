.. _`Migasfree en producción`:

=======================
Migasfree en producción
=======================

Si estás instalando en producción el servidor migasfree debes cambiar
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
de migasfree, pero ahora no es momento de explicarlas.

.. note::

      Para una personalización más avanzada mira los :ref:`Ajustes del servidor migasfree`.


Cambiando las contraseñas
=========================

* Accede a Configuracion-Usuarios-usuarios y verás los perfiles de
  usuarios.

* Edita el usuario admin. Cámbiale la contraseña y guárdalo.

* Edíta el resto de perfiles de usuario y deshabilítalos o cámbiales la
  contraseña.

La explicación de los usuarios y sus grupos la veremos más adelante en
:ref:`Usuarios migasfree`


Backups
=======

A continuación te sugiero un manera de hacer los backups.

Dump de la base de datos
------------------------

Para hacer el dump de la base de datos, crea el fichero
``/var/migasfree/dump/migasfree-dump.sh`` (deberás modificar
"mipassword" por la del usuario migasfree en posgresql):

  .. code-block:: bash

    #!/bin/bash
    export PGPASSWORD=mipassword
    pg_dump migasfree -U migasfree > /var/migasfree/dump/migasfree.sql


Crea tambien el fichero ``/var/migasfree/dump/migasfree-restore.sh``
para el caso que tengas que restaurar un dump de la Base:

  .. code-block:: bash

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

  .. code-block:: bash

    chmod 700 /var/migasfree/dump/migasfree-dump.sh
    chmod 700 /var/migasfree/dump/migasfree-restore.sh

Tarea periódica
---------------

Para programar una tarea que se ejecute periódicamente realizando el
dump de la base de datos y la copia de los ficheros de los
repositorios, crea el fichero ``/var/migasfree/dump/migasfree-backup.sh``
con el siguiente contenido:

  .. code-block:: bash

    # DUMP de la BD postgresql de migasfree
    /var/migasfree/dump/migasfree-dump.sh

    # BACKUP FICHEROS
    # (aqui se debe programar el backup de /var/migasfree con rsync p.e.)

Cámbiale los permisos:

  .. code-block:: bash

    chmod 700 /var/migasfree/dump/migasfree-backup.sh

Edita como root crontab:

  .. code-block:: bash

    crontab -e

y programa la tarea para que se ejecute diariamente a las 23:30 p.e.
añadiendo la siguiente línea a crontab:

  .. code-block:: bash

    30 23 * * * /var/migasfree/dump/migasfree-backup.sh


# TODO


Registro de Clientes
====================

  .. code-block:: bash

    migasfree -g


Etiquetando los clientes
========================

  .. code-block:: bash

    migasfree-label

