=============================
Configurando migasfree-client
=============================

En el capítulo anterior nos hemos centrado en cómo se realiza el proceso
de la GCS. Por esto, el empaquetado que has realizado para configurar el
servidor de migasfree sobre debian 7 ha sido muy sencillo.

En este capítulo vas a empaquetar la configuración del cliente migasfree
para que un ubuntu 12.04 se conecte contra la maquina virtual debian 7
que tienes.

Lo realizarás sobre otra máquina virtual (ubuntu 12.04).

El objetivo de este capítulo es que tengas una visión más avanzada del
empaquetado, realizando un paquete totalmente funcional y que podrás
utilizar en tu organización.

Obteniendo acme-migasfree-client
================================

Al igual que hicimos con la configuración del servidor puedes bajarte
el fuente del paquete que vamos a utilizar de plantilla.

En una máquina virtual con ubuntu 12.04 ejecuta:

  .. code-block:: none

    $ wget http://www.migasfree.org/repo/book/acme-migasfree-client_1.0-1.tar.gz
    $ tar -xzvf acme-migasfree-server_1.0-1.tar.gz

Modificando los metadatos
=========================

Changelogs
----------

Scripts
-------

















