======================================
La configuración del sistema migasfree
======================================

 .. epigraph::

   El hombre razonable se adapta al mundo; el irrazonable intenta adaptar el
   mundo a si mismo. Así pues, el progreso depende del irrazonable.

   George Bernard Shaw


En los capítulos anteriores has aprendido a instalar el servidor y el cliente
migasfree, así como a crear paquetes. La creación de paquetes no es una tarea
trivial, no tanto por su construcción en sí sino por el hecho de que son necesarios
amplios conocimientos de los sistemas operativos y de las aplicaciones.

En éste y en los siguientes tres capítulos vas a aprender a adaptar y usar el
servidor migasfree.


Propiedades
===========

En migasfree una ``propiedad`` es una característica de los equipos o
de los usuarios, y que nos servirá para desplegar los paquetes.

Como administrador de migasfree una de las primeras tareas que debes realizar es
definir estas propiedades. Debes preguntarte en función de qué características
vas a realizar los despliegues. Por ejemplo, ¿te interesa desplegar los paquetes
por el HOSTNAME de los equipos? ¿y por subred? ¿Que tal por el grupo al que
pertenece el usuario en el LDAP? ¿Y por su contexto LDAP?.

  .. note::

      En AZLinux usamos principalmente el contexto LDAP al que pertenece el
      usuario para desplegar los cambios por los distintos servicios o
      departamentos de nuestro ayuntamiento, y en menor medida usamos también el
      HOSTNAME de los equipos.

Una ``propiedad`` es un código que se programa en un registro de la
base de datos de migasfree. Estas propiedades serán ejecutadas en cada uno de
los clientes migasfree y su valores de retorno serán devueltos al servidor como
``atributos``.

  .. note::

      El ``atributo`` es el valor concreto que toma una ``propiedad``
      al ser ejecutada en un equipo.

Veamos un ejemplo sencillo de todo esto con la propiedad HOSTNAME. Accede a
la web de tu servidor migasfree y ve a ``Configuracion-General-Propiedades-HST``.
Verás en este registro el siguiente código escrito en python.

  .. code-block:: none

    import platform
    print platform.node()

