===
API
===

 .. epigraph::

   La belleza es el acuerdo entre el contenido y la forma.

   -- Henrik Johan Ibsen

El objetivo de este capítulo es describir la API de migasfree.

Desde sus inicios migasfree ha contado con una API propia pero desde la versión
4.11 del servidor se está incorporado una nueva API `REST`__ al servidor migasfree
con objeto de substituirla totalmente.

__ https://es.wikipedia.org/wiki/Transferencia_de_Estado_Representacional

Puedes consultar la autodocumentación de la API REST de migasfree accediendo a
http://<miservidor>/docs o haciendo click en el icono del espía que aparece
situado abajo a la derecha en todas las páginas de la aplicación web del servidor.

El proyecto ``fun-with-migasfree-examples`` incluye un directorio llamado
``api-examples`` donde encontraŕas código de ejemplo para hacer uso de la API REST.

Si aún no te has bajado los ejemplos ahora puede ser un buen momento para hacerlo
y echarle un ojo al uso de la API REST.

  .. code-block:: none

    $ wget https://github.com/migasfree/fun-with-migasfree-examples/archive/master.zip
    $ unzip master.zip
    $ cd fun-with-migasfree-examples-master/api-examples


En cuanto a la API antigua (y que va a desaparecer en el futuro) podemos decir
que tiene 2 tipos de API:

    * `Pública`__:

        * Son accesibles públicamente.

        * Utilizan el metodo GET de HTTP para el envío de parámetros

__ https://github.com/migasfree/migasfree/blob/latest/migasfree/server/views/public_api.py

    * `Privada`__:

        * Comparten entre sí la `misma manera de llamar a las funciones`__.

        * Envían un fichero en el parámetro ``message`` del método POST HTTP, cuyo
          nombre de fichero debe usar el siguiente formato:

          .. code-block:: none

            <COMPUTER_NAME>.<UUID>.<API_FUNCTION>

        * En el contenido del fichero ``message`` se introduce, en formato json
          lo que denominamos el ``API Private Data`` con los parámetros de
          entrada de las funciones.

        * En la mayoría de los casos este ``API Private Data`` es
          firmado usando la KEY del ``Proyecto`` o del ``Empaquetador``
          añadiendo esta firma al final del fichero:

          .. code-block:: none

            ``API Private Data`` + sign(``API Private Data``)

        * En el menor de los casos estas funciones en vez de firma requieren el
          uso de un usuario y contraseña que simplemente se introduce en el propio
          ``API Private Data``.

        * Los valores devueltos por la funciones se reciben en formato json
          convenientemente firmados por el servidor, siguiendo la estructura:

          .. code-block:: none

            {"<API_FUNCTION>.return": ``API Private Data`` } +
                sign({"<API_FUNCTION>.return": ``API Private Data`` })


__ https://github.com/migasfree/migasfree/blob/latest/migasfree/server/api.py

__ https://github.com/migasfree/migasfree/blob/latest/migasfree/server/views/client_api.py

.. raw:: latex

  \newpage

get_projects
============

Pertenece a la API pública.

Devuelve una lista de diccionarios de las plataformas con sus ``proyectos``
correspondientes.

Parámetros de entrada
---------------------

    * Ninguno

Salida
------

    * Lista de diccionarios de plataformas:

        * **plafform**: Nombre de la plataforma.

        * **projects**: Lista de diccionarios de proyectos:

            * **name**: Nombre del proyecto.


Veamos un ejemplo. Si en un navegador web accedemos a la siguiente dirección:

  .. code-block:: none

    http://miservidor/get_projects

Obtendremos una cadena de texto en formato json parecida a esta:

  .. code-block:: none

    [{"platform": "Linux", "projects": [{"name": "ACME-1"}, {"name": "debian-7.0"}]}]



.. raw:: latex

  \newpage

get_computer_info
=================

Pertenece a la API pública.

Obtiene un diccionario con información relevante del ordenador consultado.

Parámetros de entrada
---------------------

    * **uuid**: Como parámetro de método GET en la petición HTTP debe indicarse
      el identificador único de la placa base del ordenador.

