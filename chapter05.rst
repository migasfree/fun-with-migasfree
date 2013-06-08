==================
Probando migasfree
==================
 .. epigraph::

   La unidad es la variedad, y la variedad en la unidad es la ley
   suprema del universo.

   -- Isaac Newton.

Hay multiples combinaciones de Distribuciones, base de datos y servidores
web que se pueden elegir a la hora de instalar un servidor migasfree.

En este capítulo voy a explicarte como instalarlo sobre
`Debian 7 Wheezy`__ usando Posgresql y Apache que es la combinación
que te recomiendo que uses.

__ http://www.debian.org/

El objetivo de este capítulo es que dispongas rápidamente de un servidor
y un cliente migasfree totalmente funcional, por eso no me voy a extender
en las explicaciones.

Si decides usar otra Distribución GNU/linux de la recomendada tendrás que
conseguir los paquetes apropiados. Accede a http://migasfree.org/repo/dists__
para ver si tu Distribución se encuentra aquí. En caso negativo puedes
generar los paquetes como se indica en :ref:`Empaquetando migasfree`. Ten en cuenta
que las instrucciones de éste capitulo pueden variar segun la Distribución
que elijas.

__ http://migasfree.org/repo/dists

   .. note::

      Usa una máquina virtual de virtualbox__ realizando la instalación
      mínima por red de Debian 7 para ver el funcionamiento de migasfree
      y familiarizarte con él antes de poner a :ref:`Migasfree en producción`


__ https://www.virtualbox.org/

Instalando el servidor
======================

Instalando y configurando Postgresql
------------------------------------

Migasfree puede trabajar con las mismas bases de datos que Django, pero
nosotros recomendamos usar Postgresql, una base de datos de código
libre y alta calidad, con un rendimiento excelente.

Empieza instalando la base de datos ``Postgresql`` y su módulo de Python:

  .. code-block:: none

    # apt-get install postgresql python-psycopg2

Edita el fichero de configuración de la autenticación de
Postgresql para permitir al usuario migasfree autenticarse mediante
password, añadiendo la siguiente línea a
``/etc/postgresql/9.1/main/pg_hba.conf``:

  .. code-block:: none

    # TYPE  DATABASE        USER            ADDRESS       METHOD
    local   all             migasfree                     password


Reinicia el servicio ``postgresql``:

  .. code-block:: none

    # service postgresql restart

Crea un usuario llamado ``migasfree`` en ``Postgresql`` con el siguiente
comando,  introduciendo ``migasfree`` como contraseña para no tener que
configurar nada:

  .. code-block:: none

    # su - postgres -c "createuser -S -d -R -E -P migasfree"
    Ingrese la contraseña para el nuevo rol:
    Ingrésela nuevamente:


Instalación del paquete migasfree-server
----------------------------------------

Para añadir el repositorio que contiene los paquetes necesarios para
debian 7, crea el fichero ``/etc/apt/sources.list.d/migasfree.list``
con el siguiente contenido:

  .. code-block:: none

    deb http://migasfree.org/repo debian7 PKGS

Actualiza las listas de paquetes e instala el paquete migasfree-server:

  .. code-block:: none

    # apt-get update
    # apt-get install migasfree-server

Como aún no hemos creado la base de datos aparecerá el siguiente error:

  .. code-block:: none

    psycopg2.OperationalError: FATAL:  no existe la base de datos <<migasfree>>


Creación de la Base de datos de migasfree
-----------------------------------------

Para finalizar ejecuta el siguiente comando que crea las tablas en la
base de datos migasfree desde cero y configura el servidor web Apache:

  .. code-block:: none

    # migasfree-server-from-scratch

.. warning::

      Utiliza este comando sólo una vez, ya que cada vez que lo ejecutas
      se borra y se crea la base de datos desde cero.

Comprobando el servidor
-----------------------

En un navegador web accede a la dirección del servidor. Si todo ha
ido bien verás la figura 5.1.

.. only:: not latex

   .. figure:: graphics/chapter05/login.png
      :scale: 25
      :alt: Acceso al servidor migasfree.

      figura 5.1. Acceso al servidor migasfree.


.. only:: latex

   .. figure:: graphics/chapter05/login.png
      :scale: 50
      :alt: Acceso al servidor migasfree.

      Acceso al servidor migasfree.




Haz login con el usuario "admin" y password "admin" y verás algo
parecido a la figura 5.2.

.. only:: not latex

   .. figure:: graphics/chapter05/status.png
      :scale: 40
      :alt: Estado del servidor.

      figura 5.2. Estado del servidor.


.. only:: latex

   .. figure:: graphics/chapter05/status.png
      :scale: 80
      :alt: Estado del servidor.

      Estado del servidor.


Instalando el cliente
=====================

Instalando el paquete migasfree-client
--------------------------------------
Ahora instala el cliente migasfree sobre la misma máquina donde has
instalado el servidor. Para ello actualiza la lista de paquetes e
instala el paquete migasfree-client:

  .. code-block:: none

    # apt-get update
    # apt-get install migasfree-client

