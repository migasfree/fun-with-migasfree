.. _`La configuración del sistema migasfree`:

======================================
La configuración del sistema migasfree
======================================

 .. epigraph::

   El hombre razonable se adapta al mundo; el irrazonable intenta adaptar el
   mundo a sí mismo. Así pues, el progreso depende del irrazonable.

   -- George Bernard Shaw


En los capítulos anteriores has aprendido a instalar el servidor y el cliente
migasfree, así como a crear paquetes. La creación de paquetes no es una tarea
trivial, no tanto por su construcción en sí, sino por el hecho de que son necesarios
amplios conocimientos de los sistemas operativos y de las aplicaciones.

En éste y en los siguientes tres capítulos, vas a aprender a adaptar y usar el
servidor migasfree.

.. _`Propiedades`:

Propiedades
===========

En migasfree, una ``propiedad`` es una característica de los equipos o
de los usuarios, y que nos servirá para desplegar los paquetes.

Como administrador de migasfree, una de las primeras tareas que debes realizar es
definir estas propiedades. Debes preguntarte en función de qué características
vas a realizar los despliegues. Por ejemplo, ¿te interesa desplegar los paquetes
por el HOSTNAME de los equipos? ¿y por subred? ¿Qué tal por el grupo al que
pertenece el usuario en el LDAP? ¿O por su contexto LDAP?

  .. note::

      En AZLinux, usamos principalmente el contexto LDAP al que pertenece el
      usuario para desplegar los cambios por los distintos servicios o
      departamentos de nuestro ayuntamiento, y en menor medida usamos también el
      CID.

Una ``propiedad`` es un código que se programa en un registro de la
base de datos de migasfree. Estas propiedades serán ejecutadas en cada uno de
los clientes migasfree y su valores de retorno serán devueltos al servidor como
``atributos``.

  .. note::

      El ``atributo`` es el valor concreto que toma una ``propiedad``
      al ser ejecutada en un equipo.

Veamos un ejemplo sencillo de todo esto con la propiedad HOSTNAME. Accede a
la web de tu servidor migasfree y ve a ``Configuración-Propiedades-HST``.
Verás en este registro el siguiente código escrito en ``python``.

  .. code-block:: none

    import platform
    print platform.node()

Si ejectutas ``python`` en una consola y escribes estas dos líneas verás
que python muestra, por la salida estándar, el nombre de tu equipo.

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

Esto es, en definitiva, lo que hace el cliente migasfree: obtiene del servidor la
propiedad ``HST`` (su código), la ejecuta y devuelve al servidor el resultado
como atributo (``HST-white``).

Podrías haber escrito la propiedad también en código ``bash`` simplemente
llamando al comando de linux ``hostname`` o escribiendo ``echo $HOSTNAME`` (el
resultado sería el mismo), pero utilizar código python nos permite, en este caso,
usar la misma ``propiedad`` también para plataformas Windows o Mac OS.


Campos de la Propiedad
----------------------

Observa cada uno de los campos de la Propiedad:

* **Prefijo**: Es una combinación de tres números o letras. Este prefijo se
  utiliza para agrupar e identificar los atributos.

* **Nombre**: Denomina a la propiedad.

* **Lenguaje de programación**: En el que está escrito el código de la
  propiedad.

* **Código**: Instrucciones a ejecutar en los clientes para obtener ``atributos``.

* **Habilitado**: Indica si está activa la propiedad. Si no está marcado, la
  propiedad no será ejecutada en los clientes.

* **Clase**: Hay cuatro tipos de clases y que nos permiten tratar el valor devuelto
  por la propiedad de diferentes maneras:

    * **Normal**. El valor devuelto por la propiedad viene con el siguiente formato:

      .. code-block:: none

          <valor>~<Descripción>

      o, simplemente, como:

      .. code-block:: none

          <valor>

    * **Lista**: El valor al ejecutar la propiedad en el cliente es una ``lista de
      atributos`` separados por una coma. Puedes ver un ejemplo en la propiedad
      ``PCI``. Su formato es:

      .. code-block:: none

          <valor>~<Descripción>, ...

    * **Agrega por la Derecha**: Permite añadir atributos de la siguiente manera:
      Si el valor devuelto por la propiedad es "CONTEXTO1.CONTEXTO2.MIEMPRESA", el
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

