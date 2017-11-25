==================
Ejemplos prácticos
==================

 .. epigraph::

   La imaginación tiene sobre nosotros mucho más imperio que la realidad.

   -- Jean de la Fontaine

A continuación, te voy a mostrar una selección representativa de peticiones e
incidencias de la Gestión de Configuración Software, junto con una solución, la que
creo más acertada a día de hoy, porque es obvio que no existe una única solución
a los problemas.

El objetivo de estos ejemplos (basados en casos reales del proyecto AZLinux)
es afianzar los conceptos que hemos ido viendo durante los capítulos
anteriores. De esta manera, podrás hacerte una mejor idea de toda la potencia de
trabajar con la paquetería estándar de tu distibución Linux junto con migasfree,
en el proceso de la GCS.

El código fuente de los paquetes utilizados en este capítulo está disponible en
`http://github.com/migasfree/fun-with-migasfree-examples`__

__ http://github.com/migasfree/fun-with-migasfree-examples

Descárgatelo si aún no lo has hecho:

  .. code-block:: none

    $ wget https://github.com/migasfree/fun-with-migasfree-examples/archive/4.13.zip
    $ unzip 4.13.zip
    $ cd fun-with-migasfree-examples-4.13


Deshabilitar montaje de unidades USB y CDROM
============================================

a) Petición de cambio
------------------

Todos los ordenadores de la ``NET-192.168.100.0/24``, excepto el ordenador ``CID-3245``,
no deberían montar unidades USB por motivos de seguridad. Tampoco deben montar
unidades USB aquellos usuarios que pertenezcan al grupo de LDAP ``GRP-NO-MEDIA``, ni
tampoco el ordenador ``CID-1291``.


b) Aceptación de la petición
-------------------------

Realizaremos lo que denominamos una ``directiva de seguridad basada en un conjunto de atributos``,
ya que es muy probable que, con el tiempo, esta medida de seguridad puede ir
cambiando sus reglas asignándose o excluyéndose otros atributos.


c) Cambio
---------

Después de buscar en Internet la forma de bloquear el montaje de dispositivos
USB, y de varias pruebas, llegamos a la conclusión que realizar un cambio de
permisos en el directorio ``/media`` es suficiente para alcanzar nuestro objetivo.


ECS: acme-media-disable (nuevo)
...............................

Decidimos crear el paquete ``acme-media-disable`` que bloqueará el montaje en
``/media`` cuando esté instalado este paquete.

Observa como en la `post-instalación`__ del paquete se restringe los permisos a
``/media``, y como en la `post-desintalación`__ dejamos los permisos por defecto.

__ http://github.com/migasfree/fun-with-migasfree-examples/blob/master/acme-media-disable/debian/postinst#L23
__ http://github.com/migasfree/fun-with-migasfree-examples/blob/master/acme-media-disable/debian/postrm#L24


Crea el paquete ``acme-media-disable`` (debes tener previamente instalados el
paquete ``devscripts`` y ``debhelper``)

  .. code-block:: none

    $ cd acme-media-disable
    $ /usr/bin/debuild --no-tgz-check -us -uc
    $ cd ..

y súbelo al servidor.

  .. code-block:: none

    # migasfree-upload -f acme-media-disable_1.0-1_all.deb

d) Liberación
-------------

Creamos el conjunto de atributos ``SET-NO-MEDIA``:

    ATRIBUTOS:

        ``NET-192.168.100.0/24``

        ``GRP-NO-MEDIA``

        ``CID-1291``

    EXCLUYE:

        ``CID-3245``


Creamos un despliegue ``MEDIA-DISABLE``:

    Asignamos el paquete: ``acme-media-disable_1.0-1_all.deb``

    Ponemos en paquetes a instalar: ``acme-media-disable``

    asignamos en atributos incluidos: ``SET-NO-MEDIA``


Ahora es necesario crear otro despliegue, ``MEDIA-ENABLE``, para forzar la desinstalación del
paquete cuando el ordenador ya no pertenezca al conjunto de atributos ``SET-NO-MEDIA``:

    Ponemos en paquetes a desinstalar: ``acme-media-disable``

    asignamos en atributos incluidos: ``ALL-SYSTEMS``

    asignamos en atributos excluidos: ``SET-NO-MEDIA``


Para añadir o exluir atributos en el futuro, simplemente bastará con
modificar el conjunto de atributos ``SET-NO-MEDIA``.

   .. note::

      Este es un ejemplo de cómo implementar una "directiva de seguridad"". En versiones
      futuras de migasfree se incluirá un modelo de "directivas" para no tener
      que añadir ese segundo despliegue que fuerza la desinstalación de los
      paquetes.


Cierre de sesión gráfica en ordenadores HP ProDesk 600 G2 SFF
=============================================================

a) Petición de cambio
---------------------

Aleatoriamente y de repente, se cierra la sesión gráfica de usuario en los equipos
``HP ProDesk 600 G2 SFF``

