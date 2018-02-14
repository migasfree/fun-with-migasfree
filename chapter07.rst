.. _`Configurando migasfree-client`:

=============================
Configurando migasfree-client
=============================

 .. epigraph::

   La libertad no es poder elegir entre unas pocas opciones impuestas,
   sino tener el control de tu propia vida. La libertad no es elegir
   quien será tu amo, es no tener amo.

   -- Richard Stallman.

En el capítulo anterior nos hemos centrado en cómo se realiza el proceso
de la GCS.

En este capítulo vas a *configurar el cliente de migasfree* (mediante empaquetado)
para que se conecte al servidor migasfree que ya debes tener funcionando.

Todos los comandos de este capítulo los vas a ejecutar en otra máquina virtual,
con Ubuntu instalado, y que debes tener en la misma red en la que esté la máquina
virtual del servidor.

El objetivo de este capítulo es que conozcas un poco más el empaquetado.

Instalando migasfree-client en Ubuntu
=====================================

Instala el cliente migasfree:

  .. code-block:: none

     # wget -O - http://migasfree.org/pub/install-client | bash

Observa como en el fichero ``/etc/migasfree.conf`` que ha instalado el paquete
``migasfree-client`` no hay, lógicamente, ningún ajuste configurado.

  .. code-block:: none

    less /etc/migasfree.conf

A continuación, vamos a configurar este fichero haciendo uso del empaquetado,
así que no lo hagas manualmente.


Obteniendo acme-migasfree-client
================================

Al igual que hiciste con ``acme-test-files``, puedes bajarte
el fuente del paquete que vamos a utilizar de plantilla para configurar el
cliente de migasfree.

En la nueva máquina virtual con Ubuntu, ejecuta el siguiente código si aún
no te has descargado ``fun-with-migasfree-examples``:

  .. code-block:: none

    $ wget https://github.com/migasfree/fun-with-migasfree-examples/archive/master.zip
    $ unzip master.zip
    $ cd fun-with-migasfree-examples-master

Adaptando acme-migasfree-client
===============================

Accede al directorio acme-migasfree-client y observa su contenido:

  .. code-block:: none

    $ cd  acme-migasfree-client
    $ ls -la
    total 20
    drwxrwxr-x 5 alberto alberto 4096 jun 18 20:54 .
    drwxrwxr-x 4 alberto alberto 4096 jun 18 21:04 ..
    drwxrwxr-x 3 alberto alberto 4096 jun 18 20:54 debian
    drwxrwxr-x 3 alberto alberto 4096 jun 18 20:54 usr


Metadatos
---------

Observa el directorio ``debian``. Este directorio es el que contiene
los metadatos del paquete. Los ficheros más importantes en este
directorio son:

* El fichero ``control`` consiste en un conjunto de campos, representados
  en un formato común, que permiten al sistema de gestión de paquetes
  conocer los metadatos del paquete y así poder gestionarlo adecuadamente.
  Puedes consultar la `debian-policy`__ para explorar el conjunto de
  ``datos de control``

__ http://www.debian.org/doc/debian-policy/ch-controlfields.html

* El fichero ``changelog`` contiene información, en un formato especial,
  con las modificaciones que se han realizado en cada versión del paquete.
  Cada vez que se modifica el paquete, hay que añadir una entrada en este
  fichero, incrementando la versión y registrando lo que se ha modificado.

* El fichero ``copyright`` contiene la información sobre los recursos,
  licencia y derechos de autoría de las fuentes originales del paquete.

* El fichero ``rules`` contiene las reglas que se utilizan para generar
  los paquetes a partir de sus fuentes.

* El fichero ``install`` contiene una lista de ficheros que serán
  instalados con el paquete.

Ahora que conoces el significado de estos ficheros, modifícalos cambiando
el nombre del paquete ``acme-migasfree-client`` por ``tuempresa-migasfree-client``
y pon tu nombre y la fecha actual allí donde se requiera.