Salida
------

    * Diccionario de datos del equipo:

        * **search**: Valor del primer campo indicado en la lista
          ``MIGASFREE_COMPUTER_SEARCH_FIELDS`` de los
          :ref:`Ajustes del servidor migasfree` y que sirve para facilitar la
          identificación del equipo en vez de usar el uuid.

        * **name**: Nombre del ordenador.

        * **tags**: Lista de cadenas de texto con los nombres de las ``Etiquetas``
          asignadas al ordenador.

        * **available_tags**: Diccionario de Propiedades de tipo ``Etiqueta``.

              * **<Propiedad>**: Lista de cadenas de texto con el nombre de las
                etiquetas.

        * **helpdesk**: Cadena de texto MIGASFREE_HELP_DESK de los
          :ref:`Ajustes del servidor migasfree`

        * **id**: Número identificador del ordenador en la tabla de ``Ordenadores``

        * **uuid**: Identificador único de la placa base del ordenador


Veamos un ejemplo accediendo a:

  .. code-block:: none

    http://miservidor/get_computer_info/?uuid=E9E66900-CBD4-9A47-B2EC-6ED0367A3AFB

obtendríamos algo parecido a esto:

  .. code-block:: none

    {"search": 2, "name": "debian-client", "tags": [], "available_tags": {},
    "helpdesk": "Put here how you want to be found", "id": 2,
    "uuid": "E9E66900-CBD4-9A47-B2EC-6ED0367A3AFB"}


.. raw:: latex

  \newpage

computer_label
==============

Pertenece a la API pública.

Obtiene una página html que muestra la etiqueta que debe pegarse físicamente
en el equipo para facilitar su identificación aún estando éste apagado.

Es utilizada por el comando ``migasfree-label``.


Parámetros de entrada
---------------------

    * **uuid**: Como parámetro de método GET en la petición HTTP debe indicarse
      el identificador único de la placa base del ordenador.

Salida
------

    * La página **html** de la etiqueta:

Por ejemplo al ejecutar:

  .. code-block:: none

    http://miservidor/computer_label/?uuid=E9E66900-CBD4-9A47-B2EC-6ED0367A3AFB

Podemos obtener algo como:

.. only:: not latex

   .. figure:: graphics/chapter16/helpdesk.png
      :scale: 100
      :alt: Comando migasfree-label

      figura 18.1. Comando migasfree-label.


.. only:: latex

   .. figure:: graphics/chapter16/helpdesk.png
      :scale: 50
      :alt: Comando migasfree-label.

      Comando migasfree-label.


.. raw:: latex

  \newpage

register_computer
=================

Pertenece a la API Privada.

Necesita usuario y contraseña con permisos de lectura/escritura en
``Ordenadores``, y en ``Plataformas`` y ``Proyectos`` si
``MIGASFREE_AUTOREGISTER`` está activo. Ver :ref:`Ajustes del servidor migasfree`

Esta función realiza lo siguiente:

    * Registra el ``Ordenador`` en el servidor.

    * Añade la ``Plataforma`` y/o ``Proyecto`` del ordenador si no existen,
      siempre y cuando ``MIGASFREE_AUTOREGISTER`` esté activo.

    * Añade las correspondientes ``Notificaciones``

    * Como resultado se obtendrán las KEYS del ``Proyecto`` que usarán las
      funciones de la API pública que las requieren.

API Private Data Input
----------------------

    * **username**: Nombre del usuario

    * **pasword**: Contraseña

    * **platform**: Plataforma del ordenador.

    * **project**: Proyecto del ordenador.

    * **pms**: Sistema de paquetería.

    * **ip**: Dirección IP.

API Private Data Output
-----------------------

    * **migasfree-server.pub**: KEY pública del servidor,

    * **migasfree-client.pri**: KEY privada del proyecto.

    * **errmfs**: Diccionario con el posible error devuelto.

        * **code**: Código del error. Un valor de cero indica que no ha habido
          error.

        * **info**: Texto desciptivo del error.

