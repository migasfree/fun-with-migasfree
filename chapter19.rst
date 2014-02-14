.. _`Empaquetando migasfree`:

======================
Empaquetando migasfree
======================

 .. epigraph::

   Nadie es como otro. Ni mejor ni peor. Es otro. Y si dos están de acuerdo, es
   por un malentendido

   -- Jean-Paul Sartre

El proceso consiste básicamente en bajarte el fuente del proyecto y
ejecutar el comando ``bin/create-package``

   .. note::
      Si quieres la versión de desarrollo puedes bajar ``master.zip`` en
      vez de ``latest.zip``

Creación del paquete migasfree-server (.deb)
=====================================================

Abre una terminal como root y baja el código fuente de migasfree:

  .. code-block:: none

    wget https://github.com/migasfree/migasfree/archive/latest.zip

Necesitaremos tener instalado unzip para descomprimir el fichero zip:

  .. code-block:: none

    apt-get install unzip

Descomprimimos el fichero latest.zip:

  .. code-block:: none

    unzip latest.zip
    rm latest.zip

Ahora tendrás una carpeta llamada migasfree-latest.

Creamos a continuacion el paquete migasfree-server. Para ello
necesitamos tener instalado el paquete python-stdeb:

  .. code-block:: none

    apt-get install python-stdeb

Nos situamos en la carpeta bin del proyecto y ejecutamos el script
create-package:

  .. code-block:: none

    cd migasfree-latest/bin
    ./create-package
    cd ../..

Ahora en la carpeta deb_dist tenemos el paquete deb que instalamos:

  .. code-block:: none

    dpkg -i migasfree-latest/deb_dist/migasfree-server_*_all.deb

Por problemas de dependencias seguramente se dejará sin configurar el
servidor de migasfree. Para instalar las dependencias que faltan
haremos:

  .. code-block:: none

    apt-get -f install


Creación del paquete migasfree-client (.deb)
=====================================================

Abre una terminal como root y baja el código fuente del cliente
migasfree:

  .. code-block:: none

    wget https://github.com/migasfree/migasfree-client/archive/latest.zip

Necesitaremos tener instalado unzip para descomprimir el fichero zip:

  .. code-block:: none

    apt-get install unzip

Descomprimimos el fichero latest.zip:

  .. code-block:: none

    unzip latest.zip
    rm latest.zip

Ahora tendrás una carpeta llamada migasfree-client-latest.

Creamos a continuación el paquete migasfree-client. Para ello
necesitamos tener instalado el paquete python-stdeb:

  .. code-block:: none

    apt-get install python-stdeb

Nos situamos en la carpeta bin del proyecto y ejecutamos el script
create-package:

  .. code-block:: none

    cd migasfree-client-latest/bin
    ./create-package
    cd ../..

Ahora en la carpeta deb_dist tenemos el paquete deb que instalamos:

  .. code-block:: none

    dpkg -i migasfree-client-latest/deb_dist/migasfree-client_*_all.deb

Por problemas de dependencias seguramente se dejará sin configurar el
cliente de migasfree. Para instalar las dependencias que faltan
haremos:

  .. code-block:: none

    apt-get -f install


Otras Distribuciones a las implementadas
========================================

Si al ejecutar ``./create-package`` te aparece:

  .. error::

     Computer distro is not available. Aborting package creation.

entonces, consigue el nombre de tu Distribución:

  .. code-block:: none

    _DISTRO=$(python -c "import platform; print platform.linux_distribution()[0].strip()")

y crea un nuevo fichero cuyo nombre sea ``$_DISTRO`` en el
directorio ``setup.cfg.d`` para paquetería rpm:

  .. code-block:: none

    touch ../setup.cfg.d/$_DISTRO #

ó en el directorio ``stdeb.cfg.d`` para paquetería deb:

  .. code-block:: none

    touch ../stdeb.cfg.d/$_DISTRO

Finalmente copia dentro de este fichero el contenido de otro fichero de
una Distribución similar y modifica las dependencias necesarias.

Una vez realizado este proceso vuelve a ejecutar ``./create-package``
