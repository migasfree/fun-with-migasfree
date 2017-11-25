=================================
La sincronización de los sistemas
=================================

 .. epigraph::

   Al fin y al cabo, somos lo que hacemos para cambiar lo que somos.

   -- Eduardo Galeano

En el capitulo anterior, has aprendido a liberar paquetes desde un servidor
migasfre. Pero, para que se produzca el cambio de software, no basta sólo con
liberarlo. Los clientes deben poder acceder a los despliegues, bajarse los
paquetes e instalarlos.

En este capítulo vas a centrarte en el cliente migasfree para ir conociendo los
comandos que tienes a tu disposición.

El proceso de sincronización
============================

Ahora creo que es buen momento de aprender qué hace ``migasfree --update`` :

    * Envía mensaje de inicio del proceso de sincronización al servidor.

    * Envía errores de anteriores ejecuciones. Si los hay, el servidor creará
      un registro de ``Error``.

    * Recibe las ``Fórmulas`` definidas en el servidor.

    * Ejecuta dichas *fórmulas* y los resultados son enviados como ``Atributos``.
      El servidor almacena estos atributos y los asocia con el ordenador que se está sincronizando.

    * Recibe el código de las ``Fallas`` y los ``Despliegues`` a configurar,
      basándose en los ``Atributos`` y la fecha actual. Recibe las impresoras
      que deben estar instaladas. Además, la lista de paquetes a desinstalar e
      instalar obligatoriamente, también se reciben en este momento del proceso.

    * Ejecuta y envía el resultado de las ``Fallas``. Si estas se producen, el
      servidor creará un registro de ``Falla`` por cada una de ellas.

    * Configura los ``Despliegues`` que el servidor ha dispuesto en función de
      los ``Atributos`` del cliente y de la fecha actual.

    * Actualiza los metadatos de los repositorios configurados en el sistema.
      Consiste simplemente en obtener el índice de paquetes actualizado de cada
      repositorio.

    * Desinstala los paquetes obligatorios. Conjunto de paquetes definidos en
      el campo ``Paquetes a desinstalar`` de los ``Despliegues`` efectivos.

    * Instala los paquetes obligatorios. Conjunto de paquetes definidos en
      el campo ``Paquetes a instalar`` de los ``Despliegues`` efectivos.

    * Actualiza paquetes disponibles. En caso de que en los
      :ref:`Ajustes del cliente migasfree` ``Auto_Update_Packages`` sea
      ``False``, no se producirá esta actualización.

    * Envía al servidor el historial de cambios en el software. Es la diferencia
      de paquetes instalados en el sistema antes y despues de desisntalar, instalar
      y actualizar los paquetes.

    * Envía el inventario de software (los paquetes que tiene ahora mismo ese equipo).

    * Envía el inventario de hardware periódicamente según ``MIGASFREE_HW_PERIOD``
      de los :ref:`Ajustes del servidor migasfree`,

    * Envía los errores de ejecución. Si los hay, el servidor creará un registro
      de ``Error``.

    * Se añaden y/o eliminan las impresoras.

    * Por último, envía un mensaje de proceso finalizado. Cuando el servidor
      recibe este mensaje añade un registro de ``Sincronización`` en la base de
      datos que se emplean para hacer diferentes estadísticas.

Puedes ver una simulación de esta sincronización, accediendo al menú
desplegable del identificador del ordenador en la aplicación web. Ver :ref:`Ordenadores`


El comando ``migasfree``
========================

La opción del comando migasfree ``--update`` es, sin lugar a dudas, la más
importante. Su sintaxis es:

      .. code-block:: none

        migasfree -u
        migasfree --update

``migasfree -u`` puede usarse conjuntamente con opción ``--force-upgrade`` para forzar la
sincronización de paquetes a pesar que en el ajuste ``Auto_Update_Packages``
esté asignado a ``False``. Consulta el ajuste ``Auto_Update_Packages`` de los
:ref:`Ajustes del cliente migasfree`.

      .. code-block:: none

        migasfree -u -a
        migasfree --update --force-upgrade

Existen otras opciones que pueden hacer más fácil el mantenimiento a los
administradores.

En las organizaciones que usan distintos S.O. con sistemas de paquetería diferentes,
tanto para buscar, instalar o desinstalar paquetes, los administradores tienen
que utilizar los comandos propios del sistema de paquetería. Utilizar las
opciones del comando migasfree para realizar estas tareas te permite abstraerte
del P.M.S. (no tendrás que estar pensando si estás en un sistema basado en
Debian o en un Redhat p.e.):

    * Para buscar un determinado paquete en los repositorios utiliza:

      .. code-block:: none

        migasfree -s <texto>
        migasfree --search <texto>

    * Para instalar un determinado paquete, usa:

      .. code-block:: none

        migasfree -ip <paquete>
        migasfree --install --package=<paquete>

    * Para desinstalar un determinado paquete, usa:

      .. code-block:: none

        migasfree -rp <paquete>
        migasfree --remove --package=<paquete>

Por último, tienes la opción que permite registrar el equipo cliente en
el servidor migasfree en caso de que en el registro ``Proyecto`` del servidor el
campo ``Autoregistrado`` esté desmarcado.

      .. code-block:: none

        migasfree -g
        migasfree --register


El comando ``migasfree-tags``
=============================

Puedes ver una explicación de este comando y de su sintaxis en el campo
``Etiqueta`` de las :ref:`Fórmulas` en el capítulo
:ref:`La configuración del sistema migasfree`.


El comando ``migasfree-label``
==============================

Consulta el ajuste ``MIGASFREE_HELP_DESK`` de los :ref:`Ajustes del servidor migasfree`
donde se describe este comando.
