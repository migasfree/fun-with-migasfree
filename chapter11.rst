============
La Auditoría
============

 .. epigraph::

   Nuestro conocimiento es necesariamente finito, mientras que nuestra
   ignorancia es necesariamente infinita.

   -- Karl Raimund Popper

Una vez que liberas los paquetes y que los equipos se van sincronizando, llega el
momento de que veas, de manera centralizada, toda la información que se ha ido
generando a consecuencia del proceso de sincronización.

Esto es lo que te vas a encontrar en este capítulo.


.. _`Alertas`:

Alertas
=======

Muestra en lo que debe actuar el administrador para tener un sistema lo
más íntegro posible.

Son un conjunto de comprobaciones que se realizan para alertar al usuario.
Pulsando en cada una de las ``Alertas`` puedes obtener más información. Ver figura 11.1.

.. only:: not latex

   .. figure:: graphics/chapter11/alert.png
      :scale: 100
      :alt: Alertas del sistema.

      figura 11.1. Alertas del sistema.


.. only:: latex

   .. figure:: graphics/chapter11/alert.png
      :scale: 50
      :alt: Alertas del sistema.

      Alertas del sistema.

Hay 9 alertas predeterminadas en *migasfree*:

    * ``Errores sin comprobar``. Cuando en un cliente *migasfree* se produce algún error,
      es enviado al servidor. Esta comprobación hace que se muestren estos
      errores. Una vez revisado o solucionado un error en el cliente debes editar
      el error en el servidor y marcar el campo ``comprobado``. Esto hará que
      ya no aparezca en la lista de errores a comprobar. Puedes también
      seleccionar un conjunto de errores en la lista de errores y en el desplegable
      de ``acción`` seleccionar ``La comprobación es correcta``.

    * ``Fallas sin comprobar``. Cuando en un cliente migasfree se produce una
      falla, es enviada al servidor. Esta comprobación hace que se muestren
      las fallas pendientes. La manera de proceder con las fallas es similar a
      la de los ``Errores sin comprobar``.

    * ``Notificaciones sin comprobar``. Son hechos que se han producido en el sistema y
      que son informados mediante esta comprobación. Un ejemplo de notificación
      es cuando un equipo da de alta una plataforma o un proyecto nuevo en el
      sistema.

    * ``Paquetes huérfanos``. Comprueba si hay paquetes que no están asignados
      a ningún despliegue.

    * ``Ordenadores sincronizándose``. Cuando un equipo está ejecuando el cliente
      migasfree, éste va informando al servidor de lo que está haciendo mediante
      un texto que indica el proceso que está realizando. Cuando el cliente
      migasfree finaliza, envía al servidor un mensaje de texto vacío.
      Esta comprobación comprueba cuántos de estos mensajes se han recibido.

    * ``Ordenadores retrasados``. Si pasa un determinado tiempo desde que se recibió
      el último mensaje del cliente, es muy posible que algo ha ido mal en el
      cliente. Quizás perdió la conexión, o el usuario apagó el equipo en medio
      de la ejecución del cliente migasfree, o quizás ha habido algún error. Esta
      comprobación permite detectar estos casos. La cantidad de tiempo viene
      establecida por defecto en 30 minutos y puede ser modificado mediante el ajuste
      ``MIGASFREE_SECONDS_MESSAGE_ALERT`` de los :ref:`Ajustes del servidor migasfree`.

    * ``Generación de repositorios``. Indica si se están generando los metadatos
      de algún repositorio físico asociado a algún despliegue.

    * ``Despliegues con calendario activo``.

    * ``Despliegues con calendario finalizado``. Si hay despliegues que tienen
      el calendario de distribución finalizado, deberías pasar esa información
      (paquetes disponibles, a instalar, etc.) a otro despliegue que no tenga
      calendario y borrar el despliegue original para simplificar la gestión
      de los mismos.

Las ``alertas`` proporcionan al usuario una vista general de la situación actual del
sistema, dirigiendo su actuación a lo relevante.

El objetivo en todo momento debería ser mantener el sistema con 0 alertas. Esto
indicaría que se han revisado los errores, se han comprobado las fallas,
no hay paquetes huérfanos, etc.


.. _`Ordenadores`:

Ordenadores
===========

Accediendo a ``Datos-Ordenadores``, verás la lista de ordenadores que
se han registrado en el servidor.

Puedes acceder al hardware de un equipo desde la última columna ``Producto``
de la lista de ordenadores.

También puedes acceder a los **datos** que están **relacionados** con un equipo
determinado, mediante el desplegable que hay a la derecha del identificador del equipo.
Así, fácilmente podrías ver la cantidad de errores que ha habido en un equipo, sus fallas,
migraciones, actualizaciones, ... Además, en este menú desplegable del ordenador,
te vas a encontrar con otras opciones interesantes:

