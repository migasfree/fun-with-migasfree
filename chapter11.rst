============
La Auditoría
============

 .. epigraph::

   Nuestro conocimiento es necesariamente finito, mientras que nuestra
   ignorancia es necesariamente infinita.

   -- Karl Raimund Popper

Una vez que liberas los paquetes y que los equipos se van actualizando, llega el
momento de que veas, de manera centralizada, toda la información que se ha ido
generando a consecuencia del proceso de actualización.

Esto es lo que te vas a encontrar en este capítulo.

Alertas
=======

Muestra en lo que debe actuar el administrador para tener un sistema lo
más íntegro posible. Ya lo viste en apartado :ref:`Comprobaciones` del capítulo
:ref:`La configuración del sistema migasfree`.


.. _`Ordenadores`:

Ordenadores
===========

Accediendo a ``Datos-Ordenadores``, verás la lista de ordenadores que
se han registrado en el servidor.

Puedes acceder al ``Hardware`` de un equipo desde la última columna de la lista
de ordenadores.

También puedes acceder a los **datos** que están **relacionados** con un equipo
determinado, mediante el desplegable que hay a la derecha del identificador del equipo.
Así, fácilmente podrías ver la cantidad de errores que ha habido en un equipo, sus fallas,
migraciones, actualizaciones, ... Además, en este
menú desplegable del ordenador, te vas a encontrar con otras opciones interesantes:

* **Sucesos**: Sobre un calendario, desde la fecha de entrada del equipo en el servidor,
  se muestra la cantidad diaria de actualizaciones, errores, fallas, migraciones y
  registros de estado. A más cantidad diaria de sucesos, el color es más oscuro.

* **Simular sincronización**: Te  permite simular lo que entregaría el servidor
  al cliente cuando éste último ejecuta ``migasfree -u``. De esta manera, y basándonos
  en el último ``login`` del ordenador, puedes ver qué repositorios se configurarían en el
  cliente, qué paquetes se instalarían o eliminarían o qué fallas se ejecutarían.

* **Hardware**: Nos da acceso al hardware del equipo.


Campos de Ordenador
-------------------

    * **Estado**: Un ordenador puede tener uno de estos seis estados: ``Asignado``,
      ``Reservado``, ``Desconocido``, ``Disponible``, ``En reparación`` y finalmente
      ``Baja``.

        Estos estados los clasificamos de la siguiente manera:

        * **ALTA**: Son todos los ordenadores que no tienen el estado ``Baja`` y
          los dividimos en productivos e improductivos.

            * **PRODUCTIVOS**: Conjunto de ordenadores en uso. Los diferentes
              estados dentro de esta categoría son:

                * ``Asignado``. Es el estado por defecto e indica que el ordenador
                  está siendo usado para el propósito propio de tu organización.

                * ``Reservado``. Indica que el ordenador se utiliza para un uso
                  especial, por ejemplo para pruebas.

                * ``Desconocido``. Cualquier otro uso.

            * **IMPRODUCTIVOS**: Ordenadores que no están siendo utilizados
              y que podrán utilizarse en el futuro. Dentro de los improductivos
              encontramos los siguientes estados:

                * ``Disponible``. El ordenador está libre y listo para pasar a un
                  estado productivo inmediatamente.

                      .. note::

                        Cuando un ordenador pasa a estado ``Disponible``, se
                        elimina la asignación de todas sus etiquetas y además,
                        si el ``CID`` del ordenador se ha asignado en algún
                        Repositorio, Conjunto de Atributos, Dispositivo Lógico,
                        Definición de Falla y/o Demora de Calendario también
                        será eliminada dicha asignación automáticamente. Esto
                        evita configuraciones inapropiadas derivadas de cambios
                        de equipos (si no se hiciera de esta manera, el uso
                        antiguo que se le haya dado a un ordenador podría influir
                        en su uso futuro).

                * ``En reparación``. El ordenador está siendo reparado.

        * **BAJA**: Tienen el estado ``Baja``. Se indica con este estado que el
          ordenador no se va utilizar nunca más debido a rotura, robo, venta o
          por cualquier otro motivo.

              .. note::

                Cuando un ordenador pasa a estado ``Baja``, se elimina la
                asignación de todas sus etiquetas y además, si el ``CID`` del
                ordenador se ha asignado en algún Repositorio, Conjunto de
                Atributos, Dispositivo Lógico, Definición de Falla y/o Demora
                de Calendario también será eliminada dicha asignación
                automáticamente.

        Puedes consultar más información sobre los ``CID`` en las :ref:`Propiedades específicas`.

        Puedes asignar un estado por defecto a los nuevos ordenadores con el
        ajuste de servidor: :ref:`MIGASFREE_DEFAULT_COMPUTER_STATUS`

    * **Nombre**: Es el nombre del equipo o el especificado en el
      ajuste ``Computer_Name`` de los :ref:`Ajustes del cliente migasfree`

    * **Versión**: La versíon migasfree del ordenador.

    * **Fecha de alta**: Fecha de alta del ordenador en migasfree.

    * **Última actualización**: Fecha en la que se finalizó por última vez la
      actualización del cliente migasfree.

    * **IP**: La dirección IP del equipo en el momento de la actualización.

    * **Actualización hardware**: Fecha de la última actualización hardware.

    * **Product**: Nombre del ordenador incluido en la placa base.
      Por ejemplo ``HP ProDesk 600 G1 SFF (C8T89AV)``

    * **Uuid**: Es el identificador único universal de la placa base del equipo.

          .. note::

            El cliente de migasfree es el encargado de proporcionar este UUID. En
            caso de no poder obtenerlo porque el fabricante de la placa
            base no lo ha asignado o por cualquier otro motivo, el cliente
            proporciona un UUID basado en la MAC de la primera tarjeta de red
            que encuentre.

    * **Machine**: Indica si es una máquina física o virtual.

    * **CPU**: Nombre del microprocesador. Ejemplo: ``Intel Core i5-4590 3.30GHz``

    * **RAM**: Cantidad de memoria RAM.

    * **Almacenamiento**: Cantidad de almacenamiento en disco.

    * **Discos**: Numero de discos.

    * **MAC address**: Direcciones MAC.

    * **Inventario de software**: Diferencia actual entre el conjunto de paquetes del
      ordenador de referencia y el ordenador en cuestión. Ver en
      :ref:`Versiones` los campos de version:
      ``Actual line computer`` y ``Actual line packages``

    * **Historial de software**: Registro de los paquetes instalados y
      desinstalados según se van produciendo en el tiempo.

    * **Etiquetas**: Lista de Etiquetas asignadas actualmente al ordenador.
      Para una explicación del funcionamiento de las etiquetas mira los
      :ref:`Tipos de Etiquetas`.