Modifica también el nombre del directorio raiz ``acme-migasfree-client``
por ``tuempresa-migasfree-client``.

Scripts
-------

Observa ahora los scripts ``postinst`` y ``prerm``. Sus nombres nos indican
cuando serán ejecutados por el sistema de gestión de paquetes.

* ``postinst`` inmediatamente después de que se produzca la instalación
  del paquete.

* ``prerm`` justo antes de que se produzca la eliminación del paquete.

Observa ahora el contenido de ``postinst`` y verás que aquí se hace
una llamada al comando ``dpkg-divert``. Mediante este comando hacemos lo
que se conoce como una desviación de fichero (divert). Mediante la
desviación, indicamos al sistema de gestión de paquetes que un fichero ya
no pertenece a un determinado paquete sino al que nosotros establezcamos.

Así, el fichero de configuración ``/etc/migasfree.conf``, que pertenece en
principio al paquete migasfree-client, hacemos que pertenezca al paquete
``tuempresa-migasfree-client`` de tal manera que, una posible
actualización de ``migasfree-client`` ya no nos afectará. Cada vez que
queramos modificar un ajuste del cliente migasfree en ``/etc/migasfree.conf``,
lo haremos a través del fichero ``usr/share/divert/etc/migasfree.conf``
del paquete ``tuempresa-migasfree-client``.

Fíjate también que en ``prerm`` deshacemos esta desviación, para que
si desinstalamos el paquete, quede todo como estaba.

Modifica ahora el fichero ``usr/share/divert/etc/migasfree.conf``. Tendŕas que
poner el ajuste ``Server`` con el nombre, o la IP, del servidor migasfree que
hemos utilizado anteriormente, y el ajuste ``Project`` con el nombre de tu
distribución, por ejemplo ``ACME-1``. El resto de ajustes, modifícalos según tus
intereses. Una vez hecho esto, y situado en el directorio
``tuempresa-migasfree-client``, genera el paquete (debes tener el
paquete ``devscripts`` y ``debhelper`` previamente instalados).

  .. code-block:: none

    $ /usr/bin/debuild --no-tgz-check -us -uc

Con esto tendrás un paquete que configura el cliente migasfree para tu
organización. Ahora es momento de instalarlo:

  .. code-block:: none

    # dpkg -i tuempresa-migasfree-client_1.0-1_all.deb

Observa que al instalar el paquete, ``dpkg`` te informa que se añade la desviación
de ``/etc/migasfree.conf``. Comprueba ahora que el ajuste ``Server`` y ``Project``
son los correctos.

  .. code-block:: none

    # less /etc/migasfree.conf


Ahora ya estás preparado para registrar este ordenador en el servidor migasfree.

  .. code-block:: none

    # migasfree -u

Comprueba que en el servidor se ha creado la version ``ACME-1`` y que
existe un nuevo ordenador accediendo a la página web del servidor.

Finalmente, subimos el paquete a nuestro servidor migasfree con el fin de tenerlo
disponible para su liberación a otros escritorios ``ACME-1``.

  .. code-block:: none

    # migasfree-upload -f tuempresa-migasfree-client_1.0-1_all.deb

* Introduce usuario: admin

* Contraseña: admin

* Proyecto: ACME-1

* Almacén: acme


Ejecución del cliente migasfree
===============================

Hasta ahora, siempre hemos ejecutado el cliente migasfree desde consola
mediante el comando ``migasfree -u`` como ``root``. Ahora vamos a hacer
que se ejecute automáticamente cada vez que el usuario abra una sesión
gráfica. Para este propósito, existe el paquete ``migasfree-launcher``.

  .. code-block:: none

    $ wget https://github.com/migasfree/migasfree-launcher/archive/latest.zip
    $ unzip latest.zip
    $ rm latest.zip
    $ cd migasfree-launcher-latest
    $ python setup.py --command-packages=stdeb.command bdist_deb
    $ cd ..

