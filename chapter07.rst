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

En este capítulo vas a configurar el cliente de migasfree para que se
conecten contra la maquina virtual debian 7 en el que ya tienes un servidor
migasfree instalado.

Todos los comandos de este capítulo lo vas a ejecutar en otra máquina virtual
(ubuntu 12.04) que debes tener en la misma red en la que esté la maquina
virtual del servidor.

El objetivo de este capítulo es que conozcas un poco más el empaquetado.

Obteniendo acme-migasfree-client
================================

Al igual que hiciste con la configuración del servidor puedes bajarte
el fuente del paquete que vamos a utilizar de plantilla.

En la nueva máquina virtual con ubuntu 12.04 ejecuta:

  .. code-block:: none

    $ wget http://www.migasfree.org/repo/book/acme-migasfree-client_1.0-1.tar.gz
    $ tar -xzvf acme-migasfree-client_1.0-1.tar.gz

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
  Cada vez que se modifica el paquete hay que añadir una entrada en este
  fichero incrementando la versión y registrando lo que se ha modificado.

* El fichero ``copyright`` contiene la información sobre los recursos,
  licencia y derechos de autoría de las fuentes originales del paquete.

* El fichero ``rules``  contiene las reglas que se utilizan para generar
  los paquetes a partir de sus fuentes.

* El fichero ``install`` contiene una lista de ficheros que serán
  instalados con el paquete

Ahora que conoces el significado de estos ficheros modifícalos cambiando
el nombre del paquete ``acme-migasfree-client`` por ``tuempresa-migasfree-client``
y pon tu nombre y la fecha actual allí dónde se requiera.

Modifica tambien el nombre del directorio raiz ``acme-migasfree-client``
por ``tuempresa-migasfree-client``

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
desviación indicamos al sistema de gestión de paquetes que un fichero ya
no pertenece a un determinado paquete sino al que nosotros establezcamos.

Así el fichero de configuración ``/etc/migasfree.conf``, que pertenece en
principio al paquete migasfree-client, hacemos que pertenezca al paquete
``tuempresa-migasfree-client`` de tal manera que una posible
actualización de ``migasfree-client`` ya no nos afectará. Cada vez que
queramos modificar un ajuste del cliente migasfree en ``/etc/migasfree.conf``
lo haremos a través del fichero ``usr/share/divert/etc/migasfree.conf``
del paquete ``tuempresa-migasfree-client``.

Fíjate tambien en que en ``prerm`` deshacemos esta desviación, para que
si desinstalamos el paquete quede todo como estaba.

Modifica ahora el fichero ``usr/share/divert/etc/migasfree.conf`` para que
servidor apunte al servidor migasfree debian 7. El resto de ajuste
modifícalos según tus intereses. Una vez hecho esto y situado en el
directorio ``tuempresa-migasfree-client`` genera el paquete.

  .. code-block:: none

    $ /usr/bin/debuild --no-tgz-check -us -uc

Con esto tendrás un paquete que configura el cliente migasfree para tu
organización. Ahora es momento de instalarlo y de subirlo al servidor
migasfree.

  .. code-block:: none

    $ dpkg -i tuempresa-migasfree-client_1.0-1_all.deb
    $ migasfree-upload -f tuempresa-migasfree-client_1.0-1_all.deb


Ejecución del cliente migasfree
===============================

Hasta ahora siempre hemos ejecutado el cliente migasfree desde consola
mediante el comando ``migasfree -u`` como ``root``. Ahora vamos a hacer
que se ejecute automáticamente cada vez que el usuario abra una sesión
gráfica. Para este propósito existe el paquete ``migasfree-launcher``.

  .. code-block:: none

    $ wget https://github.com/agacias/migasfree-launcher/archive/master.zip
    $ unzip master.zip
    $ rm master.zip
    $ cd migasfree-launcher-master
    $ /usr/bin/debuild --no-tgz-check -us -uc
    $ cd ..

