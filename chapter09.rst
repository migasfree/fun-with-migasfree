=============
La Liberación
=============

 .. epigraph::

   El conocimiento nos hace responsables.

   -- Ernesto Guevara.

Este es el capítulo que mejor define a migasfree, ya que su principal funcionalidad
es la de ofrecer unos determinados repositorios de paquetes que estarán
disponibles para los cliente en función de sus atributos.

En los proyectos de software libre la liberación tiene que ver con poner a
disposición de la comunidad un determinado software. Aspectos como la autoría o
la licencia son esenciales, tanto o más como el propio software que se libera.

Liberar software en migasfree implica además decidir a quién y a partir de en qué
momento un cliente tendrá acceso a dicho software.


Subiendo Paquetes al servidor
=============================

Antes de poder liberar el software obviamente tienes que subirlo al servidor.

Como viste en los primeros capítulos la manera de hacerlo es utilizando el
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
el usuario, su contaseña y/o la versión con la que trabajas, puedes asignar
los ajustes indicados en la sección [Packager] de
:ref:`Ajustes del cliente migasfree`.

Almacenes
=========

Un almacén es un ubicación o ruta del servidor donde se colocan los paquetes y/o
conjuntos de paquetes subidos al servidor. No es más que un directorio colgando
de la ruta /var/migasfree/repo/<VERSION>/STORES, y que se utiliza para tener
organizados los paquetes. Tambien es accesible desde un explorador web accediendo
a la ruta:

  .. code-block:: none

    http://tuservidor/repo/<VERSION>/STORES.

Lo anterioriormente expuesto corresponde al lugar donde se almacenan los archivos
del paquete, pero además hay una parte lógica que es necesaria llevar en la
base de datos de migasfree. Es lo que denominamos registros de "Almacén".

Cuando se utiliza el comando ``migasfree-upload`` y se indica una ubicación
inexistente, el servidor automáticamente creará el registro lógico en la base de
datos y creará la carpeta en el sistema de archivos.

Campos de Almacén:
..................

    * ``Nombre``: Denomina al almacén. Corresponde al nombre de la carpeta en el
      sistema de archivos.

    * ``Versión``. Indica la versión migasfree a la que pertenece el almacén.


Paquetes
========

Cuando subes un paquete o un conjunto de paquetes al servidor además de
copiarse en el almacén o ubicación indicada, se crea un registro lógico en la
base de datos. Estos registros nos servirán para asignarlos posteriormente en los
``Repositorios`` que vayamos creando.



Campos de Paquete:
..................

    * ``Nombre``: Es el nombre del fichero del paquete.

    * ``Versión``: Indica la versión migasfree a la que pertenece el paquete.

    * ``Almacén``: Especifica la ubicación donde está situado el paquete.

Acciones de Paquete:
....................

Para usar las acciones de un paquete selecciónalo, elije la acción deseada y pulsa en
el botón ``ir``.

    * ``Información del paquete``. Permite ver los metadatos del paquete.

    * ``Bajar``. Permite almacenar el paquete seleccionado en tu equipo.

    * ``Borrar``. Permite borrar el registro del Paquete. A medida que vayas
      haciendo cambios en el software irás teniendo distintas versiones
      del mismo paquete. Generalmente te interesará trabajar sólo con la
      última versión. Si quieres que sólo te aparezca ésta a la hora de
      asignarlo a los ``Repositorios`` puedes borrar los registros de
      ``Paquetes`` antiguos. Borrar el registro no borrará el archivo del
      paquete en ningún caso y simplificarás la selección de paquetes.

Paquetes huérfanos
..................

Un paquete huérfano es un paquete que no está asignado a ningún Repositorio.
Cuando un paquete es subido al servidor, o cuando lo quitas de un repositorio y
no está en ningún otro repositorio se convierte en un paquete huérfano.
Existe una comprobación de ``Estado`` que te alertará de cuales son estos
paquetes.


Información de los paquetes
===========================

Si accedes a ``Liberación-Empaquetado-Información de paquetes`` verás que te
aparecen dos carpetas:

    * ``STORES``. Muestra ésta carpeta, en donde podrás navegar hasta un
      determinado paquete que hayas subido previamente.

    * ``REPOSITORIES`` Muestra los Repositorios físicos (en el sistema de archivos)
      que se hayan creado, y que son los que en última instalancia verán los
      clientes. En realidad los paquetes que veas en ``REPOSITORIES`` no son
      más que enlaces simbólicos a los paquetes ubicados en ``STORES``.

Si quieres ver los metadatos de un determinado paquete simplemente haz click
en él.

Repositorios
============

Me gusta la definición: **migasfree es simplemente un gestor de repositorios
de paquetes**. En realidad es básicamente esto. De hecho así es como empezó este
proyecto, y a partir de aquí ha ido creciendo hasta convertirse en lo que es hoy
en día, un gestor de sistemas.

