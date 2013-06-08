==============================
Ajustes del cliente migasfree
==============================

Los ajustes de configuración del cliente migasfree se encuentran en el
fichero ``/etc/migasfree.conf``


Sección [client]
================

Server
------

Nombre del Servidor migasfree. El valor por defecto es localhost.

Ejemplo:

  .. code-block:: none

    Server = 192.168.1.10

Version
-------

Nombre de la versión migasfree. Equivale al nombre de tu Distribución
personalizada. El Valor por defecto se basa en la función de python
``platform.linux_distribution()``

Ejemplo:

  .. code-block:: none

    Version = MiDistro-1

Computer_Name
-------------

Nombre del ordenador que se mostrará en migasfree. El valor por defecto
se obtiene de la función de python ``platform.node()``

Ejemplo:

  .. code-block:: none

    Computer_Name = PC15403

Debug
-----

Si se establece a True, la salida de los comandos del cliente mostrarán
información útil para la depuración del cliente. El valor por defecto es
False.

Ejemplo:

  .. code-block:: none

    Debug = True

GUI_Verbose
-----------

Indica si aparecen más o menos mensajes en el Intefaz Gráfico de
Usuario. Si se asigna a False, sólo se mostrarán el primer y último
mensaje. El Valor por defecto es True.

Ejemplo:

  .. code-block:: none

    GUI_Verbose = False

SSL_Cert
--------

Ruta al fichero de certificado SSL en el cliente.

Ejemplo:

  .. code-block:: none

    SSL_Cert = "/path/to/ssl/cert"

Proxy
-----

Configuración del proxy.

Ejemplo:

  .. code-block:: none

    Proxy = 192.168.1.100:8080


Package_Proxy_Cache
-------------------

Permite especificar la dirección de un sistema cache de repositorios
como podría ser ``apt-cacher``.

Ejemplo:

  .. code-block:: none

    Package_Proxy_Cache = 192.168.1.101:1234

Sección [packager]
==================

Esta sección se utiliza cuando se suben paquetes al servidor mediante
el comando ``migasfree-upload``. Se te pedirá la información que no hayas
especificado en estos ajustes.

User
----

Usuario con permisos para subir paquetes al servidor migasfree. Por
defecto la base de dato del servidor ``migasfree`` inlcuye el usuario
``packager`` con los permisos adecuados para almacenar paquetes en el
servidor.

Ejemplo:

  .. code-block:: none

    User = packager

Password
--------

Contraseña del usuario.

Ejemplo:

  .. code-block:: none

    Password = packager

Version
-------

Indica el nombre de la versión migasfree a la que se va a subir los
paquetes.

Ejemplo:

  .. code-block:: none

    Version = AZLinux-12

Store
-----

Almacén en el servidor migasfree donde guardarán los paquetes.

Ejemplo:

  .. code-block:: none

    Store = Acme