Usuarios
========

A medida que el cliente de migasfree va ejecutándose en los equipos, el servidor
va añadiendo los usuarios que se han autenticado en el entorno gráfico.

Puedes ver la lista de usuarios en ``Datos-Usuarios``

Campos de Usuario
-----------------

    * **Nombre**: Nombre de la cuenta de usuario para acceder al equipo.

    * **Nombre Completo**: Nombre y apellidos del usuario.

Logins
======

Cuando se ejecuta ``migasfree --update`` se crea un registro de ``Login`` en
el servidor.

  .. note::

    Migasfree sólo lleva por cada equipo el **último login**.

Campos de Login
---------------

    * **Fecha**: Fecha y hora de la ejecución de ``migasfree --update`` en el
      equipo

    * **Usuario**: Usuario en el entorno gráfico cuando se ejecutó el cliente
      migasfree.

    * **Ordenador**: El equipo al que hace referencia el login.

    * **Atributos**: Lista de ``Atributos`` que se han obtenido como resultado de
      ejecutar la ``Propiedades`` en el ordenador cliente en el proceso de
      actualización.

Errores
=======

Conforme se vayan produciendo errores en los clientes, irán llegando al servidor
y serán mostrados en ``Alertas``.

Campos de error
---------------

    * **Ordenador**: Equipo en el que se ha producido el error.

    * **Fecha**: Fecha y hora en que se produjo el error.

    * **Error**: Mensaje que describe el error. Generalmente corresponde a
      la salida de error del front-end del P.M.S.

    * **Comprobado**: Campo que se marcará manualmente cuando se ha comprobado y
      solucionado el error.

    * **Versión**: Es la versión que tenía el equipo cuando se produjo el error.

Fallas
======

Ya viste el concepto de :ref:`Fallas` y cómo se pueden programar en el capítulo
:ref:`La configuración del sistema migasfree`, así que no me repitiré.

Lo mismo que ocurre con los errores, conforme las fallas se vayan detectando en
los clientes, irán apareciendo en el ``Alertas``.

Campos de falla
---------------

    * **Ordenador**: Equipo en el que se ha producido.

    * **Definición de falla:**: Tipo de Falla. Hace referencia al código que
      ha generado la falla.

    * **Fecha**: Fecha y hora en que se produjo la falla.

    * **Texto**: Mensaje que describe la falla. Corresponde a
      la salida standard del codigo de la ``Definición de la falla``.

    * **Comprobado**: Campo que se marcará manualmente cuando se ha comprobado y
      solucionado la falla.

    * **Versión**: Es la versión que tenía el equipo cuando se produjo la falla.

Atributos
=========

A medida que se vayan actualizando los equipos, el servidor migasfree irá
añadiendo los atributos enviados por los clientes con objeto de que puedas
liberar paquetes en función de estos atributos.

Campos de Atributo
------------------

    * **Propiedad de atributo**: Propiedad a la que hace referencia el atributo.

    * **Valor**: Identifica el atributo.

    * **Descripción**: Describe el atributo.