* **Automático**: Si este campo está marcado, los nuevos atributos serán añadidos
  automáticamente a la base de datos de migasfree. En caso contrario es el
  administrador de migasfree el responsable de añadir manualmente los atributos
  para esta propiedad. Se pueden añadir atributos manualmente accediendo a
  ``Datos-Atributos``.


.. _`Propiedades específicas`:

Propiedades específicas
-----------------------

Existen unas propiedades predefinidas que tienen unos objetivos muy concretos y
que no pueden ser eliminadas del sistema. Lo más característico de ellas es que
**no son ejecutadas en el cliente** sino en el servidor.

* **SET**: Esta propiedad tiene un atributo llamado ``SET-ALL SYSTEMS``. Todos
  los ordenadores tendrán este atributo sin excepción. Sirve para referirse a **todos** los ordenadores. Por ejemplo, si en un repositorio
  asignas este atributo, todos los ordenadores tendrán acceso a él. Es habitual
  usarlo también en la última demora de un calendario. Esta propiedad, además,
  se usa internamente para definir :ref:`Conjuntos de Atributos`.

* **CID**: Computer Identificator. Esta propiedad generará un atributo que
  es igual al campo ``id`` de la tabla ``computer`` de la Base de Datos de migasfree.

  Dicho atributo ``CID`` es único por cada ordenador y se utiliza en lugar de
  referirse al ``UUID`` de la placa base de un ordenador siendo **el más
  recomendado** para señalar a un ordenador en concreto (procesos como el
  :ref:`Reemplazo de ordenadores` tienen en cuenta este atributo).

  Por ejemplo, un atributo ``CID-572`` se correspondería con el
  ``UUID`` 5FD85780-9BC9-11E3-91B8-F0921CF3678D.

  El ajuste :ref:`MIGASFREE_COMPUTER_SEARCH_FIELDS` del servidor, permite
  configurar búsquedas por otros campos del ordenador a la hora de asignar un
  determinado ``CID`` en el servidor migasfree.

  Cuando un ordenador pasa a un estado ``Baja`` o a ``Disponible`` todos sus
  ``CID`` asignados en el sistema son eliminados. Ver campo ``estado`` de :ref:`Ordenadores`.

  El ``CID`` aparece por defecto en la etiqueta del ordenador que muestra el
  comando ``migasfree-label``.

.. _`Tipos de Etiquetas`:

Tipos de Etiquetas
==================

  Hasta ahora, has visto que una propiedad es un código que se
  ejecuta en el cliente para obtener un atributo automáticamente. Ahora bien,
  pueden existir casos en que no se puede obtener automáticamente estos
  atributos. Imagina que quieres "etiquetar" ciertos equipos según la
  funcionalidad que van a realizar (Tratamiento gráfico, administración, aula,
  etc.). Esto no es algo que, a priori, se pueda programar.

  En migasfree existe la posibilidad de crear estas etiquetas y asignarlas
  manualmente a los equipos tal y como harías con una etiqueta física que pegas
  a un ordenador.

  Una etiqueta no ejecutará ningún código en el cliente. Es el propio registro
  del ordenador en el servidor de migasfree quien lleva asignadas, manualmente,
  estas etiquetas. A todos los efectos, una etiqueta es un atributo más del
  sistema y, por tanto, te permitirá hacer el despliegue también en función de
  ellas.

  Por cada ``Configuración-Tipos de etiqueta``, existirá un conjunto de
  etiquetas que manualmente debes añadir en ``Datos-Etiquetas``. Una vez
  añadidas, puedes asignarlas a ``Datos-Ordenadores``. También puedes editar
  ``Datos-Etiquetas`` y asignarle un conjunto de ordenadores.

  Existe en el cliente el comando ``migasfree-tags`` que permite consultar y
  asignar etiquetas desde el propio cliente.

  Para consultar las etiquetas de un equipo ejecuta:

    .. code-block:: none

      migasfree-tags --get

  Para asignar etiquetas al equipo, seleccionando manualmente las etiquetas entre
  las disponibles en el sistema, ejecuta:

    .. code-block:: none

      migasfree-tags --set

  Para asignar determinadas etiquetas a un equipo, escribe las etiquetas separadas
  por espacios:

    .. code-block:: none

      migasfree-tags --set <ETIQUETA1> <ETIQUETA2> ...

  Para asignar etiquetas en el servidor migasfree pero que no se produzca
  **ningún cambio de paquetes** utiliza:

    .. code-block:: none

      migasfree-tags --communicate <ETIQUETA1> <ETIQUETA2> ...

  Para quitar todas las etiquetas de un equipo, ejecuta:

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
  crear la imagen ISO de los escritorios.

  .. note::

     En AZLinux, usamos ``migasfree-tags`` básicamente para, partiendo de una
     imagen ISO de Ubuntu, desintalar e instalar los paquetes que
     componen nuestro escritorio y crear una imagen del disco para clonar.

  .. note::

     En Vitalinux se emplean las etiquetas para cambiar fácilmente de "sabor".
     Cuando se quiere cambiar de sabor Vitalinux (Infantil, Primaria, Profes, ...),
     simplemente se eligen las etiquetas mediante el comando
     ``migasfree-tag --set``, produciéndose automáticamente la instalación y
     desinstalación de los paquetes correspondientes. Tambien se utiliza en la
     creación del DVDs, permitiendo hacer una ISO para cada sabor o conjunto de
     sabores.

Campos de Tipos de Etiqueta
---------------------------

* **Prefijo**: Es una combinación de tres números o letras. Este prefijo se
  utiliza para agrupar e identificar las etiquetas.

* **Nombre**: Denomina el tipo de etiqueta.

* **Habilitado**: Si no está marcado, las etiquetas de este tipo no serán
  funcionales.

* **Clase**: El funcionamiento es exactamente igual al campo de mismo nombre que
  tienen las Propiedades.

  Un valor muy útil que puede tomar este campo es el de ``agrega
  por la derecha``. Imagina que quieres agrupar los ordenadores por ubicación para
  liberar software por distintas zonas. Una forma de hacerlo es crear un ``Tipo de Etiqueta``
  llamada p.e. ``UBICACIÓN`` definada de clase ``agrega por la derecha``. Después,
  puedes crear las ``Etiquetas`` de tipo ``UBICACION`` p.e.:

    .. code-block:: none

      UBI-PLANTA-1.SEDE_CENTRAL.MADRID

  Cuando un equipo con esta etiqueta asignada se conecta al servidor, automáticamente
  el servidor interpretará que tiene no una, sino tres etiquetas:

    .. code-block:: none

      UBI-MADRID
      UBI-SEDE_CENTRAL.MADRID
      UBI-PLANTA-1.SEDE_CENTRAL.MADRID

  Con lo que finalmente podemos liberar software a todo ``MADRID``, a toda la
  sede central de Madrid, o solamente a la planta 1ª.


  .. note::

     Observa que el caracter de delimitación es el punto: ``.``


.. _`Conjuntos de Atributos`:

Conjuntos de Atributos
======================

En ocasiones puedes necesitar agrupar ``Atributos``.

Imagina que tienes muchos equipos a los que asignar una cierta ``Etiqueta`` y
que te resulta pesado tener que hacerlo uno a uno. Puedes entonces crear un
``Conjunto de Atributos``.

Supón que tienes subredes con un buen ancho de banda y otras subredes que no,
y que necesitas liberar software en función de esto. Podríamos crear dos
``Conjuntos de Atributos``:

    .. code-block:: none

      Conjunto 1:
            Nombre:                 RED LENTA
            Atributos asignados:    NET-192.168.1.0/24
                                    NET-192.168.8.0/24

      Conjunto 2:
            Nombre:                 RED RAPIDA
            Atributos asignados:    SET-ALL SYSTEMS
            Atributos excluidos:    SET-RED LENTA

