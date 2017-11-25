==================
Probando migasfree
==================

 .. epigraph::

   La unidad es la variedad, y la variedad en la unidad es la ley
   suprema del universo.

   -- Isaac Newton.

Si bien puedes instalar el servidor migasfree en distintas
distribuciones, en este capítulo voy a explicarte como instalarlo sobre
`Debian 8 Jessie`__.

__ http://www.debian.org/

El objetivo es que dispongas rápidamente de un servidor
y un cliente migasfree totalmente funcional, por eso no me voy a extender
en explicaciones.

Si decides usar otra distribución GNU/linux de la recomendada, tendrás que
conseguir los paquetes apropiados. Puedes generar los paquetes como se indica
en :ref:`Empaquetando migasfree`. Ten en cuenta que las instrucciones de este
capítulo pueden variar según la distribución que elijas.

   .. note::

      Usa una máquina virtual de virtualbox__ realizando la instalación
      mínima por red de Debian 8 para ver el funcionamiento de migasfree
      y familiarizarte con él antes de poner a :ref:`Migasfree en producción`


__ https://www.virtualbox.org/

Instalando el servidor
======================

Como ``root``, ejecuta en un terminal:

  .. code-block:: none

    # wget -O - http://migasfree.org/pub/install-server | bash


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
      el servidor deberás cambiar la contraseña de este usuario tal y
      como se indica en :ref:`Migasfree en producción`.

  .. note::

      Otra forma alternativa de instalar un servidor migasfree, y que te recomiendo
      encarecidamente que pruebes, es utilizando **contenedores docker**. Accede a
      https://github.com/migasfree/migasfree-docker y sigue las instrucciones. En
      AZLinux llevamos tiempo utilizando estos contenedores y estamos muy
      satisfechos.


Comprobando el servidor
=======================

En un navegador web accede a la dirección del servidor. Si todo ha
ido bien, verás la figura 5.1.

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


Pulsa en ``iniciar sesión`` y haz login con el nombre de usuario "admin" y
password "admin". Verás algo parecido a la figura 5.2. Observa como arriba a la
derecha pone ``alertas 0``. Esto nos indica que todo está bien.

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
instalado el servidor. Para ello, actualiza la lista de paquetes e
instala el paquete migasfree-client:

  .. code-block:: none

    # wget -O - http://migasfree.org/pub/install-client | bash



Registrando el cliente
----------------------

Ejecuta el comando:

  .. code-block:: none

    # migasfree -u

