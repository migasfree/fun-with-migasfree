.. _`La Liberación`:

=============
La Liberación
=============

 .. epigraph::

   El conocimiento nos hace responsables.

   -- Ernesto Guevara.

Este es el capítulo que mejor define a *migasfree*, ya que su principal funcionalidad
es la de ofrecer unos determinados repositorios de paquetes que estarán
disponibles para los clientes en función de sus atributos.

En los proyectos de software libre, la liberación tiene que ver con poner a
disposición de la comunidad un determinado software. Aspectos como la autoría o
la licencia son esenciales, tanto o más como el propio software que se libera.

Liberar software en *migasfree* implica, además, **decidir quién tendrá acceso a
dicho software y a partir de qué momento**. Como vimos en la introducción al
hablar de :ref:`La liberacion`, esto es importante ya que antes de actualizar un
determinado software te conviene haberlo probarlo, para más tarde, si procede,
liberarlo paulatinamente a los equipos que lo requieran.


.. _`serversource`:

.. _`Orígenes`:

Orígenes
========

El primer paso para independizarte de los repositorios públicos
de tu Distribución GNU/Linux, es estudiarlos para a continuación **eliminarlos** y pasar dicha
configuración al servidor migasfree mediante lo que denominamos **Orígenes**.


    .. only:: not latex

       .. figure:: graphics/chapter09/source.png
          :scale: 100
          :alt: Origen migasfree.

          PC1 configurado a un origen de software vs PC2 configurado al mismo origen pero a través de un **origen migasfree**.


    .. only:: latex

       .. figure:: graphics/chapter09/source.png
          :scale: 80
          :alt: Origen migasfree.

          PC1 configurado a un origen de software vs PC2 configurado al mismo origen pero a través de un **origen migasfree**.


Un Origen en migasfree no es más que un **caché de un repositorio de paquetes**. Se configura
desde :ref:`El interfaz de administración` y por tanto está **centralizado**, lo que es una ventaja.

Cuando se ejecuta la sincronización (migasfree --update) es cuando se
creará, en el ordenador cliente, el fichero que configura dichos reposisitorios
(/etc/apt/sources.list.d/migasfree.list para apt y /etc/yum.repos.d/migasfree.repo para yum)

      .. warning::

        Los orígenes migasfree están disponibles desde la versión 4.17 (tanto
        del cliente como del servidor). Asegúrate que tienes todos los clientes actualizados
        antes de usar esta funcionalidad.

      .. note::

        Para Distros basadas en apt puedes estudiar los ficheros /etc/apt/sources.list y el
        directorio /etc/apt/sources.list.d/

      .. note::

        Para Distros basadas en yum mira los ficheros del directorio /etc/yum.repos.d/


      .. note::

        Un caché y un mirror de repositorio de paquetes no es lo mismo. El mirror tendrá
        descargados a priori todos los paquetes del repositorio público. En el caché, en cambio, se
        van descargando según los ordenadores los vayan solicitando.

      .. note::
        Si el servidor migasfree lo tienes en tu red local, tener configurados la lista de
        repositorios en Orígenes te va ahorrar, además, mucho tráfico de internet.


