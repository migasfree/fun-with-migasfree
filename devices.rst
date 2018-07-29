============
Dispositivos
============

 .. epigraph::

   La lógica es clara y sencilla: la propaganda es a la democracia lo que la
   cachiporra al estado totalitario.

   -- Noam Chomsky

Migasfree puede ser utizado también para instalar de manera centralizada las
impresoras, ahorrándote un tiempo más que considerable respecto a una instalación
manual en cada ordenador (aunque inicialmente se requiera introducir en el
sistema los distintos modelos de impresoras que vayas a utilizar).

Además, por ser un sistema centralizado, te va a permitir conocer el parque de
impresoras de tu organización.

En migasfree las impresoras son asignadas a atributos, por lo que puedes especificar
que una determinada impresora sea instalada en todos los ordenadores que tengan,
por ejemplo, la etiqueta ``AUL-AULA_DE_FORMACION`` aunque, obviamente, lo más común
será asignarlas a un ordenador concreto utilizando su CID (Computer ID).

   .. note::

      La instalación de las impresoras se producirá cuando un cliente haga ``migasfree -u``
      ya que el servidor indica en ese momento al cliente qué impresoras debe
      tener instaladas. El cliente es el que con esa información instala, desinstala
      o actualiza las impresoras.


Pasos para la configuración de las impresoras:
==============================================

* Añadir los **fabricantes**.
* Definir las diferentes **prestaciones** que vas a utilizar.
* Añadir los **modelos** y crear un paquete por cada modelo de impresora.
* Añadir cada **dispositivo** físico, especificando cómo está conectado y qué
  dispositivos lógicos deben instalarse a cada ``atributo``.


Fabricantes
===========

Campos del Fabricante
---------------------

* **Nombre**: Nombre del fabricante de la impresora.


Prestaciones
============

Representa una determina configuración por defecto del controlador del dispositivo.

Esto sirve para facilitar a los usuarios la impresión, ya que por cada impresora
fisica puedes querer instalarle diferentes configuraciones por defecto. Por ejemplo,
puedes querer configurar estas 3 impresoras lógicas:

    * Impresión en negro, doble cara y calidad borrador

    * Impresión en color y en 1 cara

    * Impresión usando la bandeja multipropósito

Así que en este caso te interesaría crear las siguiente prestaciones:

    * BORRADOR

    * COLOR

    * MULTIPROPOSITO.


Campos de la Prestación
-----------------------

* **Nombre**: Nombre la prestación.


Modelos
=======

Por cada modelo de impresora se especifican las distintas conexiones y los
distintos controladores que estarán admitidos.


Campos del modelo de dispositivo
--------------------------------

* **Nombre**: Nombre del modelo de la impresora.

* **Fabricante**: Asigna el Fabricante del modelo de impresora.

* **Tipo**: Actualmente sólo se utiliza 'PRINTER'.

* **Conexiones**: Especifica las distintas maneras en las que puedes conectar
  físicamente la impresora.


* **Controladores**: Por cada **version** y **prestación** tendrás que definir
  que archivo ppd debe ser utilizado.

  Un archivo PPD (PostScript Printer Description) describe las características
  disponibles para la impresora. Dicho archivo puede ser obtenido directamente
  del fabricante o en su defecto de `openprinting.org`__

    * **Proyecto**: Proyecto migasfree.

    * **Prestación**: Prestación.

    * **Nombre**: Ruta completa donde esta ubicado el archivo .ppd en los
      ordenadores.

    * **Paquetes a instalar**: En este campo deberás poner el nombre del paquete
      que contiene el archivo ppd que vas a utilizar. Si es necesario algún otro
      paquete, puedes añadirlo separándolo con un espacio.

__ http://www.openprinting.org/printers


Dispositivos
============

Representa a cada una de las distintas impresoras físicas.

Campos del dispositivo
----------------------

    * **Nombre**: Identificador único de la impresora física (en AZLinux usamos el nº
      de inventario que lleva impreso la etiqueta que pegamos en cada impresora).

    * **Modelo**: Modelo de la impresora

    * **Conexión**: Como se conecta físicamente la impresora.

    * **Dispositivos lógicos**:

        * **Prestación**: Prestación.

        * **Nombre**: Nombre alternativo a la prestación. Es opcional.

        * **Atributos**: Atributos a los que será instalado el dispositivo lógico.

   .. note::

      La forma más eficaz de añadir los dispositivos es asignar el nombre,
      modelo y conexión y entonces pulsar en ``grabar y continuar editando``.
      De esta manera se añadirán automáticamente los dispositivos lógicos
      asociados a ese modelo de impresora y podrán ser asignados entonces
      los atributos.


Reemplazo de dispositivos
=========================

Imagina p.e. que tienes una impresora de red instalada en 30 ordenadores
y que va a ser sustituida por otro modelo de impresora. En este caso, lo único
que tendrás que hacer es un ``Reemplazo de dispositivos`` indicando el
dispositivo antiguo y el nuevo. Solamente eso.

Si has leído y entendido bien este último párrafo, deberías ya comprender cómo
migasfree puede ahorrarte mucho tiempo en todo lo relacionado a la instalación
de impresoras.


Ejemplo EPSON AL-M300
=====================

