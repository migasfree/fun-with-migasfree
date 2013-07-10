.. _`Ajustes del cliente migasfree`:

==============================
Ajustes del cliente migasfree
==============================

Los ajustes de configuración del cliente migasfree se encuentran en el
fichero ``/etc/migasfree.conf``


Sección [client]
================

Server
------

Valor por defecto: localhost

Nombre del Servidor migasfree contra el que se van a realizar las
actualizaciones.

Ejemplo:

  .. code-block:: none

    Server = 192.168.1.10

Version
-------

Valor por defecto: Se basa en la función de python ``platform.linux_distribution()``

Nombre de la versión migasfree. Sería el equivalente al nombre que le quieras
dar a tu Distribución personalizada. Es muy *recomendable* que configures este
ajuste, ya que para algunas Distribuciones la función
``platform.linux_distribution()`` puede producir versiones diferentes
al aumentar de release (CentOS sería un ejemplo de esto).

Ejemplo:

  .. code-block:: none

    Version = MiDistro-1

Computer_Name
-------------

Valor por defecto: Se obtiene de la función de python ``platform.node()``

Nombre del ordenador que se mostrará en migasfree. Si por calquier circunstancia
se necesita que el nombre del ordenador no sea el ``hostname`` puedes configurar
este ajuste para modificarlo.

Ejemplo:

  .. code-block:: none

    Computer_Name = PC15403

Debug
-----

Valor por defecto: False

Si se establece a True, la salida de los comandos del cliente mostrará
información útil para la depuración.

Ejemplo:

  .. code-block:: none

    Debug = True

GUI_Verbose
-----------

Valor por defecto: True

Indica si aparecen más o menos mensajes en el Intefaz Gráfico de
Usuario. Si se asigna a False, sólo se mostrarán el primer y último
mensaje.

Ejemplo:

  .. code-block:: none

    GUI_Verbose = False


Auto_Update_Packages
--------------------

Valor por defecto: True

Determina si al ejecutar ``migasfree --update`` se instalan las nuevas
versiones de los paquetes ya instalados.

Si se establece este ajuste a **False** las actualizaciones de paquetes no se
producirán al ejecutar ``migasfree`` con objeto de que sea el usuario quien
decida cuándo quiere realizarlas ( siguiendo p.e. la configuración de un gestor de
actualizaciones tipo ``update-manager`` de Gnome figura 17.1 o ejecutando una
actualización desde el front-end del sistema de paquetería).

Este ajuste no afectará en ningún caso a los paquetes a instalar y/o a los
paquetes a desinstalar que hubiera definidos en los repositorios de migasfree.


.. only:: not latex

   .. figure:: graphics/chapter17/update-manager.png
      :scale: 80
      :alt: Configuración del Gestor de Actualizaciones.

      figura 17.1. Configuración del Gestor de Actualizaciones.


.. only:: latex

   .. figure:: graphics/chapter17/update-manager.png
      :scale: 80
      :alt: Configuración del Gestor de Actualizaciones.

      Configuración del Gestor de Actualizaciones.


Ejemplo:

  .. code-block:: none

    Auto_Update_Packages = False


SSL_Cert
--------

Valor por defecto: No establecido.

Ruta al fichero de certificado SSL de servidor en el cliente.

Si este fichero de certificado no existe se utilizará igualmente https para la
privacidad, pero la autenticación entre extremos no estará garantizada. En este
caso aparece en consola el siguiente mensaje:

  .. code-block:: none

    Certificate does not exist and authentication is not guaranteed

Ejemplo:

  .. code-block:: none

    SSL_Cert = "/path/to/ssl/cert"

Proxy
-----

Valor por defecto: No establecido.

Configuración del proxy.

Ejemplo:

  .. code-block:: none

    Proxy = 192.168.1.100:8080


Package_Proxy_Cache
-------------------

Valor por defecto: No establecido.

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

Valor por defecto: No establecido.

Usuario con permisos para subir paquetes al servidor migasfree. Por
defecto la base de dato del servidor ``migasfree`` incluye el usuario
``packager`` con los permisos adecuados para almacenar paquetes en el
servidor.

Ejemplo:

  .. code-block:: none

    User = packager

Password
--------

Valor por defecto: No establecido.

Contraseña del usuario.

Ejemplo:

  .. code-block:: none

    Password = packager

Version
-------

Valor por defecto: No establecido.

Indica el nombre de la versión migasfree a la que se van a subir los
paquetes.

Ejemplo:

  .. code-block:: none

    Version = AZLinux-12

Store
-----

Valor por defecto: No establecido.

Almacén en el servidor migasfree donde se guardarán los paquetes. Corresponde al
nombre de una carpeta en el servidor donde se situará el Paquete o Conjunto de Paquetes.
Puedes ver la lista de Almacenes disponibles accediendo a ``Liberación - Almacenes``
en la web del servidor migasfree. Si asignas un Almacén que no existe se creará
automáticamente al subir el primer paquete.

Ejemplo:

  .. code-block:: none

    Store = Acme # Sitúa en /var/migasfree/repo/<Version>/STORES/Acme los paquetes.