Una explicación del funcionamiento de los atributos la puedes obtener en
el apartado :ref:`Propiedades` de :ref:`La configuración del sistema migasfree`.

Etiquetas
=========

Manualmente podrás añadir etiquetas y asignarlas a ordenadores para
liberar software en función de éstas.

El funcionamiento de las etiquetas ya lo hemos visto en los
:ref:`Tipos de Etiquetas`.

Campos de Etiqueta
------------------

    * **Propiedad**: Hace referencia al tipo de etiqueta.

    * **Valor**: Identifica a la etiqueta.

    * **Descripción**: Describe la etiqueta.

    * **Ordenadores**: Permite asignar ordenadores a la etiqueta.

Migraciones
===========

Como hemos visto al principio de este capítulo, los ``Ordenadores`` se identifican
inequívocamente por el UUID de la placa base y, además, mantienen un campo
``Versión`` que se corresponde con el ajuste del mismo nombre de los
:ref:`Ajustes del cliente migasfree`. Ahora bien, en el momento en que el
servidor detecta que no corresponde la versión que tiene el ordenador en la
base de datos del servidor con la que recibe del equipo, el servidor actualiza
el registro ``Ordenador`` y además añade un registro de ``Migración``. De esta
manera se consigue llevar un histórico de migraciones.

Campos de Migración
-------------------

    * **Ordenador**: Equipo que se ha migrado de versión migasfree.

    * **Versión**: Version migasfree.

    * **Fecha**: Fecha y hora en que se ha detectado el cambio de versión.

Notificaciones
==============

Ante hechos relevantes en el sistema, el servidor genera notificaciones para
alertar a los administradores.

Campos de Notificación
----------------------

    * **Fecha**: Fecha y hora en que se ha generado la notificación.

    * **Notificación**: Describe el hecho.

    * **Comprobado**:  Campo que se marcará manualmente cuando se ha recibido
      la notificación.

Consultas
=========

Aquí podrás ejecutar las ``Consultas`` disponibles.

Puedes añadir nuevas consultas o modificar las predeterminadas accediendo a
``Configuración-Consultas``. Una pequeña explicación de cómo se programan
la puedes encontrar en el apartado :ref:`Consultas` de
:ref:`La configuración del sistema migasfree`.

Estadísticas
============

Es una lista con estadísticas predefinidas.


    * **ordenadores actualizados/hora**: Gráfica de barras que indica la cantidad
      (única) de equipos que han completado la actualización de migasfree
      por hora.

    * **ordenadores actualizados/día**: Gráfica de barras que indica la cantidad
      (única) de equipos que han completado la actualización de migasfree
      por día.

    * **ordenadores actualizados/mes**: Gráfica de barras que indica la cantidad
      (única) de equipos que han completado la actualización de migasfree
      por mes.

    * **ordenadores previstos/demora**: Gráfica de líneas que representa una
      previsión, basada en los ``Atributos`` del último ``Login`` de cada ordenador,
      de los equipos que accederían a un repositorio hipotético según
      ``Calendarios``.

    * **ordenadores/versión**: Gráfica de tarta donde se aprecia la cantidad de
      ordenadores por versión.

El proceso de las comprobaciones
================================

Al igual que como liberador debes realizar un conjunto de tareas para mantener
el sistema en codiciones, continuamente te llegarán errores, fallas, etc. que
debes comprobar y atender. Esta es la misión para un usuario ``checker``.

¿Qué tareas tienes que hacer como comprobador del sistema?. Sencillo. Mantén
las ``Alertas`` a 0. El sistema te irá avisando qué debes atender.

    * Comprueba periódicamente la existencia de ``Errores``. Soluciónalos y márcalos
      como comprobados.

    * Comprueba periódicamente la existencia de ``Fallas``. Soluciónalas y márcalas
      como comprobadas.

    * Comprueba periódicamente la existencia de ``Notificaciones``. Una vez leídas,
      márcalas como comprobadas.


Otros procesos
==============

.. _`Reemplazo de ordenadores`:

Reemplazo de ordenadores
------------------------

Este proceso permite intercambiar el estado, etiquetas, dispositivos y
atributos ``CID`` asignados en el sistema entre dos ordenadores.

Imagina que un usuario te reporta un fallo de hardware y decides darle un equipo
que tienes en estado ``disponible`` para que continúe su trabajo. En este caso
ve al menú ``Datos - Reemplazo de ordenadores`` e introduce los dos ordenadores.
Una vez pulses en el botón ``Reemplazar`` el ordenador que estaba ``disponible``
tendrá ahora el estado, etiquetas e impresoras que tenía el ordenador estropeado.
Finalmente puedes editar el ordenador que ha fallado y cambiarle el estado a
``en reparación`` o a ``baja``.