De esta manera, cualquier equipo de las subredes 192.168.1.0/24 o 192.168.8.0/24,
al ejecutar ``migasfree -u``, se le asignará automáticamente un
``Atributo: SET-RED LENTA``. Al resto de equipos se le asignará el
``Atributo: SET-RED RAPIDA``.

Ahora ya podríamos crear ``Repositorios`` y asignarles dichos ``Atributos``.

Los ``Conjuntos de Atributos`` no ejecutan ningún código en el cliente, sino que
son evaluados en el servidor. Si un ordenador pertenece a un conjunto, se le asigna
un ``Atributo`` con el mismo nombre que el ``Conjunto de Atributos``.


Campos de Conjuntos de Atributos
--------------------------------

* **Nombre**: Denomina al conjunto.

* **Activo**: Indica si el conjunto será evaluado.

* **Atributos**: Lista de ``Atributos`` que formarán parte el conjunto.

* **Excluidos**: Lista de ``Atributos`` a excluir de conjunto.


.. _`Versiones`:

Versiones
=========

Migasfree puede trabajar con distintos Sistemas Operativos. Una ``versión``, en
migasfree, representa a un conjunto de ordenadores que comparten un mismo proyecto.

Por ejemplo, en el Ayto. de Zaragoza contamos con las siguientes ``versiones``:

    * AZLinux-1 (SLED 10.2) Se migró a AZLinux-2. (Ningún PC).

    * AZLinux-2 (OpenSUSE 11.2) Se migró a AZLinux-12 (Ningún PC).

    * AZLinux-12 (Ubuntu 12.04) En producción (1200 PC). En fase de migración a AZLinux-14

    * AZLinux-14 (Ubuntu 14.04) En producción (200 PC).

    * AZLinux-16 (Ubuntu 16.04). En desarrolo (Ningún PC).

    * ZA (Ubuntu 10.04 para escritorios tipo kioskos). Obsoleto.

    * WIN-XP (Windows XP). En producción (1800 PC).

    * AZW-10 (Windows 10). En desarrollo (Ningún PC).



Cada ordenador estará configurado en una única versión en un momento dado.
Cambios de versión en un ordenador crean en el sistema un registro de
``migración`` automáticamente. De esta manera, es posible conocer las diferentes
migraciones de S.O. que se han ido produciendo en los equipos y en qué momento se
han hecho efectivas. Puedes consultar las migraciones accediendo a
``Datos-Migraciones``.

Mediante el ajuste ``MIGASFREE_AUTOREGISTER`` se permite, o no, a los equipos
registrar automáticamente las versiones. Puedes consultarlo en
:ref:`Ajustes del servidor migasfree`.


Campos de la Versión
--------------------

* **Nombre**: Denomina a la versión.

* **Sistema de gestión de paquetes**: El P.M.S. que se utiliza en el S.O. de
  esta versión.

* **Actual line computer**: Es un equipo que sirve como referencia para comparar
  con el resto de equipos. Se debe elegir un equipo que represente la línea actual
  de la versión y que sea lo más "estándar" posible.

* **Actual line packages**: Lista ordenada de paquetes que componen la actual
  línea de la versión. Cuando se conecta al servidor el equipo asignado en el
  campo ``Actual line computer`` se actualiza automáticamente este campo.

  Este campo tiene relación con el campo ``Inventario de software`` de los
  ordenadores, ya que en este último sólo se mostrará la diferencia de paquetes
  repecto al ``Actual line computer``. De esta manera, se puede ver fácilmente
  que cambios se han producido respecto al ordenador asignado como referencia.

* **Autoregistrado**: Si está marcado, se permiten registrar ordenadores desde
  un cliente automáticamente. En este caso, sólo con que un equipo esté configurado
  con la versión será añadido automáticamente a la base datos.

  En caso contrario sólo se podrán registrar ordenadores mediante el uso de un
  usuario que cuente con los permisos adecuados para añadir ordenadores al
  sistema.

* **Plataforma**: a la que pertenece la versión.

Plataformas
===========

