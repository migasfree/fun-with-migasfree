=========================================
Configurando software al estilo migasfree
=========================================

 .. epigraph::

   No esperes hasta que las condiciones sean perfectas para comenzar,
   el empezar hace las condiciones perfectas.

   -- Alan Cohen.

En este capítulo vas a aprender a configurar el servidor migasfree al
estilo migasfree.

Quizás no sea el ejemplo más acertado porque vas a configurar sólo
un servidor migasfree, pero imagina un escenario donde tienes X centros
de trabajo y te interesa tener un servidor migasfree con la misma
configuración en cada centro para dar servicio a sus clientes.
Uno de estos servidores bien podría ser el que admistrara al resto de
servidores.

El objetivo de este capítulo es que veas todo el proceso de la Gestión
de la Configuración Software en conjunto.

Al estilo tradicional
=====================

Imagina que te llega una petición de cambio para modificar, en todos los
centros, el nombre de la organización de los servidores migasfree con el
nombre de tu empresa.

Miras la documentación de migasfree y concluyes que tienes que crear el
fichero ``/etc/migasfree-server/settings.py`` y añadir la siguiente
variable:

  .. code-block:: none

    MIGASFREE_ORGANIZATION = "ACME"

Decides acceder a cada uno de los equipos por ssh, crear el fichero,
reiniciar el servidor apache y olvidarte del tema.

Ahora bien, si estás de vacaciones ¿podría responder fácilmente a las
cuestiones siguientes tu compañero de trabajo?

* ¿Qué cambios se han realizado en un determinado equipo desde el 1 de
  enero? ¿Quién los hizo? ¿Y cúando se realizaron todos esos cambios?

* ¿Qué equipos tienen el cambio propuesto?

Este método es sencillo y rápido, pero difícilmente tu compañero va a
poder reponder estas cuestiones de manera eficaz, aunque hayas registrado
muy bien tu trabajo. La integridad frente al cambio no está garantizada
con éste método.

A continuación te propongo otra forma de realizar los cambios de
configuración. Se basa en utilizar el empaquetado para trasladar los
cambios a los equipos conservando la integridad del sistema.

Asumo que tienes un gestor de proyectos como Redmine donde vas a
registrar las peticiones de cambio (o al menos que hagas como que lo
tienes) y que has completado con éxito el capítulo anterior. Todos los
comandos de este capítulo los vas a ejecutar como root en el equipo que
hayas utilizado en el capítulo anterior.



Tu primer cambio de configuración
=================================

El primer cambio sobre un Elemento de Configuración Software (ECS) es el
que te llevará más trabajo porque exige la creación de un paquete.

Petición
--------

Imagina que te llega la siguiente la petición de cambio que registras y
aceptas en el gestor de proyectos:

  .. admonition:: Gestor de proyectos:

     Registro: Sustituir el nombre de la organización ``My organization``
     de los servidores migasfree por el de ``ACME``

.. only:: not latex

   .. figure:: graphics/chapter06/myorganization.png
      :scale: 100
      :alt: Nombre de la organización.

      figura 6.1. Nombre de la organización.


.. only:: latex

   .. figure:: graphics/chapter06/myorganization.png
      :scale: 50
      :alt: Nombre de la organización.

      Nombre de la organización.


Lo primero que haces es identificar al ECS que afecta, es decir, cuál es
el paquete que debe ser modificado. Como no existe todavía un paquete
sobre el que actuar, asigna la petición de cambio a un desarrollador
(Qué suerte, siempre te toca a tí) y registra en la petición de cambio:

  .. admonition:: Gestor de proyectos:

     Registro: Crear el paquete **acme-migasfree-server**

     Asignado a: *desarrollador*.

Cambio
------

Empaquetado
***********

Cómo desarrollador tienes que crear el paquete de configuración
``acme-migasfree-server``. Si nunca has creado un paquete no te
preocupes, para facilitarte las cosas y que puedas avanzar centrándote
en el proceso GCS aqui tienes el fuente del paquete.

En la máquina virtual ejecuta:

  .. code-block:: none

    # wget http://www.migasfree.org/repo/book/acme-migasfree-server_1.0-1.tar.gz
    # tar -xzvf acme-migasfree-server_1.0-1.tar.gz