Frecuencia aproximada del error: de 0 a 3 cierres de sesión por día.

Se han recibido incidencias de este tipo sólo en algunos equipos de este modelo de
ordenador.

b) Aceptación
-------------

Se comprueba, observando el fichero ``/var/log/syslog``, que el error en estos equipos es
provocado por la tarjeta gráfica ``intel-hd-graphics-530``, que se identifica como
``PCI-8086:1912`` incluida en los ordenadores ``HP ProDesk 600 G2 SFF``.

c) Cambio
---------

Después de buscar en Internet información relativa a este error, y de probar
distintas soluciones, llegamos a comprobar que modificando el método de
aceleración de la tarjeta gráfica, siguiendo un workaround__ propuesto en Internet,
el error ya no se reproduce.

__ https://bugs.launchpad.net/ubuntu/+source/xserver-xorg-video-intel/+bug/1510970/comments/40

ECS: acme-intel-hd-graphics-530 (nuevo)
...............................

Creamos un paquete ``acme-intel-hd-graphics-530`` que, simplemente, modifica el
método de acelaración añadiendo en el sistema el fichero
``/usr/share/X11/xorg.conf.d/20-intel-hd-graphics-530.conf`` con el siguiente contenido:

  .. code-block:: none

    Section "Device"
     Identifier "Card0"
     Driver "Intel"
     Option "AccelMethod" "uxa"
    EndSection


y lo subimos al servidor.


d) Liberación
-------------

Dado que tenemos en producción unos 120 equipos con la tarjeta gráfica ``PCI-8086:1912``
desplegaremos este paquete poco a poco (sólo a los ordenadores que tengan dicho atributo)
ya que no sabemos, a priori, qué otros efectos no deseados puede provocar el
cambio de acelaración gráfica.

Creamos un calendario únicamente para este despliege:

Calendario ``intel-hd-graphics-530``

    Demora: ``0``

    Atributos: ``PCI-8086:1912``

    Duración: ``20 días``


Creamos el despliegue ``intel-hd-graphics-530``

    Ponemos en paquetes a instalar: ``acme-intel-hd-graphics-530``

    Asignamos en calendario: ``intel-hd-graphics-530``


   .. note::

      De esta manera se actualizarán aproximadamente 120/20 = 6 ordenadores por día, lo que
      puede ser manejable por el servicio telefónico de Asistencia a Usuarios en caso de
      producirse efectos no deseados.


Etiqueta MEDIA-DISABLE en migasfree
===================================

a) Petición de cambio
---------------------

Crear una etiqueta en migasfree para desplegar software en los equipos que no
deben montar unidades USB y CDROM.


b) Aceptación
-------------

Se rechaza la petición, debido a que ya disponemos del conjunto de atributos
``SET-MEDIA-DISABLE``.

   .. note::

      Los ``conjuntos de atributos`` son mucho más **versátiles** que una simple
      ``etiqueta`` asignada a un ordenador. La ``etiqueta`` está pensada para que un
      usuario puede asignarla desde su ordenador mediente el comando
      ``migasfree-tags``. En cambio, los ``conjuntos de atributos`` son
      definidos en el servidor por un administrador mediante la asignación y
      exclusión de ``atributos`` y/o  otros ``conjuntos de atributos``.


Instalación de software en ``AULA-3``
=====================================

a) Petición de cambio
---------------------

Se va a proceder a impartir cursos sobre gimp__ en el AULA-3. Es neceserario
que este software esté instalado esta misma tarde, a las 16:00 h, en todos los ordenadores
de dicha aula.

__ https://www.gimp.org/

b) Aceptación
-------------

Existe un despliegue ``per-aula-3`` para añadir software a los equipos
de dicha aula. Como atributos incluidos, este despliegue tiene el conjunto de
atributos ``SET-AULA-3``

    Conjunto de atributos ``SET-AULA-3``:

        ``CID-3578``

        ``CID-3579``

        ``CID-3580``

        ``CID-3581``

        ``CID-3582``

        ``CID-3583``

        ``CID-3584``

        ``CID-3585``

    Despliegue ``per-aula-3``:

        paquetes a instalar:

            inkscape__

            scribus__

            gvsig__

            virtualbox__

        atributos incluidos: ``SET-AULA-3``

__ https://inkscape.org

__ https://www.scribus.net/

__ http://www.gvsig.com/es

__ https://www.virtualbox.org/

c) Cambio
---------

En este caso no hay implicado ningún ECS que tenga que ser modificado.


d) Liberación
-------------

Editamos el despliegue ``per-aula-3``

    añadimos a los paquetes a instalar : ``gimp``

   .. note::

      Cuando los equipos del AULA-3 inicien la próxima sesión gráfica,
      automáticamente se les instalará el software solicitado. Observa que no
      es necesario desplazarnos al aula, acceder por control remoto, ni tan siquiera
      encender los equipos. El software se instalará cuando, plácidamente, esté
      echando mi siesta después de comer.
