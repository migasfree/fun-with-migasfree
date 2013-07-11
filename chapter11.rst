============
La Auditoría
============

 .. epigraph::

   Nuestro conocimiento es necesariamente finito, mientras que nuestra
   ignorancia es necesariamente infinita.

   -- Karl Raimund Popper

Una vez que liberas los paquetes y que los equipos se van actualizando llega el
momento de que veas, de manera centralizada, toda la información que se ha ido
generando a consecuencia del proceso de actualización.

Ésto es lo que te vas a encontrar en este capítulo.

Estado general del sistema
==========================

Muestra en lo debe actuar el administrador para tener un sistema lo más íntegro
posible. Ya lo viste en apartado ``Estado`` del capítulo
:ref:`La configuración del sistema migasfree`.

Ordenadores
===========

Accediendo a ``Auditoría-Datos-Ordenadores`` verás la lista de ordenadores que
se han registrado en el servidor.

Puedes acceder al ``Hardware`` de un equipo desde la última columna de la lista
de ordenadores.

Campos de Ordenador
-------------------

    * **Nombre**: Es el nombre del equipo o el especificado en el
      ajuste ``Computer_Name`` de los :ref:`Ajustes del cliente migasfree`

    * **Uuid**: Es el identificador único universal de la placa base del equipo.

    * **Versión**: La versíon migasfree del ordenador.

    * **Fecha de alta**: Fecha de alta del ordenador en migasfree.

    * **IP**: La dirección ip del equipo en el momento de la actualización.

    * **Inventario de software**: Diferencia actual entre el conjunto de paquetes del
      ordenador de referencia y el ordenador en cuestión. Ver en
      :ref:`La configuración del sistema migasfree` los campos de version:
      ``Actual line computer`` y ``Actual line packages``

    * **Historial de software**: Registro de los paquetes instalados y
      desinstalados según se van produciendo en el tiempo.

    * **Última actualización**: Fecha en la que se finalizó por última vez la
      actualización del cliente migasfree.

    * **Actualización hardware**: Fecha de la última actualización hardware.

    * **Etiquetas**: Lista de Etiquetas asignadas actualmente al ordenador.
      Mira el campo ``Etiqueta`` de la ``Propiedad`` del capítulo
      :ref:`La configuración del sistema migasfree` para una explicación del
      funcionamiento de las etiquetas.


Usuarios
========

A medida que el cliente de migasfree va ejecutándose en los equipos el servidor
va añadiendo los usuarios que se han autenticado en el entorno gráfico.

Puedes ver la lista de usuarios en ``Auditoria-Datos-Usuarios``


Campos de Usuario
-----------------

    * **Nombre**: Nombre de la cuenta de usuario para acceder al equipo.

    * **Nombre Completo**: Nombre y apellidos del usuario.

Logins
======

Cuando se ejecuta ``migasfree --update`` se crea un registro de ``Login`` en
el servidor.

  .. note::

    Migasfree lleva por cada equipo el **último login** de cada usuario, no
    todos.

Campos de Login
---------------

    * **Fecha**: Fecha y hora de la ejecución de ``migasfree --update`` en el
      equipo

    * **Usuario**: Usuario actual que está ejecutando el entorno gráfico

    * **Ordenador**: El equipo al que hace referencia el login.

    * **Atributos** :Lista de ``Atributos`` que se han obtenido como resultado de
      ejecutar la ``Propiedades`` en el ordenador cliente en el proceso de
      actualización.

Errores
=======

Conforme se vayan produciendo errores en los clientes irán llegando al servidor
y serán mostrados en el ``Estado del sistema``.

Campos de error
---------------

    * **Ordenador**: Equipo en el que se ha producido el error.

    * **Fecha**: Fecha y hora en que se produjo el error.

    * **Error**: Mensaje que describe el error. Mayoritariamente corresponde a
      la salida de error del front-end del P.M.S.

    * **Comprobado**: Campo que se marcará manualmente cuando se ha comprobado y
      solucionado el error.

    * **Versión**: Es la versión que tenía el equipo cuando se produjo el error.

Fallas
======

Ya viste el concepto de ``Falla`` y como se pueden programar en el capítulo
:ref:`La configuración del sistema migasfree`, así que no me repitiré.

Lo mismo que ocurre con los errores, conforme las fallas se vayan detectando en
los clientes irán apareciendo en el ``Estado del sistema``.

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

Migraciones
===========

Como hemos visto al principio de este capítulo los ordenadores, los ordenadores
se identifican inequívocamente por el uuid de la placa base y además  llevan un
campo ``Versión``. Ahora bien, en el momento en que el servidor detecta que no
corresponde la versión que tiene el ordenador en la base de datos del servidor
con la que recibe del equipo, el servidor actualiza el registro ``Ordenador``
y además crea un registro de ``Migración``.

Campos de Migración
-------------------

    * **Ordenador**: Equipo que se ha migrado de versión migasfree.

    * **Versión**: Version migasfree.

    * **Fecha**: Fecha y hora en que se ha detectado el cambio de versión

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
``Configuración-General-Consultas``. Una pequeña explicación de cómo se programan
la puedes encontrar en el apartado ``Consultas`` de
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
      de los equipos que accederían a un repositorio hipotético al que se le aplicara
      un determinado ``Calendario``.

    * **ordenadores/versión**: Gráfica de tarta donde se aprecia la cantidad de
      ordenadores por version.

El proceso de las comprobaciones
================================

Al igual que como liberador debes realizar un conjunto de tareas para mantener
el sistema en codiciones, continuamente te llegarán errores, fallas, etc. que
debes comprobar y atender. Esta es la misión para un usuario ``checker``.

¿Qué tareas tienes que hacer como comprobador del sistema?. Sencillo. Mantén
el ``Estado del sistema`` en "ALL O.K.". Él te irá avisando que debes atender.

    * Comprueba periódicamente la existencia de errores. Soluciónalos y márcalos
      como comprobado.

    * Comprueba periódicamente la existencia de fallas. Soluciónalas y márcalas
      como comprobada.

    * Comprueba periódicamente la existencia de notificaciones. Una vez leídas
      márcalos como comprobada.