Para afianzar los conceptos vamos a crear el modelo ``EPSON AL-M300`` y a
instalar dos impresoras físicas con estas tres prestaciones:

    * **BN**: Impresión en negro.
    * **MP**: Bandeja multipropósito.
    * **DUPLEX**: Doble cara

Para ello descárgate los ejemplos de este libro donde encontrarás una carpeta llamada
``acme-epson-al-m300``

  .. code-block:: none

     $ wget https://github.com/migasfree/fun-with-migasfree-examples/archive/master.zip
     $ unzip master.zip
     $ cd fun-with-migasfree-examples-master/acme-epson-al-m300

Observa que en el paquete existen tres archivos ``.ppd`` que se corresponden con las
prestaciones comentadas.

  .. code-block:: none

     $ ls  usr/share/ppd/acme
     Epson_AL_M300-duplex-ps-es.ppd
     Epson_AL_M300-MP-ps-es.ppd
     Epson_AL_M300-ps-es.ppd


Una manera simple de obtener estos archivos *ppd*, es la siguiente:

    1) Obtén el ppd del propio fabricante de la impresora o en su defecto de
       `openprinting.org`__

    2) Instala una impresora en tu sistema con el archivo ppd obtenido.

    3) **Modifica las propiedades** de la impresora desde el interface gráfico de
       usuario de acuerdo a la prestación que va a proporcionarte (ejecuta p.e. ``system-config-printer`` en un terminal).

    4) En el directorio /etc/cups/ppd/ tendrás el ppd con las opciones que has
       elegido para tu prestación, cópialo con un nombre relacionado con esa
       prestación.

__ http://www.openprinting.org/printers.

Crea ahora el paquete (debes tener el paquete ``devscripts`` y ``debhelper``
previamente instalados).

  .. code-block:: none

     $ /usr/bin/debuild --no-tgz-check -us -uc

Súbelo al servidor

  .. code-block:: none

     # migasfree-upload -f ../acme-epson-al-m300_1.0-1_all.deb

y libéralo creando un nuevo despliegue en el servidor llamado p.e.
``impresoras``. Asígnale el paquete ``acme-epson-al-m300_1.0-1_all.deb`` y en
atributos asigna ``ALL-SYSTEMS``.

Ve a ``Dispositivos - Fabricantes`` y añade EPSON.

En ``Dispositivos -Pestaciones`` añade ``BN`` ``MP`` y ``DUPLEX``

Añade un ``Dispositivo - Modelos`` de la siguiente manera:

    * Nombre: AL-M300

    * Fabricante: EPSON

    * Tipo: PRINTER

    * Conexiones: USB y TCP. (Aquí especificamos las distintas conexiones
      que tiene la impresora)


Pulsa en ``Grabar y continuar editando``.

Ahora añade los controladores:

    * Controlador 1:

        * Proyecto: debian-8.6. (u otra)

        * Prestación: BN

        * Nombre: /usr/share/ppd/acme/Epson_AL_M300-ps-es.ppd

        * Paquetes a instalar: acme-epson-al-m300

    * Controlador 2:

        * Proyecto: debian-8.6. (u otra)

        * Prestación: MP

        * Nombre: /usr/share/ppd/acme/Epson_AL_M300-MP-ps-es.ppd

        * Paquetes a instalar: acme-epson-al-m300


    * Controlador 3:

        * Proyecto: debian-8.6. (u otra)

        * Prestación: DUPLEX

        * Nombre: /usr/share/ppd/acme/Epson_AL_M300-duplex-ps-es.ppd

        * Paquetes a instalar: acme-epson-al-m300


Hasta aquí hemos definido los modelos de impresoras. Ahora ya estamos en
disposición de añadir las impresoras a los equipos.

Vamos a añadir 2 impresoras físicas de ejemplo al ordenador ``CID-1``.

Impresora Física 1 conectada por TCP
------------------------------------

Ve a ``Dispositivos - Dispositivos`` y añade la primera impresora:

    * Nombre: Impresora1

    * Modelo: AL-M300

    * Conexión: Elije TCP

    * IP: 10.0.2.250

    * Pulsa ahora en ``Grabar y continuar editando`` y aparecerán los tres dispositivos
      lógicos correspondientes. Deja el ``Nombre`` en blanco. Añade a cada uno de
      los dispositivos lógicos el atributo CID-1 (o el atributo que quieras).


Impresora Física 2 conectada por USB
------------------------------------

Ve a ``Dispositivos - Dispositivos`` y añade la segunda impresora:

    * Nombre: Impresora2

    * Modelo: AL-M300

    * Conexión: Elije ahora USB.

    * Pulsa ahora en ``Grabar y continuar editando`` y aparecerán los tres dispositivos
      lógicos correspondientes. Deja el ``Nombre en blanco``. Añade a cada uno de
      los dispositivos lógicos el atributo CID-1 (o el atributo que quieras).

Y con esto, al hacer ``migasfree -u`` en cada ordenador se instalarán las
impresoras lógicas según hemos especificado.

Para finalizar, conviene mencionar que cualquier cambio que se realice en el
``dispositivo`` (la IP, el tipo de conexión, o el nombre p.e.) será modificado
automáticamente en los ordenadores cuando estos se actualicen.
