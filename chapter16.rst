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

.. _`MIGASFREE_ORGANIZATION`:

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



MIGASFREE_EXTERNAL_ACTIONS
--------------------------

Valor por defecto: {}

Este ajuste aparece por primera vez en la versión 4.16 del servidor y sustituye a 
``MIGASFREE_REMOTE_ADMIN_LINK``, el cual ha sido eliminado definitivamente en esta misma
versión.

El objetivo de este ajuste es ejecutar un código externo al servidor migasfree
sobre los elementos relacionados de un determinado objeto (un atributo, un ordenador,
un conjunto de atributos, etc).

Veamos un ejemplo de funcionamiento con esta configuración:

  .. code-block:: none

    MIGASFREE_EXTERNAL_ACTIONS = {
        "computer": {
            "ping": {"title": "PING", "description": "comprobar conectividad"},
            "ssh": {"title": "SSH", "description": "control remoto vía ssh"},
        },
        "deployment": {
            "check": {"title": "CHECK", "description": "comprobaciones al despliegue"},
        }
    }

Aquí estamos indicando que se añadan al modelo ``computador`` las acciones ``ping`` y ``ssh``.
Además, para el modelo ``deployment`` se ha definido una acción llamada ``check``.

El servidor simplemente se encarga de mostrar un botón cuando corresponda con el ``título`` 
de cada acción.


.. only:: not latex

   .. figure:: graphics/chapter16/mea.png
      :scale: 100
      :alt: MIGASFREE_EXTERNAL_ACTIONS

      figura 16.3. MIGASFREE_EXTERNAL_ACTIONS


.. only:: latex

   .. figure:: graphics/chapter16/mea.png
      :scale: 100
      :alt: MIGASFREE_EXTERNAL_ACTIONS

      MIGASFREE_EXTERNAL_ACTIONS


Cuando se pulsa sobre una acción determinada en el navegador web, el servidor simplemente
redigirá a una página con un protocolo que hemos denominado 
``Migasfree External Action`` (mea).


   .. note::

       Fijate ahora en la figura 16.3, estamos viendo los objetos relacionados con el conjunto de Atributos 
       ``AULA-3``. Observa que tiene 14 ordenadores relacionados a los que ahora puedes hacer ``PING`` 
       y ``SSH`` en bloque. Además este Conjunto de Atributos tambien está incluido en 7 Despliegues 
       a los que ahora puedes ejecutar una acción ``CHECK``.


 
Un ejemplo de redirección al pulsar sobre la acción ``ping`` (name: ping) desde el 
``atributo`` (model: atribute) cuyo ``id`` es 18745 (id: 18745) desde el servidor 
127.0.0.1 (server: 127.0.0.1) podría ser:

  .. code-block:: none

    mea://{"name": "ping", "related_model": "computer", "server": "127.0.0.1", "related_ids": [3643, 3635, 5499], "model": "attribute", "id": 18745}      

Observa en este ejemplo que el modelo relacionado con el ``atributo`` es el ``ordenador`` 
(related_model: computer) y los ordenadores concretos en este caso son tres 
(related_ids: [3643, 3635, 5499]).

Observa también que se hace uso del protocolo ``mea://``.

El navegador web (en tu propio equipo) es el encargado de interpetrar éste nuevo protocolo
y ejecutar un script con los datos que le llegan.  

Es necesario, por tanto, configurar adecuadamente el navegador para que reconozca el protocolo MEA.

Las posibilidades son muchas: 

    PING, SSH, VNC, WOL, etc.  sobre 1 o un grupo de ordenadores.

    Forzar la sincronización inmediata en ordenadores.

    Listados a tu gusto y necesidades.

    Interactuar con otras aplicaciones como p.e para abrir una incidencia en ``Redmine`` sobre una
    impresora (o sobre cualquier otro objeto de migasfree).

    etc, etc, y etc ...

    