.. raw:: latex

  \newpage

get_key_packager
================

Pertenece a la API Privada.

Necesita usuario y contraseña con permisos de lectura/escritura en ``Paquetes``.

Obtiene la ``KEY`` que permitirá subir paquetes al servidor con el comando
de cliente ``migasfree-upload``.


API Private Data Input
----------------------

    * **username**: Nombre del usuario.

    * **password**: Contraseña del usuario.


API Private Data Output
-----------------------

    * **migasfree-server.pub**: KEY pública del servidor,

    * **migasfree-packager.pri**: KEY privada del empaquetador.

    * **errmfs**: Diccionario con el posible error devuelto.

        * **code**: Código del error. Un valor de cero indica que no ha habido
          error.

        * **info**: Texto desciptivo del error.

.. raw:: latex

  \newpage

upload_server_package
=====================

Pertenece a la API Privada.

Necesita firmar con KEY de empaquetador.

Sube un paquete al servidor.

El fichero del paquete debe enviarse en ``HttpRequest.FILES["package"]``

API Private Data Input
----------------------

    * **project**: Proyecto.

    * **store**: Almacén donde se almacena el paquete.

    * **source**: Valor booleano que indica si el paquete es el binario o
      el fuente.

API Private Data Output
-----------------------

    * **errmfs**: Diccionario con el posible error devuelto.

        * **code**: Código del error. Un valor de cero indica que no ha habido
          error.

        * **info**: Texto desciptivo del error.

.. raw:: latex

  \newpage


upload_server_set
=================

Pertenece a la API Privada.

Necesita firmar con KEY de Empaquetador.

Sube un paquete de un ``Conjunto de Paquetes`` al servidor .

El fichero del paquete debe enviarse en ``HttpRequest.FILES["package"]``

API Private Data Input
----------------------

    * **project**: Proyecto.

    * **store**: Almacén donde se almacena el paquete.

    * **packageset**: ``Conjunto de Paquetes`` en el que está incluido el
      paquete.

API Private Data Output
-----------------------

    * **errmfs**: Diccionario con el posible error devuelto.

        * **code**: Código del error. Un valor de cero indica que no ha habido
          error.

        * **info**: Texto desciptivo del error.





.. raw:: latex

  \newpage

create_repositories_of_packageset
=================================

Pertenece a la API Privada.

Necesita firmar con KEY de Empaquetador.

Se utiliza para forzar la creación de los metadatos de los ``Despliegues`` en
donde está asignado el ``Conjunto de Paquetes`` especificado.

Se usa despues de subir todos los paquetes de un ``Conjunto de Paquetes``.

API Private Data Input
----------------------

    * **packageset**: El nombre del ``Conjunto de Paquetes``.

    * **project**: El ``Proyecto`` del ``Conjunto de Paquetes``.

API Private Data Output
-----------------------

    * **errmfs**: Diccionario con el posible error devuelto.

        * **code**: Código del error. Un valor de cero indica que no ha habido
          error.

        * **info**: Texto desciptivo del error.

.. raw:: latex

  \newpage

upload_computer_message
=======================

Pertenece a la API Privada.

Necesita firmar con KEY de Proyecto.

Envia un mensaje de texto al servidor informando que proceso esta realizando el
cliente. Es utilizado por ``migasfree --update``

API Private Data Input
----------------------

El mensaje de texto que se quiere enviar al servidor.

API Private Data Output
-----------------------

    * **errmfs**: Diccionario con el posible error devuelto.

        * **code**: Código del error. Un valor de cero indica que no ha habido
          error.

        * **info**: Texto desciptivo del error.


.. raw:: latex

  \newpage

get_properties
==============

Pertenece a la API Privada.

Necesita firmar con KEY de Proyecto.

Obtiene las Propiedades activas en el servidor migasfree.

API Private Data Input
----------------------

No requiere.