* **Sucesos**: Sobre un calendario, desde la fecha de entrada del equipo en el servidor,
  se muestra la cantidad diaria de sincronizaciones, errores, fallas, migraciones y
  registros de estado. A más cantidad diaria de sucesos, el color es más oscuro.

* **Simular sincronización**: Te permite simular lo que entregaría el servidor
  al cliente cuando éste último ejecuta ``migasfree -u``. De esta manera, y basándonos
  en los actuales atributos del ordenador, puedes ver qué despliegues se configurarían en el
  cliente, qué paquetes se instalarían o eliminarían o qué fallas se ejecutarían.

* **Hardware**: Nos da acceso al hardware del equipo.

* **Etiqueta**: Te muestra una etiqueta que puede ser impresa para pegarla en
  el ordenador.


Campos de Ordenador
-------------------

    * **Nombre**: Es el nombre del equipo o el especificado en el
      ajuste ``Computer_Name`` de los :ref:`Ajustes del cliente migasfree`.

    * **Proyecto**: El proyecto migasfree del ordenador.

    * **Fecha de alta**: Fecha de alta del ordenador en migasfree.

    * **Dirección IP**: La dirección IP del equipo en el momento de la sincronización.

    * **Dirección IP reenviada**: Útil si el equipo es virtual y queremos saber la IP del ordenador anfitrión.

    * **Comentario**.

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
                        Despliegue, Conjunto de Atributos, Dispositivo Lógico,
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
                ordenador se ha asignado en algún Despliegue, Conjunto de
                Atributos, Dispositivo Lógico, Definición de Falla y/o Demora
                de Calendario también será eliminada dicha asignación
                automáticamente.

        Puedes consultar más información sobre los ``CID`` en las :ref:`Fórmulas específicas`.

        Puedes asignar un estado por defecto a los nuevos ordenadores con el
        ajuste de servidor: :ref:`MIGASFREE_DEFAULT_COMPUTER_STATUS`

        .. only:: not latex

           .. figure:: graphics/chapter11/status.png
              :scale: 100
              :alt: Iconos de estado: asignado, reservado, desconocido, disponible, en reparación y baja.

              figura 11.1.  Iconos de estado: asignado, reservado, desconocido, disponible, en reparación y baja.


        .. only:: latex

           .. figure:: graphics/chapter11/status.png
              :scale: 25
              :alt: Estado asignado, reservado, desconocido, disponible, en reparación y baja.

              Estado asignado, reservado, desconocido, disponible, en reparación y baja.

    * **Etiquetas**: Lista de Etiquetas asignadas actualmente al ordenador.
      Para una explicación del funcionamiento de las etiquetas mira los
      :ref:`Categorías de etiquetas`.

    * **Dispositivos lógicos**: Impresoras lógicas configuradas en el ordenador.

    * **Dispositivo lógico por defecto**: Indica el dispositivo lógico por defecto
      en el sistema.

    * **Usuario**: Último usuario que ha iniciado sesión en el ordenador.

    * **Atributos de la sincronización**: Lista de ``Atributos`` que se han obtenido
      como resultado de ejecutar la ``Fórmulas`` en el ordenador cliente en el proceso de
      sincronización.

    * **Fecha de inicio de la sincronización**: Fecha en la que comenzó la última sincronización del cliente migasfree.

    * **Fecha de fin de la sincronización**: Fecha en la que se finalizó por última vez la
      sincronización del cliente migasfree.

    * **Tiempo de la última actualización**: Tiempo que ha tardado el cliente migasfree
      en actualizarse.

    * **Errores sin comprobar**: Muestra el número de errores pendientes de comprobar
      del ordenador.

    * **Fallas sin comprobar**: Muestra el número de fallas pendientes de comprobar
      del ordenador.

    * **Inventario de software**: Paquetes actuales instalados en el ordenador.

    * **Historial de software**: Registro de los paquetes instalados y
      desinstalados según se van produciendo en el tiempo.

    * **Fecha de la última actualización del hardware**: Fecha en que se envió por última vez
      el hardware.

    * **Producto**: Nombre del ordenador incluido en la placa base.
      Por ejemplo ``HP ProDesk 600 G1 SFF (C8T89AV)``

    * **Uuid**: Es el identificador único universal de la placa base del equipo.

          .. note::

            El cliente de migasfree es el encargado de proporcionar este UUID. En
            caso de no poder obtenerlo porque el fabricante de la placa
            base no lo ha asignado o por cualquier otro motivo, el cliente
            proporciona un UUID basado en la MAC de la primera tarjeta de red
            que encuentre.

    * **Máquina**: Indica si es una máquina física o virtual.

    * **Procesador**: Nombre del microprocesador. Ejemplo: ``Intel Core i5-4590 3.30GHz``

    * **RAM**: Cantidad de memoria RAM.

    * **Almacenamiento**: Cantidad de almacenamiento en disco.

    * **Discos**: Número de discos.

    * **Dirección MAC**: Direcciones MAC del ordenador.

Usuarios
========

