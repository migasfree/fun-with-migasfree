.. _`Ajustes del cliente migasfree`:

==============================
Ajustes del cliente migasfree
==============================

 .. epigraph::

   Uno no debe adaptarse al cambio, sino crearlo.

   -- Jorge González Moore

Los ajustes de configuración del cliente migasfree se encuentran en el
fichero ``/etc/migasfree.conf``


Sección [client]
================

Server
------

Valor por defecto: localhost

Nombre del servidor migasfree contra el que se van a realizar las
actualizaciones.

Ejemplo:

  .. code-block:: none

    Server = 192.168.1.10

Project
-------

Valor por defecto: Se basa en la función de python ``platform.linux_distribution()``

Nombre del proyecto migasfree. Sería el equivalente al nombre que le quieras
dar a tu *distribución personalizada*. Es muy *recomendable* que configures este
ajuste, ya que para algunas distribuciones la función
``platform.linux_distribution()`` puede producir versiones diferentes
al aumentar de release (CentOS sería un ejemplo de esto).

Ejemplo:

  .. code-block:: none

    Project = MiDistro-1

Computer_Name
-------------

Valor por defecto: Se obtiene de la función de python ``platform.node()``

Nombre del ordenador que se mostrará en migasfree. Si por calquier circunstancia
se necesita que el nombre del ordenador no sea el ``hostname``, puedes configurar
este ajuste para modificarlo.

Ejemplo:

  .. code-block:: none

    Computer_Name = PC15403

Debug
-----

Valor por defecto: False

Si se establece a ``True``, la salida de los comandos del cliente mostrará
información útil para la depuración.

Ejemplo:

  .. code-block:: none

    Debug = True

GUI_Verbose
-----------

Valor por defecto: True

Indica si aparecen más o menos mensajes en el Intefaz Gráfico de
Usuario. Si se asigna a ``False``, sólo se mostrarán el primer y último
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
decida cuándo quiere realizarlas (siguiendo p.e. la configuración de un gestor de
actualizaciones tipo ``update-manager`` de Gnome figura 17.1 o ejecutando una
actualización desde el *front-end* del sistema de paquetería).

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


Manage_Devices
--------------

Valor por defecto: True

Especifica si en el ordenador se van a administrar impresoras a través del servidor
migasfree. Este ajuste está pensado, sobre todo, para aquellos equipos
(servidores p.e.) donde ni siguiera cups esté instalado.

Este ajuste está disponible a partir de la versión de cliente 4.17.

Ejemplo:

  .. code-block:: none

    Manage_Devices = False



SSL_Cert
--------

Valor por defecto: No establecido.

Ruta al fichero de certificado SSL de servidor en el cliente.

Si este fichero de certificado no existe se utilizará igualmente **https** para la
privacidad, pero la autenticación entre extremos no estará garantizada. En este
caso aparece en consola el siguiente mensaje:

  .. code-block:: none

    Certificate does not exist and authentication is not guaranteed

Ejemplo:

  .. code-block:: none

    SSL_Cert = /path/to/ssl/cert

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

Permite especificar la dirección de un sistema caché de repositorios
como podría ser ``apt-cacher``.

Ejemplo:

  .. code-block:: none

    Package_Proxy_Cache = 192.168.1.101:1234

Consulta el apartado ``Servicio de caché de paquetes`` del capítulo
:ref:`Migasfree en producción`.



Sección [packager]
==================

Esta sección se utiliza cuando se suben paquetes al servidor mediante
el comando ``migasfree-upload``. Se te pedirá la información que no hayas
especificado en estos ajustes.

User
----

Valor por defecto: No establecido.

Usuario con permisos para subir paquetes al servidor migasfree. Por
defecto, la base de dato del servidor ``migasfree`` incluye el usuario
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

Project
-------

Valor por defecto: No establecido.

Indica el nombre del proyecto migasfree al que se van a subir los paquetes.

Ejemplo:

  .. code-block:: none

    Project = AZLinux-12

Store
-----

Valor por defecto: No establecido.

Almacén en el servidor migasfree donde se guardarán los paquetes. Corresponde al
nombre de una carpeta en el servidor donde se situará el Paquete o Conjunto de Paquetes.
Puedes ver la lista de almacenes disponibles accediendo a ``Liberación - Almacenes``
en la web del servidor migasfree. Si asignas un Almacén que no existe se creará
automáticamente al subir el primer paquete.

Ejemplo:

  .. code-block:: none

    Store = Acme # Sitúa en /var/migasfree/repo/<Project>/STORES/Acme los paquetes.


Variables de entorno
====================

Mediante el uso de variables de entorno podemos modificar también la
configuración del cliente migasfree.

``MIGASFREE_CONF``

Por defecto, el fichero de configuración del cliente migasfree se encuentra en
``/etc/migasfree.conf`` pero mediante la variable de entorno ``MIGASFREE_CONF``
podemos indicar al cliente que use otro fichero. Esto puede serte útil si
tienes que subir paquetes mediante el comando``migasfree-upload`` a distintos
servidores migasfree desde la consola.

Ejemplo:

  .. code-block:: none

    export MIGASFREE_CONF='/etc/migasfree.conf.serverA'
    migasfree-upload -f <mipaquete>

Además, todos los ajustes del fichero de configuración del cliente migasfree también
pueden ser asignados mediante variables de entorno, siendo estas variables
prioritarias frente a los ajustes del fichero de configuración:

``MIGASFREE_CLIENT_SERVER``

``MIGASFREE_CLIENT_PROJECT``

``MIGASFREE_CLIENT_COMPUTER_NAME``

``MIGASFREE_CLIENT_DEBUG``

``MIGASFREE_CLIENT_GUI_VERBOSE``

``MIGASFREE_CLIENT_AUTO_UPDATE_PACKAGES``

``MIGASFREE_CLIENT_MANAGE_DEVICES``

``MIGASFREE_PROXY``

``MIGASFREE_CLIENT_PACKAGE_PROXY_CACHE``

``MIGASFREE_PACKAGER_USER``

``MIGASFREE_PACKAGER_PASSWORD``

``MIGASFREE_PACKAGER_PROJECT``

``MIGASFREE_PACKAGER_STORE``


Como ejemplo de uso de las variables de entorno, imagina un escenario en el cual
tienes un servidor migasfree y muchos centros en los que en cada uno de ellos
hay un servicio de caché de paquetes para minimizar el tráfico de Internet.
Para configurar cada equipo, deberías tener un paquete de configuración del
cliente migasfree por cada centro, pero si tienes muchos centros esto puede
resultar costoso. Una solución podría ser tener un sólo paquete de configuración del
cliente migasfree para todos los centros y, en la postinstalación del paquete,
crear las variables de entorno necesarias en función de la etiqueta del centro.

  .. code-block:: none

    # Codigo de ejemplo postinst acme-migasfree-client

    TAGS=`migasfree-tags -g`
    for CENTRO in $TAGS
    do
      if [ $CENTRO = "CTR-DELEGACION-BARCELONA" ]; then
        echo "MIGASFREE_CLIENT_PACKAGE_PROXY_CACHE='192.168.96.6:3142'" > /etc/profile.d/migasfree.sh
      fi
      if [ $CENTRO = "CTR-DELEGACION-MADRID" ]; then
        echo ""MIGASFREE_CLIENT_PACKAGE_PROXY_CACHE='192.168.80.4:3142'" > /etc/profile.d/migasfree.sh
      fi
    done
