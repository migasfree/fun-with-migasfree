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


Creación de etiquetas
---------------------



migasfree-tags


Versiones
=========

Plataformas
===========

.. _`Usuarios Migasfree`:

Usuarios Migasfree
==================

Consultas
=========

Estado general del sistema
==========================

Comprobaciones
--------------

Fallas
------

