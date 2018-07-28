.. _`Ajustes del servidor migasfree`:

==============================
Ajustes del servidor migasfree
==============================

 .. epigraph::

   No hay inteligencia allí donde no hay cambio ni necesidad de cambio.

   -- Herbert George Wells


Los ajustes de configuración del servidor migasfree se asignan en el
fichero ``/var/lib/migasfree/FQDN/conf/settings.py``.

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
el proyecto al ejecutar ``migasfree --update``.

Si no quieres que ningún ordenador registre proyectos y/o plataformas
automáticamente, tienes que darlas de alta manualmente y asignar este ajuste a
False.

Ejemplo:

  .. code-block:: none

    MIGASFREE_AUTOREGISTER = False


.. _`MIGASFREE_DEFAULT_COMPUTER_STATUS`:

MIGASFREE_DEFAULT_COMPUTER_STATUS
---------------------------------
Valor por defecto: 'intended'

Establece el estado por defecto que tendrá el ordenador cuando es añadido en el
sistema.

Los valores que se pueden asignar son: 'intended', 'reserved', 'unknown',
'in repair', 'available' o 'unsubscribed'

Ejemplo:

  .. code-block:: none

    MIGASFREE_DEFAULT_COMPUTER_STATUS = 'available' # Estado disponible por defecto


.. _`MIGASFREE_COMPUTER_SEARCH_FIELDS`:

MIGASFREE_COMPUTER_SEARCH_FIELDS
--------------------------------

Valor por defecto: ('id', 'name', )

Establece los campos del modelo ``Computer`` por los que se podrá buscar
un ordenador. El primer campo es importante ya que será el que aparezca
en la primera columna de  la lista de ordenadores. Si quieres ver el nombre
del ordenador en vez del ``id`` en la lista de ordenadores, asigna el campo
``name`` el primero de la lista.

Se utiliza también para las búsquedas de un ``CID`` por los campos especificados.
Ver :ref:`Fórmulas específicas`.

Ejemplo:

  .. code-block:: none

    MIGASFREE_COMPUTER_SEARCH_FIELDS = ("name", "ip_address") # Búsquedas por nombre e IP

MIGASFREE_TMP_DIR
-----------------

Valor por defecto: '/tmp'

Asigna la ruta donde se alamacenarán los ficheros temporales generados
por el servidor.

Ejemplo:

  .. code-block:: none

    MIGASFREE_TMP_DIR = "/tmp/server"

MIGASFREE_PUBLIC_DIR
--------------------

Valor por defecto: '/var/migasfree/repo'

Directorio donde se guardarán los paquetes y repositorios de físicos cada uno de los
proyectos.

Ejemplo:

  .. code-block:: none

    MIGASFREE_PUBLIC_DIR = "/var/repositories"


MIGASFREE_SECONDS_MESSAGE_ALERT
-------------------------------

Valor por defecto: 1800

Si un ordenador tarda más de los segundos especificados en este ajuste
en enviar un mensaje mientras se está actualizando, se considera que el
ordenador va retrasado (Delayed). Normalmente, esto ocurre cuando se ha perdido
la conexión con el servidor por cualquier circunstancia, por ejemplo cuando el
usuario ha apagado el equipo antes de que el cliente termine el proceso de
actualización. De esta forma, se queda registrado en el servidor como ``Delayed``.

.. only:: not latex

   .. figure:: graphics/chapter16/delayed.png
      :scale: 80
      :alt: Un equipo pasando a retrasado

      figura 16.1.  Un equipo pasando a retrasado.


.. only:: latex

   .. figure:: graphics/chapter16/delayed.png
      :scale: 80
      :alt:  Un equipo pasando a retrasado

      Un equipo pasando a retrasado.

Ejemplo:

  .. code-block:: none

    MIGASFREE_SECONDS_MESSAGE_ALERT = 3600 # Una hora

MIGASFREE_HELP_DESK
-------------------

Valor por defecto: 'Put here how you want to be found'

Texto que apacere al ejecutar el comando del cliente ``migasfree-label`` para
indicar al usuario cómo ponerse en contacto con Asistencia Técnica.

El comando ``migasfree-label`` tiene la finalidad de identificar inequívocamente
al cliente. Este comando ejecutado en un cliente con entorno gráfico abrirá el
navegador web mostrando una pequeña etiqueta que debe ser impresa y pegada en el
ordenador con objeto de facilitar la asistencia técnica aún estando el ordenador
apagado.

También es posible imprimir la etiqueta de un ordenador desde el servidor
desplegando el menú contextual del ordenador y pulsando en
``Etiqueta [ordenador]``.

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

Valor por defecto: []

Cuando se asigna un valor a este ajuste, apaceren nuevas acciones por cada
ordenador. El objetivo es poder ejecutar algún código desde nuestro equipo hacia
el equipo que se quiere administrar. Generalmente se usa para acceder por ``vnc`` o ``ssh``
a los ordenadores, pero puede ser utilizado con cualquier otro fin.

.. only:: not latex

   .. figure:: graphics/chapter16/remoteadminlink.png
      :scale: 50
      :alt: MIGASFREE_REMOTE_ADMIN_LINK

      figura 16.3. MIGASFREE_REMOTE_ADMIN_LINK


.. only:: latex

   .. figure:: graphics/chapter16/remoteadminlink.png
      :scale: 100
      :alt: MIGASFREE_REMOTE_ADMIN_LINK

      MIGASFREE_REMOTE_ADMIN_LINK