Observa como modificamos el nombre de la organización

  .. code-block:: none

    # less acme-migasfree-server/etc/migasfree-server/settings.py

  .. note::

      En los :ref:`Ajustes del servidor migasfree` puedes ver el
      conjunto de ajustes que se pueden emplear para adaptar el servidor
      a tus necesidades.

Y observa tambien que en la postinstalación del paquete se ejecutará el
comando ``service apache2 reload`` cuando se produzca la configuración
del paquete:

  .. code-block:: none

    # less acme-migasfree-server/debian/postinst

Ya tienes el fuente del paquete. Ahora genera el paquete, pero para ello
antes debes tener instalado el paquete devscripts:

  .. code-block:: none

    # apt-get install devscripts

Y ahora sí, genera el paquete:

  .. code-block:: none

    # cd acme-migasfree-server
    # /usr/bin/debuild --no-tgz-check -us -uc
    # cd ..

Felicidades, el cambio está empaquetado en ``acme-migasfree-server_1.0-1_all.deb``

Subiendo al servidor el cambio
******************************

Usa este comando para subir el paquete generado al servidor.

  .. code-block:: none

    # migasfree-upload -f acme-migasfree-server_1.0-1_all.deb

* Introduce usuario: admin

* Contraseña: admin

* Version: debian-7.0

* Ubicacion: acme

La salida que te devolverá el comando ``migasfree-upload`` será:

  .. code-block:: none

    root@debian7:~# migasfree-upload -f acme-migasfree-server_1.0-1_all.deb
    Versión de migasfree upload: 3.1
    Usuario para subir ficheros al servidor: admin
    Contraseña del usuario:
    Versión a la que subir en el servidor: debian-7.0
    Ubicación a la que subir en el servidor: acme

    Opciones de configuración:
        Servidor: 192.168.92.133
        Proxy: None
        Depuración: False
        Versión: debian-7.0
        Ubicación: acme
        Usuario: admin
        Fichero: acme-migasfree-server_1.0-1_all.deb
        Fichero normal: None
        Crear repositorio: True

    Obteniendo las claves de empaquetador...
    ¡Clave /root/.migasfree-keys/migasfree-server.pub creada!
    ¡Clave /root/.migasfree-keys/migasfree-packager.pri creada!

Finalmente asigna la petición de cambio a un liberador (sí, otra vez
vas a ser tú) y registra en la petición:

  .. admonition:: Gestor de proyectos:

     Registro: Creado paquete **acme-migasfree-server_1.0-1_all.deb**

     Asignado a: *liberador*

Felicidades, has realizado un cambio de configuración y lo has
almacenado en el servidor migasfree.

Liberación
----------

Ahora vas a ver el punto de vista del encargado de liberar los cambios:

Accede mediante navegador web a tu servidor. Observa que en
``Auditoria - Datos - Estado`` aparace ``1 paquete huérfano`` (Figura 6.2).

.. only:: not latex

   .. figure:: graphics/chapter06/orphan.png
      :scale: 40
      :alt: Paquetes huérfanos.

      figura 6.2. Paquetes huérfanos.


.. only:: latex

   .. figure:: graphics/chapter06/orphan.png
      :scale: 80
      :alt: Paquetes huérfanos.

      Paquetes huérfanos.

Todos los paquetes que se han subido al servidor y todavía no los has
puesto en ningún repositorio se denominan ``huérfanos``.

Liberando el cambio de configuración
************************************

Ahora, vas a liberar el cambio. Ve a ``Liberación - Añadir Repositorio``
y configúralo.

* Nombre = ``PRINCIPAL``

* Version = ``debian-0.7``

* Fecha = ``Hoy``

* Paquetes/Conjuntos = ``acme-migasfree-server_1.0-1_all.deb``

  En este campo se asignan los paquetes que contendrá este repositorio.

* Paquetes a instalar = ``acme-migasfree-server``

  En este campo se escriben los nombres de los paquetes que se
  instalarán **obligatoriamente** en los clientes.