te devolverá una salida parecida a esta:

  .. code-block:: none

    root@debian:/home/tux# migasfree -u
    Sesión gráfica no detectada
    Versión de migasfree client: 4.14

    Opciones de ejecución: /etc/migasfree.conf
        Versión: debian-8.7
        Servidor: localhost
        Actualizar paquetes automáticamente: True
        Proxy: None
        Certificado SSL: None
        Proxy caché de paquetes: None
        Depuración: False
        Nombre del ordenador: debian
        GUI detallado: True
        PMS: apt-get

        Usuario gráfico: root

    Autoregistrando ordenador...
    ¡Clave /var/migasfree-client/keys/localhost/debian-8.7.pri creada!
    ¡Clave /var/migasfree-client/keys/localhost/server.pub creada!
    ¡Clave /var/migasfree-client/keys/localhost/repositories.pub creada!

    ******************* Conectando al servidor migasfree... ********************
    ***************************** Correcto

    ************************ Obteniendo propiedades... *************************
    ***************************** Correcto

    ************************** Evaluando atributos... **************************
    SET: ALL SYSTEMS

    PCI: 8086:1237~Host bridge: Intel Corporation 440FX - 82441FX PMC [Natoma] (rev 02) ,8086:7000~ISA bridge: Intel Corporation 82371SB PIIX3 ISA [Natoma/Triton II] ,8086:7111~IDE interface: Intel Corporation 82371AB/EB/MB PIIX4 IDE (rev 01) ,80ee:beef~VGA compatible controller: InnoTek Systemberatung GmbH VirtualBox Graphics Adapter ,8086:100e~Ethernet controller: Intel Corporation 82540EM Gigabit Ethernet Controller (rev 02) ,80ee:cafe~System peripheral: InnoTek Systemberatung GmbH VirtualBox Guest Service ,106b:003f~USB controller: Apple Inc. KeyLargo/Intrepid USB ,8086:7113~Bridge: Intel Corporation 82371AB/EB/MB PIIX4 ACPI (rev 08) ,8086:265c~USB controller: Intel Corporation 82801FB/FBM/FR/FW/FRW (ICH6 Family) USB2 EHCI Controller ,8086:2829~SATA controller: Intel Corporation 82801HM/HEM (ICH8M/ICH8M-E) SATA Controller [AHCI mode] (rev 02) ,

    IP: 10.0.2.15

    HST: debian

    NET: 10.0.2.0/24

    PLT: Linux

    USR: root~root

    VER: debian-8.7


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
    Ign http://ftp.es.debian.org jessie InRelease
    Obj http://ftp.es.debian.org jessie-updates InRelease
    Obj http://security.debian.org jessie/updates InRelease
    Obj http://ftp.es.debian.org jessie Release.gpg
    Obj http://ftp.es.debian.org jessie-updates/main Sources
    Obj http://security.debian.org jessie/updates/main Sources
    Des:1 http://ftp.es.debian.org jessie-updates/main amd64 Packages/DiffIndex [6.916 B]
    Obj http://ftp.es.debian.org jessie Release
    Obj http://security.debian.org jessie/updates/main amd64 Packages
    Obj http://ftp.es.debian.org jessie/main Sources
    Obj http://ftp.es.debian.org jessie/main amd64 Packages
    Descargados 6.916 B en 1s (5.169 B/s)
    Leyendo lista de paquetes... Hecho
    ***************************** Correcto

    ************************ Desinstalando paquetes... *************************
    ***************************** Correcto

    ******************* Instalando paquetes obligatorios... ********************
    ***************************** Correcto

    ************************* Actualizando paquetes... *************************
    DEBIAN_FRONTEND=noninteractive /usr/bin/apt-get -o APT::Get::Purge=true -o Dpkg::Options::=--force-confdef -o Dpkg::Options::=--force-confold -o Debug::pkgProblemResolver=1 --assume-yes --force-yes --auto-remove dist-upgrade
    Leyendo lista de paquetes...
    Creando árbol de dependencias...
    Leyendo la información de estado...
    0 actualizados, 0 nuevos se instalarán, 0 para eliminar y 0 no actualizados.

    ***************************** Correcto

    ****************** Subiendo el inventario del software... ******************
    ***************************** Correcto

    *************** Capturando información sobre el hardware... ***************
    ***************************** Correcto

    **************** Enviando información sobre el hardware... ****************
    ***************************** Correcto

    ************************* Operaciones completadas **************************

Comprobando el estado del servidor
==================================

Comprueba los datos que se han recogido accediendo al servidor con tu
navegador web.

* Fíjate ahora que tienes 2 ``Alertas`` (figura 5.3). Pulsa sobre ellas y luego
sobre ``2 alertas por comprobar``:

    * La primera te notifica que el ordenador ``CID-1`` ha dado de alta la
      plataforma ``Linux``

    * La segunda notificación te dice que el ordenador ``CID-1`` ha añadido
      la version ``debian-x.x``

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

    * Los datos del ordenador ``CID-1`` (pulsando sobre CID-1)

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

  .. note::

      CID es un acrónimo de ``Computer IDentificator``. Es un número que el
      servidor asigna a cada ordenador para identificarlo. Es imposible tener dos
      ordenadores con el mismo CID.

  .. note::

      El símbolo que aparece a la izquierda del CID (el corazón) indica el
      ``estado`` en el que encuentra el ordenador.



¡Enhorabuena! Has instalado un servidor migasfree y has registrado en él
tu primer ordenador.

En el siguiente capítulo vas a aprender a hacer el cambio de
configuración software al estilo migasfree.