A todos los efectos, y desde el punto de vista del cliente, un repositorio
en migasfree es un repositorio de paquetes estándar como los que puedas
encontrar en cualquier Distribución. Migasfree permite crear muy fácilmente
estos repositorios y asignarlos a los equipos en función de sus atributos a
partir de una fecha determinada.

Campos de Repositorio
.....................

    * ``Nombre``: Denomina al repositorio.

      .. note::

        En AZLinux solemos incorporar en el nombre del repositorio el número de
        tarea de redmine al hace referencia el cambio de software que queremos
        liberar.

    * ``Versión``: Especifica la versión en la que estará disponible el
      repositorio.

    * ``Habilitado``: Activa o desactiva el repositorio.

    * ``Comentario``: Campo de texto que sirve para registrar aclaraciones sobre
      el repositorio. Es muy conveniente que registres las modificaciones que
      vayas haciendo a los repositorios en este campo, indicando quién, cuándo
      y qué se ha modificado.

      Un ejemplo de como lo hacemos en AZLinux sería:

      .. code-block:: none

        [alberto@2013-03-09] Añadido paquete azl-firefox-12.0-3_all.deb

        [alberto@2013-04-10] Añadido paquete azl-firefox-12.0-4_all.deb

        [eduardo@2013-05-10] Detectado problemas en algunos clientes. Desactivo
            el repositorio hasta diagnosticar y encontrar solución.

    * ``Fecha``: A partir de la cual estará disponible el repositorio
      en los clientes.

    * ``Calendario``: Especifica una programación del repositorio basada en
      calendario. En el siguiente apartado tienes más información.

    * Packages

        * ``Paquetes``: En este campo se seleccionan los ``paquetes`` y/o
          ``conjuntos de paquetes`` que se incluirán en el repositorio.

          Que un paquete este incluido en un repositorio y el repositorio
          accesible desde el cliente, no implica que se instale el paquete.
          Los sistemas de paquetería sólo actualizan aquellos paquetes que ya
          estuvieran instalados en el sistema.

          Cada vez que hay una modificación de este campo y se pulsa el botón
          ``Guardar`` se generarán los metadatos del repositorio. Dependiendo de
          la cantidad de paquetes que se tengan que procesar, el tiempo
          para realizar este proceso puede ser largo. En los casos en los que se
          asigne un ``conjunto de paquetes`` donde se incluyan todos los paquetes
          de un DVD p.e.  puede llegar a ser del orden de decenas de minutos.

          .. note::

           Fíjate que aparecen sólo los ``paquetes`` (los subidos individualmente) más
           los ``conjuntos de paquetes`` a la hora de seleccionarlos en los repositorios.
           Los paquetes incluidos  dentro de los ``conjuntos de paquetes`` no pueden
           asignarse individualmente. Esto es así para simplificar y hacer más sencilla
           la asignación de ``paquetes`` y no perdernos entre los miles que
           componen una Distribución.

        * ``Paquetes a instalar``: Campo de texto que especifica una lista de
          paquetes separados por espacios o por retornos de carro. Estos paquetes
          serán instalados **obligatoriamente** a los clientes que tengan acceso
          al repositorio.

          Se puede espeficar sólo el nombre del paquete, o el nombre de paquete
          mas una versión.

          Este campo se tiene en cuenta al ejecutar los comandos de cliente
          ``migasfree --update`` y ``migasfree-tags --set``

        * ``Paquetes a desinstalar``: Campo de texto que especifica una lista de
          paquetes separados por espacios o por retornos de carro que serán
          desinstalados **obligatorimente** en los clientes.

          Este campo se tiene en cuenta al ejecutar los comandos de cliente
          ``migasfree --update`` y ``migasfree-tags --set``


    * Default.

        * ``Default preinclude packages``: Campo de texto que especifica una
          lista de paquetes separados por espacios o por retornos de carro. Este
          campo sirve para instalar paquetes que configuran repositorios externos
          a migasfree. Un ejemplo de este tipo de paquetes lo tienes en el
          paquete `vx-repo-openshot`__.

          __ https://github.com/vitalinux/vx-repo-openshot

          La razón de la existencia de este campo es que después de intalar el
          repositorio externo es necesario obtener de nuevo los metadatos de
          los repositorios (apt-get update) a fin de que el cliente tenga acceso
          inmediatamente a los paquetes contenidos en el repositorio externo.

          Estos paquetes serán instalados a los clientes que tengan acceso al
          repositorio al ejecutar el comando ``migasfree-tags --set``.

        * ``Default include packages``: Campo de texto que especifica una lista de
          paquetes separados por espacios o por retornos de carro. Estos paquetes
          serán instalados a los clientes que tengan acceso al repositorio al
          ejecutar el comando ``migasfree-tags --set``.

        * ``Default exclude packages``: Campo de texto que especifica una lista de
          paquetes separados por espacios o por retornos de carro que serán
          desinstalados en los clientes que tengan acceso al repositorio al
          ejecutar el comando ``migasfree-tags --set``.

    * Atributtes.

        * ``Atributos``: Aquellos clientes que tengan un atributo que
          coincida con los asignados en este campo tendrán accesible el
          repositorio (a menos que otro atributo lo excluya).

        * ``Excludes``: Sirve para excluir Atributos de la lista de Atributos
          anterior.

          Por ejemplo si quieres liberar un paquete a toda la subred
          ``192.168.92.0`` menos al equipo ``PC13098`` puedes hacerlo asignando:
              * Atributos: ``NET-192.168.92.0/24``
              * Excludes:``HST-PC13098``