A medida que el cliente de migasfree va ejecutándose en los equipos, el servidor
va añadiendo los usuarios que se han autenticado en el entorno gráfico.

Puedes ver la lista de usuarios en ``Datos-Usuarios``

Campos de Usuario
-----------------

    * **Nombre**: Nombre de la cuenta de usuario para acceder al equipo.

    * **Nombre Completo**: Nombre y apellidos del usuario.

Atributos
=========

A medida que se vayan actualizando los equipos, el servidor migasfree irá
añadiendo los atributos enviados por los clientes con objeto de que puedas
liberar paquetes en función de estos atributos.

Campos de Atributo
------------------

    * **Fórmula**: Fórmula a la que hace referencia el atributo.

    * **Valor**: Identifica el atributo.

    * **Descripción**: Describe el atributo.

Una explicación del funcionamiento de los atributos la puedes obtener en
el apartado :ref:`Fórmulas` de :ref:`La configuración del sistema migasfree`.

Etiquetas
=========

Manualmente podrás añadir etiquetas y asignarlas a ordenadores para
liberar software en función de estas.

El funcionamiento de las etiquetas ya lo hemos visto en los
:ref:`Categorías de etiquetas`.

Campos de Etiqueta
------------------

    * **Categoría de etiqueta**: Hace referencia al tipo de etiqueta.

    * **Valor**: Identifica a la etiqueta.

    * **Descripción**: Describe la etiqueta.

    * **Ordenadores**: Permite asignar ordenadores a la etiqueta.

Errores
=======

Conforme se vayan produciendo errores en los clientes, irán llegando al servidor
y serán mostrados en ``Alertas``.

Campos de error
---------------

    * **Comprobado**: Campo que se marcará manualmente cuando se ha comprobado y
      solucionado el error.

    * **Ordenador**: Equipo en el que se ha producido el error.

    * **Proyecto**: Es el proyecto que tenía el equipo cuando se produjo el error.

    * **Fecha**: Fecha y hora en que se produjo el error.

    * **Descripción**: Mensaje que describe el error. Generalmente corresponde a
      la salida de error del *front-end* del P.M.S.

Fallas
======

Ya viste el concepto de :ref:`Fallas` y cómo se pueden programar en el capítulo
:ref:`La configuración del sistema migasfree`, así que no me repitiré.

Lo mismo que ocurre con los errores, conforme las fallas se vayan detectando en
los clientes, irán apareciendo en el ``Alertas``.

Campos de falla
---------------

    * **Comprobado**: Campo que se marcará manualmente cuando se ha comprobado y
      solucionado la falla.

    * **Ordenador**: Equipo en el que se ha producido.

    * **Proyecto**: Es el proyecto que tenía el equipo cuando se produjo la falla.

    * **Definición de falla:**: Tipo de Falla. Hace referencia al código que
      ha generado la falla.

    * **Fecha**: Fecha y hora en que se produjo la falla.

    * **Resultado**: Mensaje que describe la falla. Corresponde a
      la salida estándar del código de la ``Definición de la falla``.

Migraciones
===========

Como hemos visto al principio de este capítulo, los ``Ordenadores`` se identifican
inequívocamente por el UUID de la placa base y, además, mantienen un campo
``Proyecto`` que se corresponde con el ajuste del mismo nombre de los
:ref:`Ajustes del cliente migasfree`. Ahora bien, en el momento en que el
servidor detecta que no corresponde el proyecto que tiene el ordenador en la
base de datos del servidor con el que recibe del equipo, el servidor actualiza
el registro ``Ordenador`` y además añade un registro de ``Migración``. De esta
manera se consigue llevar un histórico de migraciones.

Campos de Migración
-------------------

    * **Ordenador**: Equipo que se ha migrado de proyecto migasfree.

    * **Proyecto**: Proyecto migasfree.

    * **Fecha**: Fecha y hora en que se ha detectado el cambio de proyecto.

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


    * **cuadro de mando**: Resumen de las estadísticas más importantes sobre
      el parque de ordenadores gestionado por el servidor migasfree.

    * **ordenadores actualizados/hora**: Gráfica de barras que indica la cantidad
      (única) de equipos que han completado la actualización de migasfree
      por hora.

    * **ordenadores actualizados/día**: Gráfica de barras que indica la cantidad
      (única) de equipos que han completado la actualización de migasfree
      por día.

    * **ordenadores actualizados/mes**: Gráfica de barras que indica la cantidad
      (única) de equipos que han completado la actualización de migasfree
      por mes.

    * **resumen de dispositivos**: Varias gráficas relacionadas con los dispositivos.


El proceso de las comprobaciones
================================

Al igual que como liberador debes realizar un conjunto de tareas para mantener
el sistema en codiciones, continuamente te llegarán errores, fallas, etc. que
debes comprobar y atender. Esta es la misión para un usuario ``checker``.

¿Qué tareas tienes que hacer como comprobador del sistema? Sencillo. Mantén
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