API Private Data Output
-----------------------

    * **properties**: Lista de diccionarios con las Propiedades:

        * **prefix**: Prefijo de la propiedad

        * **function** Instrucciones de la Propiedad

        * **language** Lenguaje en que está programado la propiedad.

    * **errmfs**: Diccionario con el posible error devuelto.

        * **code**: Código del error. Un valor de cero indica que no ha habido
          error.

        * **info**: Texto desciptivo del error.

.. raw:: latex

  \newpage

upload_computer_info
====================

Pertenece a la API Privada.

Necesita firmar con KEY de Proyecto.

Dados los datos del ordenador Obtiene del servidor diferente información con
lo que el cliente debe hacer para realizar una actuliazación.

API Private Data Input
----------------------

    * **computer**: Diccionario con información relativa al ``Ordenador``

        * **hostname**: Nombre del ordenador.

        * **ip**: Dirección ip del ordenador.

        * **platform**: Plataforma.

        * **project**: Nombre del proyecto.

        * **user**: Cuenta del usuario que esta logueado en la sesión gráfica.

        * **user_fullname**: Nombre completo del usuario

    * **attributes**: Lista de diccionarios con los ``Atributos`` conseguidos
      al ejecutar cada una de las ``Propiedades``

        * **<ATTRIBUTES_NAME>**: Valor del Atributo


API Private Data Output
-----------------------

    * **faultsdef**: Lista de diccionarios de ``Definiciones de Fallas``

        * **name**: Nombre de la falla.

        * **function**: Instrucciones de la falla.

        * **language**: Lenguaje en que está escrita la falla.

    * **repositories**: Lista de diccionarios de repositorios que deben
      configurarse en el cliente y que han sido seleccionados por el servidor
      en función de los atributos de entrada y la fecha actual.

          * **name**:

    * **packages**: Diccionario de paquetes.

        * **install**: Lista de cadenas de texto con los paquetes a instalar.

        * **remove**: Lista de cadenas de texto con los paquetes a desinstalar.

        * **hardware_capture**: ``True`` si el ordenador tiene que enviar
          el hardware.

        * **devices**: #TODO

    * **logical**: Diccionario de dispositivos a instalar o desinstalar.

    * **errmfs**: Diccionario con el posible error devuelto.

        * **code**: Código del error. Un valor de cero indica que no ha habido
          error.

        * **info**: Texto desciptivo del error.


.. raw:: latex

  \newpage

upload_computer_faults
======================

Pertenece a la API Privada.

Necesita firmar con KEY de Proyecto.

Sube el resultado de las ``Fallas``.

API Private Data Input
----------------------

Diccionario con las Fallas:

    * **<PROPIEDAD>**: Texto de la salida estándar al ejecutar la ``FALLA``

API Private Data Output
-----------------------

    * **errmfs**: Diccionario con el posible error devuelto.

        * **code**: Código del error. Un valor de cero indica que no ha habido
          error.

        * **info**: Texto desciptivo del error.


.. raw:: latex

  \newpage

upload_computer_hardware
========================

Pertenece a la API Privada.

Necesita firmar con KEY de Proyecto.

Sube el hardware del ``Ordenador``.

API Private Data Input
----------------------

Salida en formato *json* del comando ``lshw``.

API Private Data Output
-----------------------

    * **errmfs**: Diccionario con el posible error devuelto.

        * **code**: Código del error. Un valor de cero indica que no ha habido
          error.

        * **info**: Texto desciptivo del error.

.. raw:: latex

  \newpage

upload_computer_software_base_diff
==================================

Pertenece a la API Privada.

Necesita firmar con KEY de Proyecto.

Sube la diferencia respecto al ordenador base

API Private Data Input
----------------------

Texto con la lista de paquetes respecto al ordenador base separados por retornos
de carro.

API Private Data Output
-----------------------

    * **errmfs**: Diccionario con el posible error devuelto.

        * **code**: Código del error. Un valor de cero indica que no ha habido
          error.

        * **info**: Texto desciptivo del error.

.. raw:: latex

  \newpage

upload_computer_software_base
=============================

Pertenece a la API Privada.

Necesita firmar con KEY de Proyecto.

Lo utiliza el ``Ordenador`` de referencia para informar de los paquetes que
tiene instalados.