Sube el fichero migasfree-launcher al servidor:

  .. code-block:: none

    # migasfree-upload -f migasfree-launcher_1.0-1_all.deb

Ahora observa los ficheros que contiene este paquete:

* ``etc/sudoers.d/migasfree-launcher`` establece los comandos que no
  requieren **password de root** para que pueden ser ejecutados desde un
  usuario cualquiera. Puedes obtener más información sobre la configuración
  de ``sudoers`` ejecutando ``man sudoers`` en un terminal.

* ``etc/xdg/autostart/migasfree-indicator.desktop`` ejecutará el comando
  ``/usr/bin/migasfree-indicator`` cuando el usuario inicia sesión gráfica.
  ``migasfree-indicator`` llamará a ``/usr/bin/migasfree-launcher`` y éste a
  su vez a ``migasfree --update``.

  Puedes aprender más sobre la especificación de los ficheros **.desktop**
  en `freedesktop.org`__.

__ http://standards.freedesktop.org/desktop-entry-spec/latest/index.html

Ahora que ya tienes los paquetes ``tuempesa-migasfree-client`` y
``migasfree-launcher`` en el servidor migasfree, crea un despliegue en el
servidor y pon estos paquetes en ``paquetes a instalar`` y asígnale el
atributo ``SET-ALL SYSTEMS``.

  .. note::

      Para aprender más sobre el empaquetado, consulta la
      `Guía del nuevo desarrollador de Debian`__

__ http://www.debian.org/doc/manuals/maint-guide/index.es.html


  .. note::

      Para paquetería ``rpm``, los metadatos del paquete se especifican en
      un único fichero llamado ``SPEC``.
      Para aprender más sobre la creación de paquetes **rpm**, puedes consultar
      `rpm.org`__ y la `wiki del proyecto fedora`__.

__ http://www.rpm.org/
__ http://fedoraproject.org/wiki/How_to_create_an_RPM_package


Despliegue
==========

A partir de este momento, vas a poder administrar fácilmente los escritorios
Ubuntu de tu organización, de forma generalizada, instalando
simplemente estos dos paquetes.

Hay varias formas de realizar esta instalación:

* Bajando los dos paquetes a cada uno de los escritorios e instalándolos
  mediante el comando ``dpkg -i``

* Creando un fichero ``/etc/apt/sources.list.d/migasfree.list`` con el
  siguiente contenido:

  .. code-block:: none

    deb http://<myserver>/public/<project>/REPOSITORIES <deployment> PKGS

  donde sustituirás:

  * ``<myserver>`` por tu servidor.

  * ``<project>`` por el proyecto que pusiste en /etc/migasfree.conf

  * y ``<deployment>`` por el nombre de un despliegue que tenga como
  paquetes disponibles: ``acme-migasfree-client`` y ``migasfree-client``, y
  como paquetes a instalar: ``acme-migasfree-client``

  Una vez creado este fichero ejecuta:

    .. code-block:: none

      # apt-get update
      # apt-get install acme-migasfree-client

   y los paquetes se instalarán automáticamente.

* Puedes hacer un clon de un equipo donde ya estén instalados estos paquetes,
  utilizando un sistema de clonado como `clonezilla`__. Este es el método
  que usamos en **AZLinux**, y nos resulta muy cómodo y rápido ya que en
  una memoria USB llevamos un clonezilla, junto con la imagen clonada de nuestro
  escritorio, consiguiendo instalar un AZLinux en menos de 10 minutos.

__ http://clonezilla.org/

* Puedes crear un DVD de tu escritorio tal y como se realiza en el proyecto
  `vitalinux`__. En concreto, tendrías que adaptar el paquete `vx-create-iso`__
  a tus necesidades. En este método son los usuarios quienes se
  bajan la iso del DVD y se instalan ellos mismos el sistema.

__ http://vitalinux.org
__ https://github.com/vitalinux/vx-create-iso