Puedes ver un ejemplo de empaquetado de la configuración para Chromium y Firefox, así como de un
script que interpreta el protocolo mea:// en la carpeta ``acme-migasfree-exetrnal-actions`` de `fun-with-migasfree-examples`__.


__ https://github.com/migasfree/fun-with-migasfree-examples



Instrucciones para intalar el paquete acme-migasfree-external-actions:

  .. code-block:: none    

    $ wget https://github.com/migasfree/fun-with-migasfree-examples/archive/master.zip
    $ unzip master.zip
    $ cd fun-with-migasfree-examples-master/acme-migasfree-external-action
    $ debuild --no-tgz-check -us -uc
    $ sudo dpkg -i ../acme-migasfree-external-actions_*_all.deb


La configuracion del protocolo MEA para ``Firefox`` se encuentra en: ``usr/lib/firefox/defaults/pref/acme-migasfree-external-actions.js``

La configuracion del protocolo MEA para ``Chromium`` se encuentra en: ``usr/share/applications/acme-migasfree-external-actions.desktop``

El script que se ejecuta cuando pulsamos en una acción se encuentra en: ``usr/bin/acme-migasfree-external-actions``

Para obtener información de los ordenadores el paquete acme-migasfree-external-actions hace uso de `migasfree-sdk`__.

__ https://github.com/migasfree/migasfree-sdk


Puedes instalarlo mediante:

  .. code-block:: none    

    wget -O - http://migasfree.org/pub/install-sdk | bash



Para cada acción se puede especificar:

     ``title``: Título de la acción. Es obligatorio especificarlo.

     ``description``: "Tooltip" de la acción. Es opcional.

     ``many``: Por defecto su valor es ``True``. Si se establece a ``False``
     indica que el botón de la acción sólo se mostrará cuando el número de elementos sea 
     igual a 1. Si quieres que la acción ``VNC`` del ``ordenador`` sólo se muestre cuando 
     haya sólo un ordenador relacionado, establécelo como ``"many": False``. Es opcional.

     ``related``: Por defecto se muestra la acción para todos los modelos relacionados. 
     Si quieres que la acción solo se muestre sólo desde unos determinados modelos debes 
     especificarlos en una lista. Si quieres que la acción ``UPDATE`` del ``ordenador`` solo se 
     muestre desde ``ordenadores`` y ``despliegues``, pero no desde el resto de modelos relacionados,
     en ese caso establece ``"related": ["computer", "deployment"]``. Es opcional.


   .. note::

       La primera vez que ejecutes una acción se pedirá la contraseña del usuario
       ``reader``, empleado para acceder a la API de migasfree. Puedes cambiar ese usuario 
       modificando ``usr/bin/acme-migasfree-external-actions``

Ejemplo: 
     
  .. code-block:: none

    MIGASFREE_EXTERNAL_ACTIONS = {
        "computer": {
            "ping": {"title": "PING", "description": "comprobar conectividad"},
            "ssh": {"title": "SSH", "description": "control remoto vía ssh"},
            "vnc": {"title": "VNC", "description": "control remoto vía vnc", "many": False},
            "update": {"title": "UPDATE", "description": "Forzar sincronización", related: ['computer', 'deployment']},
        },
        "deployment": {
            "check": {"title": "CHECK", "description": "comprobaciones al despliegue"},
        }
    }


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


.. _`email`:

EMAIL
-----

Otros ajustes importantes son los relacionados con la configuración
del correo electrónico. Se emplean para enviar mensajes a los usuarios y así poder
restablecer su contraseña. También se usan para enviar a los
administradores notificaciones de errores al correo.

  .. code-block:: none

    EMAIL_USE_TLS = True
    EMAIL_HOST = 'webmail.example.com'
    EMAIL_PORT = 25
    EMAIL_HOST_USER = "myaccount@example.com"
    EMAIL_HOST_PASSWORD = "mypassword"
    DEFAULT_FROM_EMAIL = "migasfree-server <noreply@example.com>"

    ADMINS = [('John', 'john@example.com'), ('Mary', 'mary@example.com')]