API Private Data Input
----------------------

Texto con la lista de paquetes instalados separados por retornos de carro.

API Private Data Output
-----------------------

    * **errmfs**: Diccionario con el posible error devuelto.

        * **code**: Código del error. Un valor de cero indica que no ha habido
          error.

        * **info**: Texto desciptivo del error.


.. raw:: latex

  \newpage

upload_computer_software_history
================================

Pertenece a la API Privada.

Necesita firmar con KEY de Proyecto.

Informa de cambio en el software.

API Private Data Input
----------------------

Texto con el cambio de paquetes producidos en el ``Ordenador``. Sigue el formato:

  .. code-block:: none

    # [<FECHA DESDE>, <FECHA_HASTA]
    <ACTION><PACKAGE> ,
    <ACTION><PACKAGE> , ...

dónde ACTION puede ser (-) para indicar desintalado y (+) para indicar paquete
instalado.

API Private Data Output
-----------------------

    * **errmfs**: Diccionario con el posible error devuelto.

        * **code**: Código del error. Un valor de cero indica que no ha habido
          error.

        * **info**: Texto desciptivo del error.


.. raw:: latex

  \newpage

get_computer_software
=====================

Pertenece a la API Privada.

Necesita firmar con KEY de Proyecto.

Obtiene el conjunto de paquetes del ``Ordenador`` de referencia.

API Private Data Input
----------------------

No requiere.

API Private Data Output
-----------------------

    * Texto con la lista de paquetes del ``Ordenador`` de referencia separados
      por retorno de carro

    * **errmfs**: Diccionario con el posible error devuelto.

        * **code**: Código del error. Un valor de cero indica que no ha habido
          error.

        * **info**: Texto desciptivo del error.


.. raw:: latex

  \newpage

upload_computer_errors
======================

Pertenece a la API Privada.

Necesita firmar con KEY de Proyecto.

Sube los errores producidos en el cliente.

API Private Data Input
----------------------

Texto con el errores que han producido en el cliente.

API Private Data Output
-----------------------

    * **errmfs**: Diccionario con el posible error devuelto.

        * **code**: Código del error. Un valor de cero indica que no ha habido
          error.

        * **info**: Texto desciptivo del error.


.. raw:: latex

  \newpage

get_computer_tags
=================

Pertenece a la API Privada.

Necesita firmar con KEY de Proyecto.

Obtiene las etiquetas del ``Ordenador`` y las disponibles en el sistema.

API Private Data Input
----------------------

No requerido

API Private Data Output
-----------------------

    * **selected**: Lista de textos con las ``Etiquetas`` asignadas al ordenador.

    * **available**: Diccionario de etiquetas.

        * **<PROPERTY>**: Lista de textos con las ``Etiquetas`` disponibles
          por cada ``Propiedad` de tipo ``tag``

    * **errmfs**: Diccionario con el posible error devuelto.

        * **code**: Código del error. Un valor de cero indica que no ha habido
          error.

        * **info**: Texto desciptivo del error.

.. raw:: latex

  \newpage

set_computer_tags
=================

Pertenece a la API Privada.

Necesita firmar con KEY de Proyecto.

Asigna las etiquetas al ordenador y como resultado se obtiene los paquetes que
deben instalarse y desinstalarse en función de las etiquetas que anteriormente
tuviera asignadas el equipo.


API Private Data Input
----------------------

    * **tags**: Lista de etiquetas a asignar al ``Ordenador``

API Private Data Output
-----------------------

    * **packages**: Diccionario con la listas de paquetes.

        * **preinstall**: Lista de nombres de paquetes separados por espacios
          obtenidos del campo ``default preinstall packages``

        * **install**: Lista de nombres de paquetes separados por espacios
          obtenidos del campo ``default install packages``

        * **remove**:Lista de nombres de paquetes separados por espacios
          obtenidos del campo ``default remove packages``

    * **errmfs**: Diccionario con el posible error devuelto.

        * **code**: Código del error. Un valor de cero indica que no ha habido
          error.

        * **info**: Texto desciptivo del error.