* Atributos = ``ALL-ALL SYSTEMS``

  De esta manera indicamos que todos los clientes tendrán acceso a este
  repositorio.

Guarda el repositorio.

Observa que en ``Auditoría - Datos- Estado`` ya no tienes ningún paquete
huérfano.

Registra y cierra la petición de cambio:

  .. admonition:: Gestor de proyectos:

     Registro: Liberado en Repositorio **PRINCIPAL**.

     Petición: *cerrada*.

Aplicando el cambio
*******************

Para aplicar el cambio ejecuta el siguiente comando:

  .. code-block:: none

    # migasfree -u

Observa en la salida del comando:

  .. code-block:: none

    ****************** Subiendo el historial del software... *******************
    Diferencia en el software: # 2013-05-19 10:42:33
    +acme-migasfree-server-1.0-1
    ***************************** Correcto


Abre el navegador y fíjate que el nombre de la organización ha cambiado
(Figura 6.3).

.. only:: not latex

   .. figure:: graphics/chapter06/acme.png
      :scale: 100
      :alt: Cambio nombre organización a ACME.

      figura 6.3. Cambio nombre organización a ACME.


.. only:: latex

   .. figure:: graphics/chapter06/acme.png
      :scale: 50
      :alt: Cambio nombre organización a ACME.

      Cambio nombre organización a ACME.

Tu segundo cambio de configuración
==================================

Petición
--------

Te llega la segunda petición de cambio:


  .. admonition:: Gestor de proyectos:

     Registro: Sustituir de nuevo el nombre de la organización  en los
     servidores migasfree ya que el nombre correcto es
     `Acme Corporation.`__

__ http://en.wikipedia.org/wiki/Acme_Corporation

Como siemrpre, identificas primero el ECS al que afecta el cambio: En
este caso es a ``acme-migasfree-server``. En la petición
de cambio asignas al desarrollador y registras:

  .. admonition:: Gestor de proyectos:

     Registro: Modificar el paquete **acme-migasfree-server-1-0.1**

     Asignado a : *desarrollador*.


Cambio
------
Los cambios que se realizan sobre un paquete ya creado suelen ser más
sencillos de realizar porque simplemente se modifica el paquete.

Empaquetado
***********

Edita el fichero ``acme-migasfree-server/etc/migasfree-server/settings.py``
y modifica la variable ``MIGASFREE_ORGANIZATION``:

  .. code-block:: none

    MIGASFREE_ORGANIZATION = "Acme Corporation"

Edita ``acme-migasfree-server/debian/changelog`` para registrar el
cambio realizado. Tendrás que **añadir** estas líneas **al principio
del fichero**:

  .. code-block:: none

    acme-migasfree-server (1.0-2) unstable; urgency=low

      * Change organitation to Acme Corporation

     -- Alberto Gacías <alberto@migasfree.org>  Sun, 19 May 2013 13:09:00 +0200

Presta atención a:

* La versión del paquete **(1.0-2)**.

* Sustituir **tu nombre y dirección de correo**.

* Modificar la **fecha y hora**.

Ahora generamos el paquete:

  .. code-block:: none

    # cd acme-migasfree-server
    # /usr/bin/debuild --no-tgz-check -us -uc
    # cd ..

Observa que se ha generado el mismo paquete pero con la versión 1.0-2

  .. code-block:: none

    # root@debian7:~# ls -la *.deb
    -rw-r--r-- 1 root root 2286 may 19 10:37 acme-migasfree-server_1.0-1_all.deb
    -rw-r--r-- 1 root root 2338 may 19 13:25 acme-migasfree-server_1.0-2_all.deb


Subiendo al servidor el cambio
******************************

  .. code-block:: none

    # migasfree-upload -f acme-migasfree-server_1.0-2_all.deb

* Introduce usuario: admin

* Contraseña: admin

* Version: debian-7.0

* Ubicacion: acme


  .. admonition:: Gestor de proyectos:

     Registro: Creado paquete **acme-migasfree-server_1.0-2_all.deb**

     Asignado a: *liberador*


Liberación
----------

Liberando el cambio de configuracion
************************************

