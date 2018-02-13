.. _`Migasfree en producción`:

=======================
Migasfree en producción
=======================

 .. epigraph::

   El valor del producto se halla en la producción.

   -- Albert Einstein

Si te has decidido a instalar en producción el servidor migasfree, asegúrate
de cambiar las contraseñas a los usuarios que vienen por defecto.

Desde la versión 4.14 del servidor migasfree usamos contenedores docker__.

Deberás disponer de una máquina con un S.O. linux de 64 bits sobre
la que vas a instalar docker y poder ejecutar los 2 contenedores necesarios,
uno es para la BD y el otro para la aplicación.

__ https://www.docker.com/


Instalación y configuracion del servidor
========================================

Sigue los pasos indicados en migasfree-docker__

__ https://github.com/migasfree/migasfree-docker


Configuración del servidor
==========================

Una vez en funcionamiento el servidor puedes configurar el servidor mediante
el fichero /var/lib/migasfree/FQDN/conf/settings.py

Hay diversas variables que se pueden configurar aquí para modificar el
comportamiento de migasfree. Para una personalización más avanzada, mira los
:ref:`Ajustes del servidor migasfree`.


Cambiando las contraseñas
-------------------------

* Accede a ``Configuracion-Usuarios`` y verás los perfiles de
  usuarios.

* Edita el usuario ``admin``. Cámbiale la contraseña y guárdalo.

* Edíta el resto de perfiles de usuario y deshabilítalos o cámbiales la
  contraseña.

La explicación de los usuarios y sus grupos lo has visto ya en
:ref:`La configuración del sistema migasfree`


Servicio de caché de paquetes
=============================

Montar un caché de paquetes para disminuir el tráfico de Internet es habitual.
Su funcionamiento es muy sencillo. Cuando un equipo necesita descargar un
paquete de Internet, lo solicita al caché. Si el servicio de caché no lo tiene
ya almacenado, lo descargará de Internet, lo almacenará y se lo ofrecerá al
equipo. Si otro equipo necesita ese mismo paquete, como ya está en la caché
ya no se producirá tráfico Internet, sino que el servicio de caché lo ofrecerá
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

Por defecto el puerto del servicio ``apt-cacher-ng`` es el **3142**. Accede a la
página http:<miservidor>:3142 para la administración del servicio de caché.

Hasta aquí hemos instalado y configurado el caché en el servidor.

Para la configuración de los clientes, debes crear el fichero
``/etc/apt/apt.conf.d/02proxy`` con el siguiente contenido:

  .. code-block:: none

    Acquire::http { Proxy "http://<miservidor>:3142"; };

Para hacerlo correctamente, modifica el paquete ``acme-migasfree-client``
añadiéndo este fichero al paquete.

Otra manera de configurar los clientes es haciendo uso del ajuste
``Package_Proxy_Cache`` de los :ref:`Ajustes del cliente migasfree`. La
diferencia entre éste método y el anterior es que el primero hará uso del
servicio del caché de paquetes tanto cuando ejecutes el comando migasfree
en los clientes, como cuando ejecutes el gestor de paquetes (apt-get).
En cambio, en el segundo método sólo usará el servicio de caché al ejecutar el
comando migasfree.

Puede consultar el `manual de apt-cacher-ng`__ para una configuración más
avanzada del servicio de caché.

__ http://www.unix-ag.uni-kl.de/~bloch/acng/html/index.html


Etiquetando los clientes
========================

Para facilitar la atención a los usuarios cuando tengan un problema, es
conveniente imprimir y pegar físicamente la etiqueta que identifica
inequívocamente a cada equipo, ejecutando desde el cliente el comando:

  .. code-block:: none

    migasfree-label

Consulta el ajuste ``MIGASFREE_HELP_DESK`` de los :ref:`Ajustes del servidor migasfree`

  .. note::

    También puedes imprimir la ``Etiqueta`` desplegando el menú del ordenador
    en el servidor.