Las versiones se clasifican por plataformas. Las plataformas vienen establecidas
por la función python ``platform.system()`` y, por tanto, sus valores pueden ser:

    * Linux

    * Windows

    * (Otras)

Esta clasificación de las versiones te permite realizar consultas y estadísticas
en función de la plataforma.

Mediante el ajuste ``MIGASFREE_AUTOREGISTER`` se permite, o no, a los equipos
registrar automáticamente las plataformas. Puedes consultarlo en
:ref:`Ajustes del servidor migasfree`.


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

Estos usuarios son ficticios para realizar pruebas y conviene que
sean eliminados. Se recomienda crear los usuarios reales que usarán la web del
servidor migasfree asignándoles los grupos de usuarios correspondientes.

  .. note::

     Es importante que en un entorno de producción se deshabiliten los usuarios
     que no se vayan a utilizar o que, al menos, se les cambie la contraseña por
     motivos de seguridad.

Cambio de contraseña
--------------------
La contraseña puede ser cambiada por los usuarios pulsando en su nombre de usuario
y que aparece arriba a la derecha en todas las páginas web del servidor.

También puede ser modificada por otro usuario que tenga marcado el campo
``Es superusuario``, accediendo al registro del usuario en cuestión y modificando
directamente su campo ``Contaseña``.

Versión por defecto de un Usuario
---------------------------------

Los usuarios tienen un campo ``versión`` que sirve para filtrar registros. De
esta manera, cuando un usuario consulta los Repositorios p.e., sólo se muestran
los repositorios de la versión que tiene asignada.

Un usuario puede seleccionar su versión pulsando en su nombre de usuario y
luego ``Preferencias``

.. _`Comprobaciones`:

Comprobaciones
==============

Son un conjunto de comprobaciones que se realizan para alertar al usuario.
Pulsando en cada una de las ``Alertas`` puedes obtener más información. ver figura 8.1.

.. only:: not latex

   .. figure:: graphics/chapter08/estado.png
      :scale: 100
      :alt: Alertas del sistema.

      figura 8.1. Alertas del sistema.


.. only:: latex

   .. figure:: graphics/chapter08/estado.png
      :scale: 50
      :alt: Alertas del sistema..

      Alertas del sistema.

Cada ``Alerta`` viene programada en un registro de ``Comprobación``. Hay 8
comprobaciones predeterminadas:

    * ``Errors to check``. Cuando en un cliente migasfree se produce algún error,
      éste es enviado al servidor. Esta comprobación hace que se muestren estos
      errores. Una vez revisado o solucionado un error en el cliente debes editar
      el error en el servidor y marcar el campo ``comprobado``. Esto hará que
      ya no aparezca en la lista de errores a comprobar. Puedes también
      seleccionar un conjunto de errores en la lista de errores y en el desplegable
      de ``acción`` seleccionar ``La comprobación es correcta``.

    * ``Faults to check``. Cuando en un cliente migasfree se produce una
      falla, ésta es enviada al servidor. Esta comprobación hace que se muestren
      las fallas pendientes. La manera de proceder con las fallas es similar a
      la de los ``Errors to check``.

    * ``Notifications to check``. Son hechos que se han producido en el sistema y
      que son informados mediante esta comprobación. Un ejemplo de notificación
      es cuando un equipo da de alta una plataforma o una versión nueva en el
      sistema.

    * ``Package/Set orphan``. Comprueba si hay paquetes que no están asignados
      a ningún repositorio.

    * ``Computer updating now``. Cuando un equipo está ejecuando el cliente
      migasfree, éste va informando al servidor de lo que está haciendo mediante
      un texto que indica el proceso que está realizando. Cuando el cliente
      migasfree finaliza, envía al servidor un mensaje de texto vacío.
      Esta comprobación comprueba cuantos de estos mensajes se han recibido.

    * ``Computer delayed``. Si pasa un determinado tiempo desde que se recibió
      el último mensaje del cliente, es muy posible que algo ha ido mal en el
      cliente. Quizás perdió la conexión, o el usuario apagó el equipo en medio
      de la ejecución del cliente migasfree, o quizás ha habido algún error. Esta
      comprobación permite detectar estos casos. La cantidad de tiempo viene
      establecida por defecto en 30 minutos y puede ser modificado mediante el ajuste
      ``MIGASFREE_SECONDS_MESSAGE_ALERT`` de los :ref:`Ajustes del servidor migasfree`.

    * ``Server Messages``. Es similar a ``Computer updating now`` pero para los
      mensajes que se producen en el servidor.

    * ``Server Messages Delayed``. Similar a ``Computer delayed`` pero para los
      mensajes que se producen en el servidor.