Si ejectutas ``python`` en una consola y escribes estas dos líneas verás
que python muestra por la salida estandard el nombre de tu equipo.

  .. code-block:: none

    $ python
    Python 2.7.3 (default, Apr 10 2013, 05:46:21)
    [GCC 4.6.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import platform
    >>> print platform.node()
    white

En mi caso me ha devuelto ``white``, que es el nombre de mi portátil. ¿A que
no aciertas de qué color es?

Esto es en definitiva lo que hace el cliente migasfree: obtiene del servidor la
propiedad ``HST`` (su código), la ejecuta y devuelve al servidor el resultado
como atributo ``HST-white``.

Podrías haber escrito la propiedad tambien en código ``bash`` simplemente
llamando al comando de linux ``hostname`` o escribiendo ``echo $HOSTNAME`` (el
resultado sería el mismo), pero utilizar código python nos permite usar la misma
``propiedad`` también para plataformas Windows ó MAC.


Campos de la Propiedad.
-----------------------

Observa cada uno de los campos de la Propiedad:

* **Prefijo**: Es una combinación de tres números o letras. Este prefijo se
  utiliza para agrupar e identificar los atributos.

* **Nombre**: Denomina a la propiedad.

* **lenguaje de programación**: En el que está escrito el código de la
  propiedad.

* **Código**: Instrucciones a ejecutar en los clientes para obtener ``atributos``.

* **Habilitado**: Indica si está activa la propiedad. Si no está marcado la
  propiedad no será ejecutada en los clientes.

* **Clase**: Hay cuatro tipos de clases y que nos permiten tratar el valor devuelto
  por la propiedad de diferentes maneras:

    * **Normal**. El valor devuelto por la propiedad viene con el siguiente formato:

      .. code-block:: none

          <valor>~<Descripción>

      ó simplemente como:

      .. code-block:: none

          <valor>

    * **Lista**: El valor al ejecutar la propiedad en el cliente es una ``lista de
      atributos`` separados por una coma. Puedes ver un ejemplo en la propiedad
      ``PCI``. Su formato es:

      .. code-block:: none

          <valor>~<Descripción>, ...

    * **Agrega por la Derecha**: Permite añadir atributos de la siguiente manera:
      Si el valor devuelto por la propiedad es "CONTEXTO1.CONTEXTO2.MIEMPRESA" el
      servidor interpreta que el equipo tiene estos tres atributos:

      * MIEMPRESA

      * CONTEXTO2.MIEMPRESA

      * CONTEXTO1.CONTEXTO2.MIEMPRESA

      Se utiliza esta clase para crear atributos relacionados con LDAP.

    * **Agrega por la Izquierda**. Lo mismo que el anterior pero agregando por la
      izquierda.

      * CONTEXTO1

      * CONTEXTO1.CONTEXTO2

      * CONTEXTO1.CONTEXTO2.MIEMPRESA

* **Automático**: Si este campo está marcado los nuevos atributos será añadidos
  automáticamente a la base de datos de migasfree. En caso contrario es el
  administrador de migasfree el responsable de añadir manualmente los atributos
  para esta propiedad. Se pueden añadir atributos manualmente accediendo a
  ``Auditoría-Datos-Atributos``.

* **Etiqueta**: Hasta ahora has visto que una propiedad es un código que se
  ejecuta en el cliente para obtener un atributo automáticamente. Ahora bien,
  pueden existir casos en que no se puede obtener automáticamente estos
  atributos. Imagina que quieres "etiquetar" ciertos equipos según la
  funcionalidad que van a realizar (Tratamiento gráfico, administración, etc).
  Esto no es algo que a priori se pueda programar.

  En migasfree existe la posibilidad de crear estas etiquetas y asignarlas
  manualmente a los equipos tal y como harías con una etiqueta física que pegas
  a un ordenador.

  Una propiedad de tipo etiqueta no ejecutará ningún código en el
  cliente. Es el propio registro del ordenador en el servidor de migasfree
  quien lleva asignada manualmente estas etiquetas. A todos los efectos
  una etiqueta es un atributo más del sistema y por tanto te permitirá hacer
  el despliegue tambien en función de ellas.


  La creación de etiquetas requiere que se defina primero una propiedad con el
  campo etiqueta marcado. A continuación se añaden los atributos (etiquetas)
  manualmente desde ``Auditoria-Datos-Atributos`` asignando a cada atributo dicha
  propiedad.

  Una vez añadidos estos atributos ya pueden ser asignados en
  ``Auditoria-Datos-Ordenadores`` en el campo ``etiquetas`` de cada ordenador.

  Existe en el cliente el comando ``migasfree-tags`` que permite consultar y
  asignar etiquetas desde el propio cliente.

  Para consultar las etiquetas de un equipo ejecuta:

    .. code-block:: none

      migasfree-tags --get

  Para asignar etiquetas al equipo, seleccionando manualmente las etiquetas entre
  las disponibles en el sistema, ejecuta:

    .. code-block:: none

      migasfree-tags --set


  Para asignar determinadas etiquetas a un equipo escribe las etiquetas separadas
  por espacios:

    .. code-block:: none

      migasfree-tags --set <ETIQUETA1> <ETIQUETA2> ...

  Para quitar todas las etiquetas de un equipo ejecuta:

    .. code-block:: none

      migasfree-tags --set ""

  Las etiquetas están relacionadas con los campos de los repositorios:

      * default preinclude packages

      * default include packages

      * default exclude packages

  ya que al ejecutar el comando ``migasfre-tags --set`` se instalarán los
  paquetes definidos en ``preinclude`` e ``include`` y se desinstalarán los
  paquetes definidos en el campo ``exclude``, siempre y cuando los atributos
  asignados al repositorio coincidan con los del equipo. Esto se utiliza para
  crear la imagen iso de los escritorios.

  .. note::

     En AZlinux usamos ``migasfree-tags`` básicamente para, partiendo de una
     imagen iso de Ubuntu 12.04, desintalar e instalar los paquetes que
     componen nuestro escritorio y crear una imagen del disco para clonar.

  .. note::

     En Vitalinux se emplean las etiquetas para cambiar fácilmente de "sabor".
     Cuando se quiere cambiar de sabor Vitalinux (Infantil, Primaria, Profes, ...),
     simplemente se eligen las etiquetas mediante el comando
     ``migasfree-tag --set``, produciéndose automáticamente la instalación y
     desinstalación de los paquetes correspondientes. Tambien se utiliza en la
     creación del DVDs, permitiendo hacer una iso para cada sabor o conjunto de
     sabores.

Versiones
=========

Migasfree puede trabajar con distintos Sistemas Operativos. Una ``version`` en
migasfree representa a un conjunto de ordenadores que comparten un mismo S.O.

Por ejemplo, en AZLinux tenemos actualmente 5 versiones establecidas:

    * AZLinux-1 (SLED 10.2)

    * AZLinux-2 (OpenSUSE 11.2)

    * AZLinux-12 (Ubuntu 12.04)

    * WIN-XP (Windows XP)

    * ZA (Ubuntu 10.04 para escritorios tipo kioskos)

Cada ordenador estará configurado en una única versión en un momento dado.
Cambios de versión en un ordenador crean en el sistema un registro de
``migración`` automáticamente. De esta manera es posible conocer las diferentes
migraciones de S.O. que se han ido produciendo en los equipos y en qué momento se
han hecho efectivas. Puedes consultar las migraciones accediendo a
``Auditoría-Datos-Migraciones``.

Mediante el ajuste ``MIGASFREE_AUTOREGISTER`` se permite, o no, a los equipos
registrar automáticamente las versiones. Puedes consultarlo en
:ref:`Ajustes del servidor migasfree`.


Campos de la Versión.
---------------------

* **Nombre**: Denomina a la versión.

* **Sistema de gestión de paquetes**: El P.M.S. que se utiliza en el S.O. de
  esta versión.

* **Actual line computer**: Es un equipo que sirve como referencia para comparar
  con el resto de equipos. Se debe elegir un equipo que represente la línea actual
  de la versión y que sea lo más "estandar" posible.

* **Actual line packages**: Lista ordenada de paquetes que componen la actual
  línea de la versión. Cuando se conecta al servidor el equipo asignado en el
  campo ``Actual line computer`` se actualiza automáticamente este campo.

  Este campo tiene relación con el campo ``Inventario de software`` de los
  ordenadores, ya que en este último sólo se mostrará la diferencia de paquetes
  repecto al ``Actual line computer``. De esta manera se puede ver fácilmente
  que cambios se han producido respecto al ordenador asignado como de referencia.

* **Autoregistrado**: Si está marcado se permiten registrar ordenadores desde
  un cliente automáticamente. En este caso, sólo con que un equipo esté configurado
  con la versión será añadido automáticamente a la base datos.

  En caso contrario sólo se podrán registrar ordenadores mediante el uso de un
  usuario que cuente con los permisos adecuados para añadir ordenadores al
  sistema.

* **Plataforma**: a la que pertenece la versión.

Plataformas
===========

Las versiones se clasifican por plataformas. Las plataformas vienen establecidas
por la función python ``platform.system()`` y por tanto sus valores pueden ser:

    * Linux

    * Windows

    * (Otras)

Esta clasificación de las versiones te permite realizar consultas y estadísticas
en función de la plataforma.

Mediante el ajuste ``MIGASFREE_AUTOREGISTER`` se permite, o no, a los equipos
registrar automáticamente las plataformas. Puedes consultarlo en
:ref:`Ajustes del servidor migasfree`.


.. _`Usuarios Migasfree`:

Usuarios Migasfree
==================

En migasfree existen dos tipos de usuarios, los usuarios que administran
migasfree y los usuarios que utilizan los ordenadores. Este apartado se refiere
a los primeros.

Cuando se genera la base de datos de migasfree se crean 7 grupos de usuarios y
8 usuarios predeterminados:

Grupos de Usuarios
------------------

En función de las tareas que los usuarios de administración de migasfree
pueden realizar, se establecen los siguientes grupos de usuarios.



    * ``Configurator`` con permisos de lectura/escritura a:

        * Propiedades

        * Versiones

        * P.M.S.

        * Plataformas

        * Comprobaciones

        * Definicion de fallas

        * Mensajes

        * Actualizaciones

        * Mensajes del servidor

        * Migraciones

        * Notificaciones

    * ``Computer Checker`` tiene permisos de lectura/escritura a:

        * Errores

        * Fallas

        * Mensajes

        * Actualizaciones

    * ``Liberator``. Permisos de lectura/escritura a:

        * Repositorios

        * Calendarios

    * ``Packager`` cuenta con permisos de lectura/escritura a:

        * Paquetes

        * Almacenes

    * ``Query``. Permisos de lectura/escritura a:

        * Consultas

    * ``Device installer`` cuenta con permisos de lectura/escritura a:

        * Dispositivos

    * ``Reader``. Permisos de sólo lectura a todas las tablas.

Usuarios
--------

    * ``admin``. Tiene permisos de lectura/escritura a todas las tablas.

    * ``packager``. Pertenece a los grupos ``Reader`` y ``Packager``.

    * ``configurator``. Pertenece a los grupos ``Reader`` y ``Configurator``.

    * ``installer``. Pertenece a los grupos ``Reader`` y ``Device installer``.

    * ``query``. Pertenece a los grupos ``Reader`` y ``Query``.

    * ``liberator``. Pertenece a los grupos ``Reader`` y ``Liberator``.

    * ``checker``. Pertenece a los grupos ``Reader`` y ``Computer Checker``.

    * ``reader``. Pertenece  al grupo ``Reader``.

Estos usuarios tienen por defecto como contaseña su nombre, es decir, la
contraseña de admin es admin, y lo mismo es aplicable al resto de usuarios.

Estos usuarios, son ficticios para realizar pruebas y conviene que
sean eliminados. Se recomienda crear los usuarios reales que usarán la web del
servidor migasfree asignandoles los grupos de usuarios correspondientes.

  .. note::

     Es importante que en un entorno de producción se deshabiliten los usuarios
     que no se vayan a utilizar o que al menos se les cambie la contraseña por
     motivos de seguridad.

Cambio de contraseña
--------------------
La contraseña puede ser cambiada por los usuarios pulsando en su nombre de usuario
y que aparece arriba a la derecha en todas las páginas web del servidor.

También puede ser modificada por otro usuario que tenga marcado el campo
``Es superusuario``, accediendo al registro del usuario en cuestión y modificando
directamente su campo ``Contaseña``.

Version por defecto de un Usuario
---------------------------------

Los usuarios tienen un campo ``version`` que sirve para filtrar registros. De
esta manera cuando un usuario consulta los Repositorios p.e., solo se muestran
los repositorios de la versión que tiene asignada.

Para cambiar la ``version`` de un usuario hay que acceder a ``Liberacion-Escoger version``.


Consultas
=========

Estado general del sistema
==========================

Comprobaciones
--------------

Fallas
------

