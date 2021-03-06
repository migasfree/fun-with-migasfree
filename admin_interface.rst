.. _`El interfaz de administración`:

=============================
El interfaz de administración
=============================

 .. epigraph::

   Mantén tus ojos en las estrellas y tus pies en la tierra.

   -- Theodore Roosevelt.


Antes de profundizar en el uso de migasfree, déjame que te describa
el interfaz de administración del servidor migasfree mediante la
siguiente imagen.

.. only:: not latex

   .. figure:: graphics/admin_interface/general.png
      :scale: 50
      :alt: interfaz de administración.

.. only:: latex

   .. figure:: graphics/admin_interface/general.png
      :scale: 60
      :alt: interfaz de administración.


1. Nombre de tu organización (o instancia del servidor) definido en
   el ajuste de configuración del servidor: :ref:`MIGASFREE_ORGANIZATION`.


2. Menú.

    * Configuración.

    * Dispositivos.

    * Liberación.

    * Datos.

    * Consultas.


3. Búsqueda rápida de ordenador.

4. Selección de :ref:`Dominios`.

5. Selección de :ref:`Ambitos`.

6. :ref:`Alertas`.

7. Usuario que ha iniciado sesión. Permite el :ref:`Cambio de contraseña`.

8. `Miga de pan`__. Debajo de la ``miga de pan`` aparece el nombre
   de los datos con los que estamos trabajando, ``Ordenadores`` en este caso.
   A continuación del nombre aparecería un simbolo ``+`` para introducir más datos
   en caso de disponer permisos para ello.


9. Filtros predefinidos.

10. Búsqueda.

11. Acciones sobre los datos:

    * Selecciona los datos (12).
    * Elije una acción.
    * Pulsa en el botón ``ir``.

12. Datos.

__ https://es.wikipedia.org/wiki/Miga_de_pan_(inform%C3%A1tica)


Ayudas
======

Ahora fíjate que en el interfaz de administración, abajo a la derecha, hay
tres iconos de ayuda.


.. only:: not latex

   .. figure:: graphics/admin_interface/helps.png
      :scale: 100
      :alt: Ayudas.

.. only:: latex

   .. figure:: graphics/admin_interface/helps.png
      :scale: 100
      :alt: Ayuda.

El primer icono, representa al ``modelo de datos``. Te proporciona
información contextual de las tablas y campos de la Base de Datos
junto con sus relaciones con otras tablas. Puede serte útil para
obtener información a la hora de realizar consultas SQL a la
Base de Datos.

Mediante el segundo icono podrás acceder a la documentación de la
``Migasfree REST API``. Desde aquí podrás realizar llamadas directamente a la API
y ver la respuesta del servidor. Muy útil para el desarrollo de programas que hacen
uso de ella.

El último icono, el del libro, también es una ayuda contextual. Pulsando
en él, y dependiendo de en que menú estés situado, se te dirigirá a la sección
de la ``Guía de uso`` de ``Fun with migasfree`` en la que se describe lo que estás
viendo en ese momento.


Datos relacionados
==================

Ahora fíjate en cómo podemos navegar fácilmente por los ``datos relacionados``,
pulsando en el ``triángulo`` que aparece a la derecha de los elementos.


.. only:: not latex

   .. figure:: graphics/admin_interface/relations.png
      :scale: 100
      :alt: Datos relacionados.

.. only:: latex

   .. figure:: graphics/admin_interface/relations.png
      :scale: 100
      :alt: Datos relacionados.


Para acceder a los datos relacionados pulsa sobre el **número** de elementos.

Mas adelante, cuando cojas soltura, podrás añadir tus propias ``acciones externas``
tales como **VNC**, **PING**, **SSH**, etc. mediante el ajuste :ref:`MIGASFREE_EXTERNAL_ACTIONS` 
de los :ref:`Ajustes del servidor migasfree`, pero por ahora creo que es suficiente.