Campos de Comprobación
----------------------

    * **Nombre**: Denomina la comprobación

    * **Descripción**: Sirve para describir en detalle la comprobación.

    * **Código**: Instrucciones escritas en ``Django`` para realizar la comprobación.
      El servidor interpretará las siguientes variables que deben ser asignadas
      en este campo.

          ``result``. Debe ser un numero. Un valor de 0 indica que no hay nada
          que mostrar en la alerta.

          ``alert``. Es el tipo de alerta. Puede ser uno de estos tres valores:
          'info', 'warning' ó 'danger'. Se representan con los colores azul, naranja o rojo.
          El valor por defecto es 'info'.

          ``url``. Es el link al que accederá el usuario cuando pulse en la
          alerta.

          ``msg``. Es el texto a mostrar en la alerta.

          ``target``. Puede ser "computer" o "server" para indicar que la
          comprobación está relacionada con el equipo cliente o con el servidor.
          Se representa con el icono de un ordenador o con el de una nube.

      Mira este codigo de ejemplo, el de ``Errors to check``:

          .. code-block:: none

            from migasfree.server.models import Error
            result = Error.objects.filter(checked__exact=0).count()
            url = '/admin/server/error/?checked__exact=0'
            icon = 'error.png'
            msg = 'Errors to check'
            target = 'computer'

      Lo primero que hacemos en importar el modelo Error. Depués obtenemos el
      número de registros de errores que que no se han comprobado y lo asignamos
      a la variable ``result``. A continuación, vamos asignando los valores a cada
      una de las variables.


    * **Habilitado**. Activa o desactiva la comprobación.

Las ``alertas`` proporcionan al usuario una vista general de la situación actual del
sistema, dirigiendo su actuación a lo relevante.

El objetivo en todo momento debería ser mantener el sistema con 0 alertas. Esto
indicaría que se han revisado los errores, se han comprobado las fallas,
no hay paquetes huérfanos, etc.

.. _`Fallas`:

Fallas
======

Una falla es un hecho negativo que se produce en un equipo cliente. Por
ejemplo que un equipo se quede con poco espacio en la partición de sistema, es
algo a lo que se debe prestar atención y ser solucionado antes de que sea tarde.

Migasfree mediante las fallas permite lanzar código en el cliente con este
objetivo. Fíjate que las posibilidades son inmensas y que te permite ser
muy proactivo.

En definitiva, una falla es un código que se ejecuta en el cliente. Si el código
escribe algo por la salida estándar, ésta será enviada al servidor como ``Falla``.
El servidor entonces añadirá un registro de ``Falla``, apareciendo en las
``Alertas`` de los usuarios de migasfree.

Campos de Definición de Falla
-----------------------------

    * **Nombre**: Denomina a la falla.

    * **Descripción**: Para detallar lo que hace la falla.

    * **Habilitado**: Activa o desactiva la falla.

    * **Lenguaje de programación**: Especifica en qué lenguaje está escrito el
      ``código``. Mi recomendación es que programes en la medida de lo posible
      en **python**.

    * **Código**: Instrucciones que detectan alguna falla en los equipos y que
      debe poner en la salida estándar un texto que indique la falla producida.
      Puede serte útil en algunos casos poner también el procedimiento a seguir.

    * **Attributes**: Permite asignar a que equipos cliente será efectiva
      la falla. Por ejemplo si escribes el código en bash, deberías asignar la
      falla sólo a los equipos con plataforma Linux ``PLT-Linux``,
      ya que plataformas Windows no serán capaces de ejecutar bash.
      También te puede interesar programar una falla sólo para obtener
      información de un equipo o de un grupo de equipos.

    * **Users**: Sirve para asignar usuarios de migasfree a los que les
      aparecerán las fallas de este tipo cuando se accede desde las ``Alertas``
      (sólo se muestran las que están pendientes de comprobar por el usuario autenticado).