Las variables que se pueden usar dentro de este ajuste son:

    ``{{computer.<FIELD>}}`` para cualquier campo del modelo ``Computer``

    ``{{<<PROPERTYPREFIX>>}}`` cualquier propiedad del equipo cliente

Ejemplo vía ssh:

  .. code-block:: none

    MIGASFREE_REMOTE_ADMIN_LINK = ["ssh://root@{{computer.ip_address}}"]

Ejemplo vía https y puerto (este último definido como propiedad ``PRT``):

  .. code-block:: none

    MIGASFREE_REMOTE_ADMIN_LINK = ["https://myserver/?computer={{computer.name}}&port={{PRT}}"]

Pueden usarse varios protocolos:

  .. code-block:: none

    MIGASFREE_REMOTE_ADMIN_LINK = [
        "vnc://{{computer.ip_address}}",
        "checkping://{{computer.ip_address}}",
        "ssh://root@{{computer.ip_address}}",
    ]

Evidentemente, el navegador con el que se accede a la web del servidor debe saber
cómo interpretar dichos protocolos. Por ejemplo, si usas Firefox y quieres
permitir el protocolo ``vnc`` debes acceder a la dirección ``about:config`` y añadir:

  .. code-block:: none

    network.protocol-handler.expose.vnc false

Luego crea un fichero ejecutable para asociarlo al protocolo vnc para que lanze
``vinagre`` contra la IP del ordenador:

  .. code-block:: none

    #!/bin/bash
    URL=${1#vnc://}
    vinagre $URL


MIGASFREE_HW_PERIOD
-------------------

Valor por defecto: 30

Período en días para el envío del hardware de los ordenadores al
servidor. Si han pasado más días de los especificados, se envía de nuevo
toda la información del hardware al servidor.

Ejemplo:

  .. code-block:: none

    MIGASFREE_HW_PERIOD = 1 # Cada día

MIGASFREE_INVALID_UUID
----------------------

Valor por defecto =

  .. code-block:: none

     [
        "03000200-0400-0500-0006-000700080008", # ASROCK
        "00000000-0000-0000-0000-000000000000",
        "FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF",
        "00000000-0000-0000-0000-FFFFFFFFFFFF",
     ]

Es una lista con UUIDs inválidos.

Algunas placas base pueden no tener asignado un UUID único, pudiéndose darse
el caso que varios equipos tengan un mismo UUID. Esto provoca que en el servidor
se comparta el mismo registro de ``ordenador``.

Para evitarlo, es preciso añadir estos UUIDs en este ajuste.

Cuando un ordenador tiene un UUID inválido, el servidor toma y asigna el ``nombre
del ordenador`` como UUID.

Puedes hacer UUIDs inválidos añadiendo en ``/var/lib/migasfree/FQDN/conf/settings.py``
la siguiente instrucción:

  .. code-block:: none

    MIGASFREE_INVALID_UUID.extend( my_invalid_UUIDs )

donde ``my_invalid_UUIDs`` es una lista de UUIDs invalidos.

Ejemplo:

  .. code-block:: none

    MIGASFREE_INVALID_UUID.extend( ["00000000-FFFF-FFFF-FFFF-FFFFFFFFFFFF",] )

MIGASFREE_NOTIFY_NEW_COMPUTER
-----------------------------

Valor por defecto = False

Si se asigna a ``True``, el sistema añadirá una ``Notificación`` cuando un
cliente migasfree se registra en el servidor por primera vez.

MIGASFREE_NOTIFY_CHANGE_UUID
----------------------------

Valor por defecto = False

Si se establece a True se creará una ``Notificación`` cuando un equipo cambia
de UUID.

Esto puede ocurrir en contadas ocasiones y está relacionado con antiguos
clientes de migasfree, UUIDs inválidos, o con cambios de placa base en el
ordenador.

MIGASFREE_NOTIFY_CHANGE_NAME
----------------------------

Valor por defecto = False

Si se establece a True, se creará una ``Notificación`` cuando se detecta que un
ordenador ha cambiado de nombre.

Este ajuste puede resultar útil para detectar UUIDs no únicos.


MIGASFREE_NOTIFY_CHANGE_IP
--------------------------

Valor por defecto = False

Si se establece a True se creará una ``Notificación`` cuando un ordenador cambia
de ip.

Este ajuste puede resultar útil para detectar UUIDs no únicos.

   .. note::
       No actives este ajuste si tienes ordenadores con IP dinámica, ya que se
       crearán demasiadas notificaciones irrelevantes.


Ajustes de Django
=================

Los `ajustes de Django`__ también pueden ser modificados para
adaptar el funcionamiento del servidor añadiendo el ajuste en el fichero
``/var/lib/migasfree/FQDN/conf/settings.py``.

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

Otros ajustes importantes son los relacionados con la configuración
del email. Se emplean para enviar mensajes a los usuarios y asi poder
restablecer su contraseña. Tambien se usan para enviar a los
administradores notificaciones de errores vía email.

  .. code-block:: none

    EMAIL_USE_TLS = True
    EMAIL_HOST = 'webmail.example.com'
    EMAIL_PORT = 25
    EMAIL_HOST_USER = "myaccount@example.com"
    EMAIL_HOST_PASSWORD = "mypassword"
    DEFAULT_FROM_EMAIL = "migasfree-server <noreply@example.com>"

    ADMINS = [('John', 'john@example.com'), ('Mary', 'mary@example.com')]

