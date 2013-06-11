.. _`Ajustes del servidor migasfree`:

==============================
Ajustes del servidor migasfree
==============================

Los ajustes de configuración del servidor migasfree se encuentran en el
fichero ``/etc/migasfree-server/settings.py``.

   .. note::
      Este es un fichero ``python``, por lo que hay que llevar cuidado con
      la sintaxis y la indentación.

Ajustes propios de migasfree
============================

MIGASFREE_ORGANIZATION
----------------------

Valor por defecto: 'My Organization'

Establece el nombre de tu organización.

Ejemplo:

  .. code-block:: none

    MIGASFREE_ORGANIZATION = "ACME Corporation"

MIGASFREE_AUTOREGISTER
----------------------

Valor por defecto:  True

Especifica si los ordenadores pueden autoregistrar la plataforma y
la version migasfree.

Si no quieres que ningún ordenador registre versiones y/o plataformas
automáticamente, tienes que darlas de alta manualmente y asignar este ajuste a
False.

Ejemplo:

  .. code-block:: none

    MIGASFREE_AUTOREGISTER = False


MIGASFREE_COMPUTER_SEARCH_FIELDS
--------------------------------

Valor por defecto: ('id', 'name', )

Establece los campos del modelo ``Computer`` por los que se podrá buscar
un ordenador. El primer campo es importante ya que será el que aparezca
en la primera columna de  la lista de ordenadores. Si quieres ver el nombre
del ordenador en vez del id en la lista de ordenadores asigna el campo
``name`` el primero de la lista.

Ejemplo:

  .. code-block:: none

    MIGASFREE_COMPUTER_SEARCH_FIELDS = ("name", )

MIGASFREE_TMP_DIR
-----------------

Valor por defecto: '/tmp'

Asigna la ruta donde se alamacenarán los ficheros temporales generados
por el servidor.

Ejemplo:

  .. code-block:: none

    MIGASFREE_TMP_DIR = "/tmp/server"

MIGASFREE_SECONDS_MESSAGE_ALERT
-------------------------------

Valor por defecto: 1800

Si un ordenador tarda mas de los segundos especificados en este ajuste
en enviar un mensaje mientras se está actualizando, se considera que el
ordenador va retrasado (Delayed). Normalmente esto ocurre cuando se ha perdido
la conexión con el servidor por cualquier circunstancia, por ejemplo cuando el
usuario ha apagado el equipo antes de que el cliente termine el proceso de
actualización. De esta forma se queda registrado en el servidor como ``Delayed``.

.. only:: not latex

   .. figure:: graphics/chapter16/delayed.png
      :scale: 100
      :alt: MIGASFREE_SECONDS_MESSAGE_ALERT

      figura 16.3. MIGASFREE_SECONDS_MESSAGE_ALERT


.. only:: latex

   .. figure:: graphics/chapter16/delayed.png
      :scale: 80
      :alt: MIGASFREE_SECONDS_MESSAGE_ALERT

      MIGASFREE_SECONDS_MESSAGE_ALERT

Ejemplo:

  .. code-block:: none

    MIGASFREE_SECONDS_MESSAGE_ALERT = 3600 # Una hora

MIGASFREE_HELP_DESK
-------------------

Valor por defecto: 'Put here how you want to be found'

Texto que apacere al ejecutar el comando del cliente``migasfree-label``
para indicar al usuario como ponerse en contacto con Asistencia
Técnica.

El comando ``migasfree-label`` tiene la finalidad de identificar inequívocamente
al cliente. Este comando ejecutado en un cliente con entorno gráfico abrirá el
navegador web mostrando una pequeña etiqueta que debe ser impresa y pegada en el
ordenador con objeto de facilitar la asistencia técnica aún estando el ordenador
apagado.


.. only:: not latex

   .. figure:: graphics/chapter16/helpdesk.png
      :scale: 100
      :alt: Comando migasfree-label

      figura 16.2. Comando migasfree-label.


.. only:: latex

   .. figure:: graphics/chapter16/helpdesk.png
      :scale: 50
      :alt: Comando migasfree-label.

      Comando migasfree-label.

Ejemplo:

  .. code-block:: none

    MIGASFREE_HELP_DESK = "Teléfono Asistencia Técnica: 555.12.34.56"

MIGASFREE_REMOTE_ADMIN_LINK
---------------------------

Valor por defecto: ''

Cuando se asigna un valor a este ajuste, apacere un icono a la izquierda
del ordenador en las páginas web del servidor para permitir acceder al
ordenador remotamente con un simple click.

.. only:: not latex

   .. figure:: graphics/chapter16/remoteadminlink.png
      :scale: 100
      :alt: MIGASFREE_REMOTE_ADMIN_LINK

      figura 16.3. MIGASFREE_REMOTE_ADMIN_LINK


.. only:: latex

   .. figure:: graphics/chapter16/remoteadminlink.png
      :scale: 50
      :alt: MIGASFREE_REMOTE_ADMIN_LINK

      MIGASFREE_REMOTE_ADMIN_LINK


Las variables que se pueden usar dentro de este ajuste son:

    ``{{computer.<FIELD>}}`` para cualquier campo del modelo ``Computer``

    ``{{<<PROPERTYPREFIX>>}}`` cualquier propiedad del equipo cliente

Ejemplo vía ssh usando el complemento ``fireSSH`` para ``Firefox``:

  .. code-block:: none

    MIGASFREE_REMOTE_ADMIN_LINK = "ssh://root@{{computer.ip}}"

Ejemplo via https y puerto:

  .. code-block:: none

    MIGASFREE_REMOTE_ADMIN_LINK = "https://myserver/?computer={{computer.name}}&port={{PRT}}"

MIGASFREE_HW_PERIOD
-------------------

Valor por defecto: 30

Periodo en días para el envío del hardware de los ordenadores al
servidor. Si han pasado más días de los especificados se envia de nuevo
toda la información del harware al servidor.

Ejemplo:

  .. code-block:: none

    MIGASFREE_HW_PERIOD = 1 # Cada día

Ajustes de Django
=================

Los `ajustes de Django`__ tambien pueden ser modificados para
adaptar el funcionamiento del servidor añadiendo el ajuste en el fichero
``/etc/migasfree-server/settings.py``.

__ https://docs.djangoproject.com/en/dev/ref/settings/

El más importante de este tipo de ajustes es:

DATABASES
---------

Valor por defecto:

  .. code-block:: none

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'migasfree',
            'USER': 'migasfree',
            'PASSWORD': 'migasfree',
            'HOST': '',
            'PORT': '',
        }
    }