Configuración mínima del cliente
--------------------------------

Edita el fichero ``/etc/migasfree.conf`` y descomenta la variable ``Server``
asignándola con la direccion del servidor migasfree.

  .. code-block:: none

    Server = miservidor


Registrando el cliente
----------------------

Ejecuta el comando:

  .. code-block:: none

    # migasfree -u

te devolverá una salida parecida a esta:

  .. code-block:: none

    root@debian7:~# migasfree -u
    Sesión gráfica no detectada
    Versión de migasfree client: 3.1

    Opciones de ejecución:
        Versión: debian-7.0
        Servidor: 192.168.92.133
        Proxy: None
        Certificado SSL: None
        Package Proxy Cache: None
        Depuración: False
        Nombre del ordenador: debian7
        GUI detallado: True
        Usuario gráfico: root
        PMS: apt-get

    Autoregistrando ordenador...
    ¡Clave /root/.migasfree-keys/migasfree-client.pri creada!
    ¡Clave /root/.migasfree-keys/migasfree-server.pub creada!

    ******************* Conectando al servidor migasfree... ********************
    ***************************** Correcto

    ************************ Obteniendo propiedades... *************************
    ***************************** Correcto

    ************************** Evaluando atributos... **************************
    VER: debian-7.0

    ALL: ALL SYSTEMS

    IP: 192.168.92.133

    NET: 192.168.92.0/24

    PCI: 8086:1237~Host bridge: Intel Corporation 440FX - 82441FX PMC [Natoma] ...

    PLT: Linux

    HST: debian7

    USR: root~root


    ************************** Subiendo atributos... ***************************
    ***************************** Correcto

    *************************** Ejecutando fallas... ***************************
    LOW_HOME_PARTITION_SPACE:
    LOW_SYSTEM_PARTITION_SPACE:

    **************************** Subiendo fallas... ****************************
    ***************************** Correcto

    ************************* Creando repositorios... **************************
    ***************************** Correcto

    ************* Obteniendo los metadatos de los repositorios... **************
    Des:1 http://ftp.es.debian.org wheezy Release.gpg [1.672 B]
    Ign http://migasfree.org debian7 Release.gpg
    Des:2 http://ftp.es.debian.org wheezy-updates Release.gpg [1.571 B]
    Obj http://security.debian.org wheezy/updates Release.gpg
    ...
    Des:11 http://ftp.es.debian.org wheezy-updates/main Translation-en [14 B]
    Descargados 16,3 MB en 15seg. (1.025 kB/s)
    Leyendo lista de paquetes... Hecho
    ***************************** Correcto

    ************************ Desinstalando paquetes... *************************
    ***************************** Correcto

    ******************* Instalando paquetes obligatorios... ********************
    ***************************** Correcto

    ************************* Actualizando paquetes... *************************
    DEBIAN_FRONTEND=noninteractive /usr/bin/apt-get --assume-yes --force-yes ...
    Leyendo lista de paquetes...
    Creando árbol de dependencias...
    Leyendo la información de estado...
    0 actualizados, 0 se instalarán, 0 para eliminar y 0 no actualizados.

    ***************************** Correcto

    ****************** Subiendo el inventario del software... ******************
    ***************************** Correcto

    ************************* Operaciones completadas **************************
    root@debian7:~#

Comprobando el estado del servidor
==================================

Comprueba los datos que se han recogido accediendo al servidor con tu
navegador web.

* En ``Estado`` tendrás 2 ``Notificaciones`` (figura 5.3):

    * La primera te notifica que el ordenador ``1`` ha dado de alta la
      plataforma ``Linux``

    * La segunda notificación te dice que el ordenador ``1`` ha añadido
      la version ``debian-7.0``

    .. only:: not latex

       .. figure:: graphics/chapter05/notifications.png
          :scale: 40
          :alt: Notificaciones.

          figura 5.3. Notificaciones.

    .. only:: latex

       .. figure:: graphics/chapter05/notifications.png
          :scale: 80
          :alt: Notificaciones.

          Notificaciones.





* Accede a ``Auditoría - Datos - Ordenadores`` (figura 5.4) y mira:

    * Los datos del ordenador ``1`` (pulsando en el número 1)

    * Su ``último login``, accediendo a ``mostrar atributos`` para ver
      los atributos que ha enviado el cliente.

    * Su hardware.

    .. only:: not latex

       .. figure:: graphics/chapter05/computers.png
          :scale: 40
          :alt: Equipos..

          figura 5.4. Equipos.

    .. only:: latex

       .. figure:: graphics/chapter05/computers.png
          :scale: 80
          :alt: Equipos.

          Equipos..


¡Enhorabuena! Has instalado un servidor migasfree y has registrado en él
tu primer ordenador.

En el siguiente capítulo vas a aprender a hacer el cambio de
configuración software al estilo migasfree.
