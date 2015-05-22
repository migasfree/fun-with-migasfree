==================
Probando migasfree
==================
 .. epigraph::

   La unidad es la variedad, y la variedad en la unidad es la ley
   suprema del universo.

   -- Isaac Newton.

Si bien puedes instalar el servidor migasfree en distintas
distribuciones, en este capítulo voy a explicarte como instalarlo sobre
`Debian 7 Wheezy`__.

__ http://www.debian.org/

El objetivo de este capítulo es que dispongas rápidamente de un servidor
y un cliente migasfree totalmente funcional, por eso no me voy a extender
en explicaciones.

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

Para añadir el repositorio que contiene los paquetes necesarios para
debian 7, ejecutaremos la siguiente instrucción:

  .. code-block:: none

    # echo "deb http://migasfree.org/repo debian7 PKGS" > /etc/apt/sources.list.d/migasfree.list

Actualiza las listas de paquetes e instala el paquete migasfree-server:

  .. code-block:: none

    # apt-get update
    # apt-get install migasfree-server


  .. note::

      Al instalar el paquete del servidor migasfree se añade al sistema
      el fichero ``/etc/apache2/conf.d/migasfree.conf``. Este fichero
      contiene la configuración del servidor web.


  .. note::

      Al instalar el paquete del servidor migasfree se crea el usuario
      ``migasfree`` en Postgresql con password ``migasfree`` y se añade al
      fichero ``/etc/postgresql/9.1/main/pg_hba.conf`` la línea
      ``'local all migasfree password'`` para permitir al usuario migasfree
      autenticarse mediante password. Recuerda que para poner en producción
      el servidor deberás cambiar la contraseña de éste usuario tal y
      como se indica en :ref:`Migasfree en producción`.



Comprobando el servidor
=======================

En un navegador web accede a la dirección del servidor. Si todo ha
ido bien verás la figura 5.1.

.. only:: not latex

   .. figure:: graphics/chapter05/login.png
      :scale: 50
      :alt: Acceso al servidor migasfree.

      figura 5.1. Acceso al servidor migasfree.


.. only:: latex

   .. figure:: graphics/chapter05/login.png
      :scale: 100
      :alt: Acceso al servidor migasfree.

      Acceso al servidor migasfree.


Haz login con el usuario "admin" y password "admin" y verás algo
parecido a la figura 5.2. Observa como arriba a la derecha pone ``alertas 0``.
Esto nos indica que todo esta bien.

.. only:: not latex

   .. figure:: graphics/chapter05/status.png
      :scale: 50
      :alt: Estado del servidor con 0 alertas.

      figura 5.2. Estado del servidor con 0 alertas.


.. only:: latex

   .. figure:: graphics/chapter05/status.png
      :scale: 100
      :alt: Estado del servidor con 0 alertas.

      Estado del servidor con 0 alertas.



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
        Versión: debian-7.4
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
    VER: debian-7.4

    SET: ALL SYSTEMS

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

* Fíjate ahora que en las ``Alertas`` tendrás 2 ``Notificaciones`` (figura 5.3):

    * La primera te notifica que el ordenador ``1`` ha dado de alta la
      plataforma ``Linux``

    * La segunda notificación te dice que el ordenador ``1`` ha añadido
      la version ``debian-7.x``

    .. only:: not latex

       .. figure:: graphics/chapter05/notifications.png
          :scale: 50
          :alt: Notificaciones.

          figura 5.3. Notificaciones.

    .. only:: latex

       .. figure:: graphics/chapter05/notifications.png
          :scale: 100
          :alt: Notificaciones.

          Notificaciones.



* Accede a ``Datos - Ordenadores`` y observa: (figura 5.4)

    * Los datos del ordenador ``1`` (pulsando en el número 1)

    * Su ``login``, para ver los atributos que ha enviado el cliente.

    * Su ``hardware``.

    .. only:: not latex

       .. figure:: graphics/chapter05/computers.png
          :scale: 50
          :alt: Ordenadores

          figura 5.4. Ordenadores.

    .. only:: latex

       .. figure:: graphics/chapter05/computers.png
          :scale: 100
          :alt: Ordenadores.

          Ordenadores.


¡Enhorabuena! Has instalado un servidor migasfree y has registrado en él
tu primer ordenador.

En el siguiente capítulo vas a aprender a hacer el cambio de
configuración software al estilo migasfree.