Campos de origen
-----------------


    * **Habilitado**: Activa o desactiva el origen.

    * **Nombre**: Denomina al origen.

    * **Proyecto**. Indica el proyecto *migasfree* al que pertenece.

    * **Comentario**: Campo de texto que sirve para registrar aclaraciones sobre
      el origen.

    * Origen: Aquí especificaremos el origen del repositorio público.

            .. note::

              Para más información consulta: ``man sources.list`` ó ``man yum.conf``, según el caso.


        * **base**: URI del repositorio público de la Distro GNU/Linux

        * **suite**: Suele indicar el nombre concreto de tu Distribución: **stretch**, **bionic**,
          **7** (para centos), etc.

        * **components**: Aquí se enumeran los distintos componentes del origen. Ejemplos pueden
          ser **main contrib non-free** (para Debian),  **main updates universe multiverse** (para
          Ubuntu, **os udpates extras** (para Centos)

        * **frozen**: Indica que los **metadatos del repositorio publico** no son actualizados. Con ello
          indicamos que queremos "congelar" el origen a la fecha de la primera solicitud de datos
          por parte de los ordenadores. Si se desmarca los metadatos son actualizados desde el repositorio
          público teniendo en cuenta el campo **expire**.

        * **options**: Permite especificar las distintas opciones que necesitemos para el repositorio.

        * **expire**: Minutos en que los metadatos del repositorio publico permanecerá cacheado. Sólo
          se tiene en cuenta para el caso que el campo **frozen no esté marcado**.


    * El qué (paquetes):

        * **Paquetes a instalar**: Campo de texto que especifica una lista de
          paquetes separados por espacios o por retornos de carro. Estos paquetes
          serán instalados **obligatoriamente** a los clientes que tengan acceso
          al origen.

          Se puede espeficar sólo el nombre del paquete, o el nombre de paquete
          más una versión.

          Este campo se tiene en cuenta al ejecutar los comandos de cliente
          ``migasfree --update`` y ``migasfree-tags --set``.

        * **Paquetes a desinstalar**: Campo de texto que especifica una lista de
          paquetes separados por espacios o por retornos de carro que serán
          desinstalados **obligatorimente** en los clientes.

          Este campo se tiene en cuenta al ejecutar los comandos de cliente
          ``migasfree --update`` y ``migasfree-tags --set``.

    * Por defecto:

        * **Paquetes pre-incluidos por defecto**: Campo de texto que especifica una
          lista de paquetes separados por espacios o por retornos de carro. Este
          campo sirve para instalar paquetes que configuran repositorios externos
          a migasfree (ver :ref:`Repositorios internos vs externos`).
          Un ejemplo de este tipo de paquetes lo tienes en el paquete `vx-repo-unizar`__.

          __ https://github.com/vitalinux/vx-repo-unizar

          La razón de la existencia de este campo, es que después de instalar este
          repositorio externo, es necesario obtener de nuevo los metadatos de
          los repositorios (``apt-get update``), a fin de que el cliente tenga acceso
          inmediatamente a los paquetes contenidos en el repositorio externo.

          Estos paquetes serán instalados a los clientes que tengan acceso al
          despliegue al ejecutar el comando ``migasfree-tags --set``.

        * **Paquetes incluidos por defecto**: Campo de texto que especifica una lista de
          paquetes separados por espacios o por retornos de carro. Estos paquetes
          serán instalados a los clientes que tengan acceso al origen al
          ejecutar el comando ``migasfree-tags --set``.

        * **Paquetes excluidos por defecto**: Campo de texto que especifica una lista de
          paquetes separados por espacios o por retornos de carro que serán
          desinstalados en los clientes que tengan acceso al origen al
          ejecutar el comando ``migasfree-tags --set``.

    * A quién (atributos):

        * **Atributos incluidos**: Aquellos clientes que tengan un atributo que
          coincida con los asignados en este campo tendrán accesible el
          origen (a menos que otro atributo lo excluya).

        * **Atributos excluidos**: Sirve para excluir atributos de la lista anterior.

          Por ejemplo, si quieres liberar el origen a toda la subred
          ``192.168.92.0`` menos al equipo ``PC13098``, puedes hacerlo asignando:

              * Atributos incluidos: ``NET-192.168.92.0/24``
              * Atributos excluidos:``HST-PC13098``

    * Cuándo (calendario):
        * **Fecha de inicio**: A partir de la cual estará disponible el origen
          en los clientes.

        * **Calendario**: Especifica una programación del origen basada en
          calendario.



Ejemplos
--------

Aterrizando, que desde el cielo no se ven a las hormigas: a continuación una lista
de configuraciones de Origenes a modo de ejemplo para Ubuntu y Centos.

      * **UBUNTU XENIAL**:


          * name: BASE

          * base: http://es.archive.ubuntu.com/ubuntu (ó http://softlibre.unizar.es/ubuntu/archive)

          * suite: xenial

          * components: main universe multiverse

          * frozen: True

          * options: [arch=amd64]


      * **UBUNTU XENIAL UPDATES**:

          * name: UPDATES

          * comentario: Actualizaciones para errores graves que no afectan
            la seguridad del sistema.

          * base: http://es.archive.ubuntu.com/ubuntu (ó http://softlibre.unizar.es/ubuntu/archive)

          * suite: xenial-updates

          * components: main universe multiverse

          * frozen: True

          * options: [arch=amd64]


      * **UBUNTU XENIAL SECURITY**:

          * name: UPDATES

          * comentario: Parches para vulnerabilidades de seguridad.
            Están gestionados por el Equipo de seguridad de Ubuntu y están diseñados para
            cambiar el comportamiento del paquete lo menos posible, de hecho, el mínimo
            requerido para resolver el problema de seguridad. Como resultado, tienden a
            ser de muy bajo riesgo de aplicación y se insta a todos los usuarios a
            aplicar actualizaciones de seguridad.

          * base: http://es.archive.ubuntu.com/ubuntu (ó http://softlibre.unizar.es/ubuntu/archive)

          * suite: xenial-security

          * components: main universe multiverse

          * frozen: False

          * options: [arch=amd64]

          * expire: 1440 minutos (Mantenemos los metadatos cacheados 1 día)


      * **UBUNTU XENIAL PPA tacocat/pylink-nightly**

          * name: PYLINK

          * comentario: Ejemplo de uso de PPA

          * base: http://ppa.launchpad.net/tacocat/pylink-nightly/ubuntu

          * suite: xenial

          * components: main

          * frozen: True

          * options: [arch=amd64]


      * **CENTOS 7**

          * name: BASE

          * base: http://mirror.centos.org/centos

          * suite: 7

          * components: os updates extras

          * frozen: True

          * options: gpgcheck=1 gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7


      * **CENTOS 7 EPEL**

          * name: EPEL

          * base: http://download.fedoraproject.org/pub/epel

          * suite: 7

          * components:

          * frozen: True

          * options: gpgcheck=1 gpgkey=https://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7



Subiendo paquetes al servidor
=============================

Acabamos de ver que mediante los :ref:`Orígenes` podemos almacenar paquetes de repositorios
públicos en el servidor migasfree, pero... ¿ y si quiero liberar un paquete que
he realizado yo mismo? ¿Como lo hago?

Lo primero que tienes que hacer es **subir el paquete al servidor** ( y después
ya podrás desplegarlo a los equipos que te interesen, pero vayamos poco a poco ).

Como viste en los primeros capítulos, la manera de hacerlo es utilizando el
comando de cliente:

  .. code-block:: none

    migasfree-upload -f <mipaquete>

o si quieres subir un conjunto de paquetes (Set) ponlos todos juntos
en un directorio y ejecuta:

  .. code-block:: none

    migasfree-upload -d <midirectorio>

Para subir paquetes al servidor es necesario utilizar un usuario que tenga permisos
de lectura/escritura en la tabla de almacenes y paquetes. Por defecto el usuario
``packager`` y el usuario ``admin`` los tienen.

Para no tener que introducir cada vez que subas un paquete al servidor
el usuario, su contaseña y/o el proyecto con el que trabajas, puedes asignar
los ajustes indicados en la sección [Packager] de
:ref:`Ajustes del cliente migasfree`.

.. _`serverstore`:

Almacenes
=========

Un almacén es una ubicación o ruta del servidor donde se colocan los paquetes y/o
conjuntos de paquetes subidos al servidor. No es más que un directorio colgando
de la ruta ``/var/migasfree/repo/<PROJECT>/STORES``, y que se utiliza para tener
organizados los paquetes. También es accesible desde un explorador web accediendo
a la ruta:

  .. code-block:: none

    http://tuservidor/public/<PROJECT>/STORES/

Lo anterioriormente expuesto, corresponde al lugar donde se almacenan los archivos
del paquete, pero además hay una parte lógica que es necesaria llevar en la
base de datos de *migasfree*. Es lo que denominamos registros de "Almacén".

Cuando se utiliza el comando ``migasfree-upload`` y se indica una ubicación
inexistente, el servidor automáticamente creará el registro lógico en la base de
datos y creará la carpeta en el sistema de archivos.

Campos de Almacén
-----------------

    * ``Nombre``: Denomina al almacén. Corresponde al nombre de la carpeta en el
      sistema de archivos.

    * ``Proyecto``. Indica el proyecto *migasfree* al que pertenece el almacén.

.. _`serverpackage`:

Paquetes
========

Cuando subes un paquete o un conjunto de paquetes al servidor, además de
copiarse en el almacén o ubicación indicada, se crea un registro lógico en la
base de datos. Estos registros nos servirán para asignarlos posteriormente en los
``Despliegues`` que vayamos creando.


Campos de Paquete
-----------------

    * ``Nombre``: Es el nombre del fichero del paquete.

    * ``Proyecto``: Indica el proyecto *migasfree* al que pertenece el paquete.

    * ``Almacén``: Especifica la ubicación donde está situado el paquete.


Acciones de Paquete
-------------------

A la derecha del nombre del paquete, en la lista de paquetes, hay un desplegable
con las siguientes acciones:

    * ``Información del paquete``. Permite ver los metadatos del paquete.

    * ``Descargar``. Permite almacenar el paquete seleccionado en tu equipo.

Si necesitas borrar uno o varios paquetes, selecciónalos y en el desplegable ``Acción``
elige ``Eliminar Paquetes/conjuntos seleccionados`` y después pulsa en el botón
``ir``.

    * ``Eliminar Paquetes/conjuntos seleccionados``. Permite borrar el registro
      del paquete. A medida que vayas haciendo cambios en el software,
      irás teniendo distintas versiones del mismo paquete. Generalmente, te
      interesará trabajar sólo con la última versión. Si quieres que sólo te
      aparezca ésta a la hora de asignarlo a los ``Despliegues``, puedes borrar
      los registros de ``Paquetes`` antiguos. Borrar el registro no borrará el
      archivo del paquete en ningún caso y simplificarás la selección de paquetes.

Paquetes huérfanos
------------------

Un paquete huérfano es un paquete que no está asignado a ningún despliegue.
Cuando un paquete es subido al servidor, o cuando lo quitas de un despliegue y
no está en ningún otro, se convierte en un paquete huérfano.
Existe una comprobación de ``Alerta`` que te avisará de cuáles son estos
paquetes.


Información de los paquetes
===========================

Si accedes a ``Liberación-Información de paquetes`` verás que te
aparecen dos carpetas:

    * ``STORES``. Muestra esta carpeta, en donde podrás navegar hasta un
      determinado paquete que hayas subido previamente.

    * ``REPOSITORIES`` Muestra los repositorios físicos (en el sistema de archivos)
      que se hayan creado, y que son los que, en última instancia, verán los
      clientes. En realidad, los paquetes que veas en ``REPOSITORIES`` no son
      más que enlaces simbólicos a los paquetes ubicados en ``STORES``.

Si quieres ver los metadatos de un determinado paquete, simplemente, pulsa sobre él.


.. _`Despliegues`:

.. _`serverdeployment`:

Despliegues
===========

Me gusta la definición: **migasfree es simplemente un gestor de despliegues
de paquetes**. En realidad es básicamente esto. De hecho, así es como empezó este
proyecto, y a partir de aquí ha ido creciendo hasta convertirse en lo que es hoy
en día, un gestor de sistemas.

A todos los efectos, y desde el punto de vista del cliente, un despliegue
en *migasfree* es un repositorio de paquetes estándar como los que puedas
encontrar en cualquier distribución. *Migasfree* permite crear muy fácilmente
estos repositorios y asignarlos a los equipos en función de sus atributos a
partir de una fecha determinada.

Campos de despliegue
--------------------

    * **Nombre**: Denomina al despliegue.

      .. note::

        En AZLinux solemos incorporar en el nombre del despliegue el número de
        tarea de redmine al que hace referencia el cambio de software que queremos
        liberar.

    * **Proyecto**: Especifica el proyecto en el que estará disponible el
      despliegue.

    * **Habilitado**: Activa o desactiva el despliegue.

    * **Comentario**: Campo de texto que sirve para registrar aclaraciones sobre
      el despliegue. Es muy conveniente que registres las modificaciones que
      vayas haciendo en este campo, indicando quién, cuándo y qué se ha modificado.

      Un ejemplo de cómo lo hacemos en AZLinux, sería:

      .. code-block:: none

        [alberto@2013-03-09] Añadido paquete azl-firefox-12.0-3_all.deb

        [alberto@2013-04-10] Añadido paquete azl-firefox-12.0-4_all.deb

        [eduardo@2013-05-10] Detectado problemas en algunos clientes. Desactivo
            el despliegue hasta diagnosticar y encontrar solución.

    * El qué (paquetes):

        * **Paquetes disponibles**: En este campo se seleccionan los ``paquetes`` y/o
          ``conjuntos de paquetes`` que se incluirán en el repositorio físico.

          Que un paquete esté incluido en un repositorio y el repositorio sea
          accesible desde el cliente, no implica que se instale el paquete.
          Los sistemas de paquetería sólo actualizan aquellos paquetes que ya
          estuvieran instalados en el sistema.

          Cada vez que hay una modificación de este campo y se pulsa el botón
          ``Grabar``, se generarán los metadatos del repositorio físico. Dependiendo de
          la cantidad de paquetes que se tengan que procesar, el tiempo
          para realizar este proceso puede ser largo. En los casos en los que se
          asigne un ``conjunto de paquetes`` donde se incluyan todos los paquetes
          de un DVD p.e. puede llegar a ser del orden de decenas de minutos.

          .. note::

           Fíjate que aparecen sólo los ``paquetes`` (los subidos individualmente) más
           los ``conjuntos de paquetes`` a la hora de seleccionarlos en los despliegues.
           Los paquetes incluidos dentro de los ``conjuntos de paquetes`` no pueden
           asignarse individualmente. Esto es así para simplificar y hacer más sencilla
           la asignación de ``paquetes`` y no perdernos entre los miles que
           componen una distribución.

        * **Paquetes a instalar**: Campo de texto que especifica una lista de
          paquetes separados por espacios o por retornos de carro. Estos paquetes
          serán instalados **obligatoriamente** a los clientes que tengan acceso
          al despliegue.

          Se puede espeficar sólo el nombre del paquete, o el nombre de paquete
          más una versión.

          Este campo se tiene en cuenta al ejecutar los comandos de cliente
          ``migasfree --update`` y ``migasfree-tags --set``.

        * **Paquetes a desinstalar**: Campo de texto que especifica una lista de
          paquetes separados por espacios o por retornos de carro que serán
          desinstalados **obligatorimente** en los clientes.

          Este campo se tiene en cuenta al ejecutar los comandos de cliente
          ``migasfree --update`` y ``migasfree-tags --set``.

    * Por defecto:

        * **Paquetes pre-incluidos por defecto**: Campo de texto que especifica una
          lista de paquetes separados por espacios o por retornos de carro. Este
          campo sirve para instalar paquetes que configuran repositorios externos
          a migasfree (ver :ref:`Repositorios internos vs externos`). Un ejemplo
          de este tipo de paquetes lo tienes en el paquete `vx-repo-unizar`__.

          __ https://github.com/vitalinux/vx-repo-unizar

          La razón de la existencia de este campo, es que después de instalar el
          repositorio externo, es necesario obtener de nuevo los metadatos de
          los repositorios (``apt-get update``), a fin de que el cliente tenga acceso
          inmediatamente a los paquetes contenidos en el repositorio externo.

          Estos paquetes serán instalados a los clientes que tengan acceso al
          despliegue al ejecutar el comando ``migasfree-tags --set``.

        * **Paquetes incluidos por defecto**: Campo de texto que especifica una lista de
          paquetes separados por espacios o por retornos de carro. Estos paquetes
          serán instalados a los clientes que tengan acceso al despliegue al
          ejecutar el comando ``migasfree-tags --set``.

        * **Paquetes excluidos por defecto**: Campo de texto que especifica una lista de
          paquetes separados por espacios o por retornos de carro que serán
          desinstalados en los clientes que tengan acceso al despliegue al
          ejecutar el comando ``migasfree-tags --set``.

    * A quién (atributos):

        * **Atributos incluidos**: Aquellos clientes que tengan un atributo que
          coincida con los asignados en este campo tendrán accesible el
          despliegue (a menos que otro atributo lo excluya).

        * **Atributos excluidos**: Sirve para excluir atributos de la lista anterior.

          Por ejemplo, si quieres liberar un paquete a toda la subred
          ``192.168.92.0`` menos al equipo ``PC13098``, puedes hacerlo asignando:

              * Atributos incluidos: ``NET-192.168.92.0/24``
              * Atributos excluidos:``HST-PC13098``

    * Cuándo (calendario):
        * **Fecha de inicio**: A partir de la cual estará disponible el despliegue
          en los clientes.

        * **Calendario**: Especifica una programación del despliegue basada en
          calendario. En el siguiente apartado tienes más información.

.. _`serverschedule`:

Calendarios
===========

Los calendarios te permiten programar sistemáticamente liberaciones en el tiempo
para unos determinados atributos previamente establecidos, partiendo de la
fecha de inicio del despliegue.

Por ejemplo, en AZLinux usamos distintos calendarios (LENTO, NORMAL, RÁPIDO,
MUY RÁPIDO) según la criticidad del cambio de software que se va a liberar
o de su urgencia. En estos calendarios, asignamos días de demora para los
distintos servicios de nuestra organización.

      .. code-block:: none

        CALENDARIO LENTO
            a los 0 días:  GRP-EQUIPOS DE TEST.
            a los 5 días:  CTX-SERVICIO DE PERSONAL
            a los 10 días: CTX-GESTION TRIBUTARIA
            a los 15 días: SET-ALL SYSTEMS

        CALENDARIO MUY RÁPIDO
            a los 0 días: CTX-SERVICIO DE PERSONAL, CTX-GESTION TRIBUTARIA
            a los 2 dias: SET-ALL SYSTEMS

Es conveniente que en la última demora asignes, si procede, el atributo
``SET-ALL SYSTEMS``.

Cuando asignas un calendario a un despliegue, podrás ver la temporalización
resultante en la columna ``línea temporal`` de ``Liberación-Despliegues``
(pulsa en el desplegable que contiene el nombre del calendario).

Asignar un calendario a un despliegue no es obligatorio.

Esta programación de la liberación se utiliza, fundamentalmente, para conseguir:

    * No aplicar una liberación de golpe a muchos equipos, lo que puede provocar
      un consumo de tráfico de red intenso (imagina 1000 equipos actualizando
      LibreOffice a la vez).

    * Liberar poco a poco los paquetes y así poder hacer comprobaciones más
      tranquilamente. Cualquier error en el empaquetado o *bug* en los fuentes
      del paquete, puede ser más manejable si ha afectado a pocos equipos y no
      a la totalidad.

Un determinado cliente tendrá acceso al despliegue si:

    * Tiene un atributo que coincide con alguno de los asignados en el despliegue
      y ya se ha cumplido la fecha de inicio del despliegue.

    * O existe un atributo coincidente con el calendario cuya fecha de inicio del despliegue
      más la demora se ha cumplido.

    * Siempre y cuando un atributo del cliente no coincida con  el campo ``atributos
      excluidos`` del despliegue.

Una manera en que puedes ver una estimación de la cantidad de equipos que un
calendario va haciendo efectivos los despliegues a lo largo de los días es
accediendo a la ``línea temporal`` en cada despliegue.

Campos de calendario
--------------------

    * **Nombre**: Denomina al calendario.

    * **Descripcion**: Describe el calendario.

    * Demoras: Es un conjunto de días (demoras) a los que se asignan atributos.

        * **Demora**: Número de días desde la fecha de inicio del despliegue a los que los
          atributos asignados serán efectivos. No se tienen
          en cuenta ni sábados ni domingos.

        * **Atributos**: Lista de atributos para una demora.

        * **Duración**: Número de días en que se completará el despliegue a
          los equipos asignados a la demora. O dicho de otra forma, si asignamos
          el atributo ``SET-ALL SYSTEMS`` y una duración de 20 días, obtendríamos un
          incremento diario aproximado del 5% del total de equipos.



.. _`catalogapplication`:

.. _`Aplicaciones`:

Aplicaciones
============

En los sistemas GNU/Linux existen front-ends para los PMS tales como `Synaptic`__
o el `Centro de software de Ubuntu`__ que permiten a los usuarios buscar e instalar
aplicaciones de forma sencilla.

__ https://es.wikipedia.org/wiki/Synaptic

__ https://es.wikipedia.org/wiki/Centro_de_software_de_Ubuntu

Ahora bien, estos front-end te permiten instalar miles de aplicaciones y
por supuesto la mayoría de ellas nunca van a ser instaladas en tu
organización. Por otra parte un usuario puede verse
aturdido al ver la cantidad de paquetes que puede instalar, y no encontrar la
que debe utilizar.

Conviene por tanto que  tu organización cuente con un catálogo de las
aplicaciones que más usáis.

Pues bien, mediante lo que denominamos ``Aplicaciones`` el servidor migasfree
**publica** éste catálogo de aplicaciones simplificando este proceso al usuario
mediante el uso de :ref:`Migasfree Play`.


Campos de Aplicaciones.
-----------------------

* **Nombre**: Identifica la aplicación

* **Categoría**: Permite clasificar la aplicación.

* **Nivel**: El ``nivel de usuario`` indica que no se requerirá tener
  privilegios de administrador deĺ ordenador para que usuario instalale la aplicación.
  En cambio si se establece la aplicación de ``nivel administrador`` sólo un
  usuario con privilegios de administrador en el ordenador podrá instalar la aplicación. En este
  caso :ref:`Migasfree Play` solicitará dicho usuario y contraseña.

* **Puntuación**: Relevancia para la organización.

* **Icono**: Campo obligatorio.

* **Disponible para los atributos**: La aplicación aparecerá publicada
  en los ordenadores que cuenten con alguno de los atributos especificados.

* **Descripción**: Campo que se utiliza para descibrir la aplicación. Puedes emplear
  notación `markdown`__.

__ https://es.wikipedia.org/wiki/Markdown

      .. note::

        Si quieres que el usuario encuentre ``gimp`` cuando busca por ``Photoshop``,
        puedes añadir en la descripción que: ``gimp es una alternativa a Photoshop``.


* **Paquetes por proyectos**: Por cada ``Proyecto`` se deben especificar los
  ``Paquetes a instalar`` en el ordenador.


.. _`catalogpolicy`:

Políticas
=========

Las políticas te van a permitir dar órdenes complejas de instalación y
desinstalación de aplicaciones.

Ya has visto que en los :ref:`Despliegues` puedes dar ordenes de instalar y
desinstalar paquetes de manera obligatoria a los ordenadores.

Ahora bien, imagina que quieres dar la orden de **instalar obligatoriamente**
un paquete en un grupo de ordenadores, y que se **desinstale obligatoriamente** en
el resto de ordenadores. ¿cómo se hace esto?

Una posible solución a este problema sería:

    * Crear un :ref:`Conjunto de atributos` ``A`` en donde incluimos los ordenadores
      a los que se va instalar el paquete obligatoriamente.

    * Crear otro Conjunto de atributos ``A-`` que sea el inverso de ``A``.
      Es decir: incluimos ``ALL SYSTEMS`` y excluimos ``A``.

    * Crear dos despliegues.

        * En uno asignamos como atributo el conjunto ``A``
          y ponemos como ``paquetes a instalar`` dicho paquete.

        * En el segundo asignamos como atributo el conjunto ``A-`` y
          ponemos el paquete en ``paquetes a desinstalar``

Vale, de acuerdo, esto funcionaría, pero es tedioso de configurar y de mantener.


Otro escenario imaginable puede ser el que en un ``proyecto migasfree``
una determinada aplicacion se llame diferente en otro ``proyecto migasfree``.
No es tan extraño, ocurre a menudo. ¿Como puedo dar una única orden de instalar
esa aplicación independientemente de como se llame y de qúe proyecto tenga configurado
cada ordenador?

Para estas situaciones (y otras similares), hemos creado lo que denominamos Políticas.

Una Politica comprende una **lista ordenada de prioridades** en las que se indica
que :ref:`Aplicaciones` se van a instalar obligatoriamente a unos determinados
atributos.

En el proceso de la sincronización del ordenador, un algoritmo recorre esta
lista ordenada y en cuanto se cumple que los atributos de una prioridad coinciden
con los del ordenador, se ordena **instalar** las :ref:`Aplicaciones` de esa la prioridad,
y además se ordenará **desinstalar** las :ref:`Aplicaciones` del resto de prioridades
siempre y cuando en la Politica esté marcado el campo ``exclusivo``.


Campos de Políticas.
--------------------

* **Nombre**: Denomina la política.

* **Comentario**: Describe la política.

* **Habilitado**: si desmarca este campo, la política está deshabilitada para todos los ordenadores.

* **Exclusivo**: Se ordena desinstalar las :ref:`Aplicaciones` asignadas en las prioridades que no se han cumplido.

* **atributos incluidos**: Permite especificar el área de aplicación de la politica, es decir a que ordenadores
  va a afectar dicha política.

* **atributos excluidos**: Permite excluir ordenadores del área de aplicación de la politica.

* **Grupos de políticas**: Lista de prioridades.

      * Prioridad: Es un número entero. Sirve únicamente para ordenar.

      * Atributos incluidos: Atributos a los que va se les va a instalar :ref:`Aplicación` indicada en la prioridad.

      * Atributos excluidos: Excluye atributos de la prioridad.

      * Aplicaciones: Lista de Aplicaciones.



Ejemplo de uso.
---------------

Julián puede iniciar sesion en cualquier ordenador, pero
se necesita deshabilitarle el montaje de unidades USB y CDROM sólamente para él.

1. Crea el paquete que deshabilita el montaje de USB y CDROM: :ref:`acme-media-disable`.

2. Pon el paquete ``acme-media-disable`` en un despliegue disponible para ``ALL SYSTEMS``

3. Crea la ``Aplicación NO-MEDIA``.

4. Crea la ``Politica Julián``

    * Nombre: Julian

    * Comentario: No queremos que Julián use USB.

    * Exclusivo: Marcado

    * Atributos incluidos: ``ALL SYSTEMS``

    * Grupos de politicas:

        * Prioridad 1:

             * Atributos incluidos: ``USR-Julian``

             * Aplicaciones: ``NO-MEDIA``

        * Prioridad 2:

             * Atributos incluidos: ``ALL SYSTEMS``

             * Aplicaciones: (vacio)

Cuando Julián inicia sesión en cualquier ordenador y se ejecuta la sincronización con
el servidor migasfree, el algoritmo de las políticas recorre las prioridades
en orden:

    * Prioridad 1: Como se cumple (es Julian) se instala la aplicacion `NO-MEDIA`,
      y cómo está marcado el campo `exclusivo` se desinstala las Aplicaciones del
      resto de prioridades (no hay ninguna en Prioridad 2)

Veamos ahora como funcionaría para cualquier usuario que **no** sea Julian:

    * Prioridad 1: Como no se cumple (no es Julian) salta a la siguiente prioridad.

    * Prioridad 2: Como se cumple `ALL SYSTEMS`, se instalan las aplicaciones
      de la prioridad 2 (ninguna en este caso), y cómo está marcado el campo `exclusivo`
      se desinstalan las Aplicaciones del resto de prioridades. Por tanto se desintalará
      la aplicación `NO-MEDIA`

En resumen, en cualquier ordenador Julian tendrá instalada la aplicacion `NO-MEDIA`
y el resto de usuarios no.

.. _`Repositorios internos vs externos`:

Repositorios internos vs externos
=================================

Llamamos repositorio interno al repositorio que **controla** el servidor *migasfree*.

Un repositorio externo es un repositorio configurado en los clientes y que no
apunta al servidor *migasfree*. Los repositorios que vienen por defecto configurados
en las distribuiciones son un ejemplo. Otro serían los repositorios tipo ``ppa``.

Si quieres tener un mayor control de tus sistemas, mi recomendación es que hagas uso
los :ref:`Orígenes`, pero una segunda opción es que te bajes todos los paquetes de los
repositorios de tu distribución y luego los subas como
``conjunto de paquetes`` al servidor y crees un despliegue
al efecto. A esto, lo denominamos ``congelar un repositorio`` y vendría a ser como
un mirror del repositorio publico.

De esta manera, tendrás congelados a una fecha los repositorios de tu distribución,
y podrás actualizar sólo el software que te interese. Si te decides por este
método, obviamente tendrás que empaquetar un código que deshabilite los
repositorios externos en los clientes.

+------------------------------+------------------------------+
| Repositorios Internos        | Repositorios Externos        |
+==============================+==============================+
| Requieren mantenimiento      | No requieren mantenimiento   |
| ante las actualizaciones de  | ya que es mantenido por el   |
| los paquetes                 | dueño del repositorio        |
+------------------------------+------------------------------+
| Mayor control de los sistemas| Menor control frente a los   |
| frente a los cambios, siendo | cambios                      |
| tu quién decide qué          |                              |
| actualizaciones deben        |                              |
| producirse                   |                              |
+------------------------------+------------------------------+
| Si el servidor migasfree está| Genera tráfico internet      |
| en la red local, no produce  |                              |
| tráfico internet             |                              |
+------------------------------+------------------------------+


Un pequeño script para obtener los paquetes de los repositorios externos
(en este caso para ubuntu-16.04) podría ser:

  .. code-block:: none

    #!/bin/bash

    function download(){
      _SERIE_POCKET=$1
      download_repo "$_SERIE_POCKET" "main"
      download_repo "$_SERIE_POCKET" "multiverse"
      download_repo "$_SERIE_POCKET" "restricted"
      download_repo "$_SERIE_POCKET" "universe"
    }

    function download_repo(){
      _SERVER=http://en.archive.ubuntu.com/ubuntu
      _PKGS=Packages
      _SERIES=$1
      _REPO=$2
      _PATH=`pwd`
      echo "PATH= $_PATH"
      wget $_SERVER/dists/$_SERIES/$_REPO/binary-amd64/$_PKGS.bz2
      bzip2 -d $_PKGS.bz2
      _FILES=`grep "^Filename:" $_PKGS| awk '{print $2}'|sort`
      _TARGET=$_SERIES-$_REPO
      echo "$_FILES" > Packages-$_TARGET
      mkdir -p $_TARGET
      cd "$_TARGET"
      for _f in $_FILES
      do
        _file=${_f:6+${#_REPO}}
        _BASE=`basename $_file`
        mkdir -p `dirname $_file`
        echo "Downloading $_SERIES $_f"
        wget -c -t1  $_SERVER/$_f -O $_file
      done
      cd "$_PATH"
      rm $_PKGS
    }

    download "xenial-security"
    download "xenial-updates"
    download "xenial-backports"
    download "xenial"


El proceso de la liberación
===========================

Las tareas que debe realizar un liberador son:

    * Controlar que no haya paquetes huérfanos, borrando los paquetes antiguos
      y creando los despliegues adecuados para los nuevos paquetes.

    * Decidir qué calendario es conveniente aplicar a cada despliegue.

    * Decidir cuándo un despliegue ha terminado de liberarse (se ha cumplido
      toda la línea temporal) y qué debe hacerse con sus paquetes.

      En AZLinux mayoritariamente, y para no tener muchos despliegues activos,
      estos paquetes los asignamos a otro despliegue (ya existente para este
      fin) que tiene asignado sólo el atributo ``SET-ALL SYSTEMS``. Los despliegues
      que nos han servido para liberar poco a poco los paquetes son
      desactivados (no los borramos) para mantener así la historia de lo que
      se ha ido haciendo.