Sube el fichero migasfree-launcher al servidor

  .. code-block:: none

    # migasfree-upload -f migasfree-launcher_1.0-1_all.deb

Ahora observa los ficheros que contiene este paquete:

* ``etc/sudoers.d/migasfree-launcher`` establece los comandos que no
  requieren password de root para que pueden ser ejecutados desde un
  usuario cualquiera. Puedes obtener más información sobre la configuración
  de ``sudoers`` ejecutando ``man sudoers`` en un terminal.

* ``etc/xdg/autostart/migasfree-launcher.desktop`` ejecutará el comando
  ``/usr/bin/migasfree-launcher`` cuando el usuario inicia sesión gráfica.
  Este comando llamará finalmente a ``migasfree -u``. Puedes aprender más
  sobre la especificación de los ficheros .desktop en `freedesktop.org`__.

__ http://standards.freedesktop.org/desktop-entry-spec/latest/index.html

* ``usr/share/applications/migasfree-launcher.desktop`` es un fichero
  .desktop que pone disponible en el menú de ``Herramientas del Sistema``
  al comando migasfree-launcher.

* ``/usr/bin/migasfree-launcher`` comando para actualizar el sistema
  a través de un servidor migasfree.

Ahora que ya tienes los paquetes ``tuempesa-migasfree-client`` y
``migasfree-launcher`` en el servidor migasfree, crea un repositorio en el
servidor y pon estos paquetes en ``paquetes a instalar`` y asígnale el
atributo ``ALL-SYSTEMS``.

  .. note::

      Para aprender mas sobre el empaquetado consulta la
      `Guía del nuevo desarrollador de Debian`__

__ http://www.debian.org/doc/manuals/maint-guide/index.es.html


  .. note::

      Para paquetería rpm los metadatos del paquete se especifican en
      un único fichero llamado ``SPEC``.
      Para aprender más sobre la creación de paquetes rpm puedes consultar
      `rpm.org`__ y la `wiki del proyecto fedora`__.

__ http://www.rpm.org/
__ http://fedoraproject.org/wiki/How_to_create_an_RPM_package


Despliegue
==========

A partir de este momento vas a poder administrar fácilmente los escritorios
ubuntu-12.04 de tu organización, de forma generalizada, instalando
simplemente estos dos paquetes.

Hay varias formas de realizar esta instalación:

* Bajando los dos paquetes a cada uno de los escritorios e instalándolos
  mediante el comando ``dpkg -i``

* Creando un fichero ``/etc/apt/sources.list.d/migasfree.list`` con el
  siguiente contenido:

  .. code-block:: none

    deb http://<myserver>/repo/<version>/REPOSITORIES <store> PKGS

  donde sustituirás:

  * ``<myserver>`` por tu servidor.

  * ``<version>`` por la versión que pusiste en /etc/migasfree.conf

  * y ``<store>`` por la ubicación que pusiste al subir el paquete al servidor migasfree
    con migasfree-upload.

  Una vez creado este fichero ejecuta:

    .. code-block:: none

      # apt-get update
      # migasfree -u

   y los paquetes se instalarán automáticamente

* Puedes hacer un clon de un equipo donde ya estén instalados estos paquetes
  utilizando un sistema de clonado como `clonezilla`__. Este es el método
  que usamos en AZLinux, y nos resulta muy cómodo y rápido ya que en
  una memoria USB llevamos un clonezilla junto con la imagen clonada de nuestro
  escritorio consiguiendo instalar un AZLinux en menos de 10 minutos.

__ http://clonezilla.org/

* Puedes crear un DVD de tu escritorio tal y como se realiza en el proyecto
  `vitalinux`__. En concreto tendrías que adaptar el paquete `vx-create-iso`__
  a tus necesidades. En éste método son los usuarios quienes se
  bajan la iso del DVD y se instalan ellos mismos el sistema.

__ http://vitalinux.unizar.es
__ https://github.com/vitalinux/vx-create-iso