Accede a ``Liberación - Empaquetado -Repositorios`` y edita el repositorio
``PRINCIPAL``. Añade a ``Paquetes/Conjuntos`` el paquete
``acme-migasfree-server_1.0-2_all.deb``

Guarda el repositorio.

Registra y cierra la petición de cambio:

  .. admonition:: Gestor de proyectos:

     Registro: Liberado en Repositorio **PRINCIPAL**.

     Petición: *cerrada*.


Aplicando el cambio
********************

Ejecuta de nuevo:

  .. code-block:: none

    # migasfree -u

Observa en la salida de este comando el cambio de software:

  .. code-block:: none

    ****************** Subiendo el historial del software... *******************
    Diferencia en el software: # 2013-05-19 21:51:28
    +acme-migasfree-server-1.0-2
    -acme-migasfree-server-1.0-1
    ***************************** Correcto


Comprueba si el cambio se ha aplicado.

.. only:: not latex

   .. figure:: graphics/chapter06/acmecorporation.png
      :scale: 100
      :alt: Nombre de la organización.

      figura 6.4. Cambio nombre organización a Acme Corporation.

.. only:: latex

   .. figure:: graphics/chapter06/acmecorporation.png
      :scale: 50
      :alt: Cambio nombre organización a Acme Corporation.

      Cambio nombre organización a Acme Corporation.

Auditoría
=========

Ahora sí que vas a responder las siguientes cuestiones de
manera centralizada desde el servidor migasfree:

¿Qué cambios se han producido en el ordenador ``1`` y cuándo?
-------------------------------------------------------------

Accede a ``Auditoria - Datos - ordenadores``, edita el equipo ``1``
y mira el final del campo ``historial de software``:

  .. code-block:: none

    # 2013-05-19 21:47:18
    +acme-migasfree-server-1.0-1

    # 2013-05-19 21:51:28
    +acme-migasfree-server-1.0-2
    -acme-migasfree-server-1.0-1

El signo (-) indica paquete desinstalado y el signo (+) paquete instalado.

¿Qué se cambió, quién y cuándo lo hizo?
------------------------------------------------------------------

Esta información está en el paquete como metainformación. Para acceder
a ella accede a ``Liberación - Empaquetado - Paquetes``.  En el campo
``Acción`` selecciona ``informacion del paquete``. Marca la casilla del
paquete ``acme-migasfree-server_1.0-2_all.deb`` y pulsa en el botón ``ir``.

Aquí podras ver el registro de los cambios (entre otra información):

  .. code-block:: none

    ****CHANGELOG****
    acme-migasfree-server (1.0-2) unstable; urgency=low

      * Change organitation to Acme Corporation

     -- Alberto Gacías <alberto@migasfree.org>  Sat, 19 May 2013 08:32:00 +0200

    acme-migasfree-server (1.0-1) unstable; urgency=low

      * Change organitation to ACME

     -- Alberto Gacías <alberto@migasfree.org>  Sat, 18 May 2013 08:32:00 +0200

¿Qué equipos tienen el cambio acme-migasfree-server-1.0-2?
----------------------------------------------------------

Ve a ``Auditoria - Consultas - Ordenadores con el paquete...``.
Escribe en el campo Paquete  ``acme-migasfree-server-1.0-2`` y obtendrás
el resultado.


Conclusión
==========

Aunque requiera de un esfuerzo inicial *empaquetar la configuración de
las aplicaciones*, los beneficios que obtendrás justifican sobradamente
el uso de este método, ya que dispondrás de sistemas más estables, te
permitirá hacer el seguimento y control de los cambios y mejorarás la
resolución de incidencias.

Beneficios de crear paquetes de configuración
---------------------------------------------

* La configuración permacece encapsulada.

* Las configuraciones puede revertirse fácilmente.

* Facilita las pruebas antes del despliegue.

* Facilita la distribución de las configuraciones de forma segura.

* Proporciona integridad frente a los cambios de la configuración.

Desventajas del empaqueteado de la configuración.
-------------------------------------------------

* Cuesta más tiempo que otras alternativas ya que hay que crear los paquetes.


Utilizar migasfree para la realizar la *Liberación* te permitirá
controlar a quién y a partir de que momento se deben aplicar dichos cambios.