Calendarios
===========

Los calendarios te permiten programar sistemáticamente liberaciones en el tiempo
para unos determinados atributos previamente establecidos partiendo de la
fecha del Repositorio.

Por ejemplo, en AZLinux usamos distintos calendarios (LENTO, NORMAL, RAPIDO,
MUY RAPIDO) según la críticidad del cambio de software que se va a liberar
o de su urgencia. En estos calendarios asignamos días de demora para los
distintos servicios de nuestro ayuntamiento.

      .. code-block:: none

        CALENDARIO LENTO
            a los 0 días:  GRP-EQUIPOS DE TEST.
            a los 5 días:  CTX-SERVICIO DE PERSONAL
            a los 10 días: CTX-GESTION TRIBUTARIA
            a los 15 días: ALL-SYSTEMS

        CALENDARIO MUY RAPIDO
            a los 0 días: CTX-SERVICIO DE PERSONAL, CTX-GESTION TRIBUTARIA
            a los 2 dias: ALL-SYSTEMS

Es conveniente que en la última demora asignes, si procede, el atributo
``ALL-SYSTEMS``.

Cuando asignas un calendario a un repositorio podrás ver la temporalización
resultante en la columna ``línea temporal`` de
``Liberación-Empaquetado-Repositorios``.

Asignar un calendario a un repositorio no es obligatorio.

Esta programación de la liberación se utiliza fundamentalmente para conseguir:

    * No aplicar una liberación de golpe a muchos equipos, lo que puede provocar
      un consumo de tráfico de red intenso (imagina 1000 equipos actualizando
      libreoffice a la vez)

    * Liberar poco a poco los paquetes y así poder hacer comprobaciones más
      tranquilamente. Cualquier error en el empaquetado o bug en los fuentes
      del paquete puede ser mas manejable si ha afectado a pocos equipos y no
      a la totalidad.

Un determinado cliente tendrá acceso al repositorio si:

    * Tiene un atributo que coincide con alguno de los asignados en el repositorio
      y ya se ha cumplido la fecha del repositorio.

    * O existe un atributo coincidente con el calendario cuya fecha de repositorio
      mas demora se ha cumplido.

    * Siempre y cuando un atributo del cliente no coincida con  el campo ``Excludes``
      del repositorio.

Una manera en que puedes ver una estimación de la cantidad de equipos que un
calendario va haciendo efectivos los repositorios a lo largo de los días es
acceder a ``Auditoría-Estadísticas-Ordenadores previstos/demora``.

Campos de calendario
....................

    * ``Nombre``: Denomina al calendario.

    * ``Descripcion``: Describe el calendario.

    * Demoras: Es un conjunto de días (demoras) a los que se asignan atributos.

        * ``Demora``: Número de días desde la fecha del repositorio a los que los
          atributos asignados serán efectivos en el repositorio. No se tienen
          en cuenta ni sábados ni domingos.

        * ``Atributos`` Lista de atributos para una demora.


Repositorios internos vs externos
=================================

LLamamos repositorio interno al repositorio que controla el servidor migasfree.

Un repositorio externo es un repositorio configurado en los clientes y que no
apunta al servidor migasfree, Los repositorios que vienen por defecto configurados
en las Distribuiciones son un ejemplo. Otro sería los repositorios tipo ``ppa``

Si quieres tener un mayor control de tus sistemas, mi recomendación es que te
bajes todos los paquetes de los repositorios de tu distribución a una fecha y
luego los subas como ``conjunto de paquetes`` al servidor y creando un repositorio
al efecto.

De esta manera tendrás congelados a una fecha los repositorios de tu Distribución,
y podrás actualizar sólo el software que te interese. Si te decides por este
método obviamente tendrás que empaquetar un código que deshabilite los
repositorios externos en los clientes.

El proceso de la liberación
===========================

Las tareas que debe realizar un liberador son:

    * Controlar que no haya paquetes huérfanos, borrando los paquetes antiguos
      y creando los repositorios adecuados para los nuevos paquetes.

    * Decidir que calendario es conveniente aplicar a cada repositorio.

    * Cuando un repositorio ha terminado de liberarse (se ha completado su línea
      temporal) decidir que se debe hacer con sus paquetes.

      En AZLinux mayoritariamente, y para no tener muchos repositorios activos,
      estos paquetes los asignamos a otro repositorio que tiene asignado
      sólo el atributo ``ALL-SYSTEMS``. Los repositorios que nos han servido para
      liberar poco a poco los paquetes son desactivados (no los borramos) para
      mantener así la historia de lo que se ha ido haciendo.