Si una definición de falla no tiene asignado ningún usuario, las fallas
que se produzcan aparecerán a cualquier usuario autenticado.

  .. note::

      Poder ejecutar código en los clientes proporciona una gran potencia para
      realizar cualquier cosa. Usa esta capacidad con responsabilidad y sé
      meticuloso en las comprobaciones antes de activar cualquier falla.

.. _`Consultas`:

Consultas
=========

Migasfree incorpora un sistema para crear consultas parametrizables sencillas.

Cada consulta se programa en un registro y podrá ser ejecutada accediendo a
``Consultas``

Hay una pocas consultas ya predefinidas, pero puedes programar nuevas o adaptar
las que ya existen.

Campos de consulta
------------------

    * **Nombre**: Denomina la consulta.

    * **Descripción**: Describe la consulta.

    * **Código**: Instrucción en Django de la consulta. Mediante la asignación
      de una variables predeterminadas el servidor podrá crear la consulta.

      Las variables en concreto son:

        * **QuerySet**: Conjunto de registros de la consulta.

        * **fields**: Lista de los campos del QuerySet que se quieren mostrar.

        * **titles**: Lista de los titulos de los campos que se quieren mostrar.

        * **version**: Sirve para obtener la version del usuario y poder hacer
          filtros cuando se requiera.

    * **Parámetros**: Permite la petición de parámetros de consulta. Se debe
      crear una función que se llame ``form_params`` y que devuelva una clase
      que herede de ``ParametersForm``

En fin, creo que lo mejor es que veas un ejemplo para comprender la programación de
consultas: hay una que muestra todas las consultas, se llama ``QUERIES``:

    **Parametros**: Aquí se programa un formulario de parametros que pedirá
    el paŕametro ``id``.

    .. code-block:: none

      def form_params():
          from migasfree.server.forms import ParametersForm
          class myForm(ParametersForm):
              id = forms.CharField()
          return myForm

    **Código**: Programamos que si el parámetro ``id`` que ha introducido el usuario
    es una cadena vacía, la variable ``query`` sea igual a todos los regitros de
    la tabla ``Consulta``.
    En caso de que el usuario introduzca un valor filtramos las ``Consultas``
    por ``parameters['id']``.

    .. code-block:: none

      if parameters['id'] == '':
          query = Query.objects.all()
      else:
          query = Query.objects.filter(id=parameters['id'])
      fields = ('id', 'name', 'description', 'code', 'parameters')

  .. note::

     Para realizar consultas necesitarás conocer un poco los `QuerySet`__ de
     Django y la ``Documentación del modelo de datos``. Esta última la tienes
     disponible al final de todas las páginas del servidor pulsando sobre el
     icono de información .

__ https://docs.djangoproject.com/en/dev/ref/models/querysets/


Errores autocomprobables
========================

Por defecto, los errores producidos por el P.M.S., se añaden al sistema como no
comprobados. Ahora bien, en ocasiones puede resultar tedioso tener que marcar como
comprobados uno a uno ciertos errores que más que errores son "alertas".

Para automatizar esta tarea puedes crear un ``error autocomprobable``. Simplemente añade
un registro con el `patrón de búsqueda`__ deseado y los errores que coincidan son ese
patrón se marcarán automáticamente como comprobados.

__ https://docs.python.org/2/library/re.html#module-re

Por ejemplo si quisieras que todos los errores que llegan del tipo:

    .. code-block:: none

      2014-10-03 10:44:47
      Error: Generic error
      Info: Curl error: Couldn't resolve host 'myserver'

se autocomprobaran, podrías emplear el siguiente patrón:

    .. code-block:: none

      .*\sError: Generic error\sInfo: Curl error: Couldn't resolve host 'myserver'
