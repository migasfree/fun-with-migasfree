.. _`Empaquetando los paquetes requeridos`:

=============================
Empaquetando proyectos python
=============================

 .. epigraph::

   La diferencia entre el pasado, el presente y el futuro es sólo una ilusión
   persistente.

   -- Albert Einstein

Es muy posible que en la distribución en la que has instalado el servidor migasfree
no encuentres los paquetes que se requieren para instalar el servidor, bien porque
simplemente no están disponibles o bien porque la versión disponible no es
suficientemente reciente como para ejecutar el servidor.

En este capítulo vas a empaquetar ``django`` como ejemplo y el método que
usarás es válido para la mayoría de proyectos escritos en ``python``.


Creación del paquete ``django`` en distros basadas en paquetería ``apt``
========================================================================

Descarga el código del proyecto django cuya versión necesites y descomprímelo:

  .. code-block:: none

    wget https://www.djangoproject.com/download/1.6.2/tarball/ -O Django-1.6.2.tar.gz
    tar xzvf Django-1.6.2.tar.gz
    cd Django-1.6.2

Asegúrate que tienes instalado el paquete python-stdeb:

  .. code-block:: none

    apt-get install python-stdeb

Ahora crea el paquete:

  .. code-block:: none

    python setup.py --command-packages=stdeb.command bdist_deb

En la carpeta ``deb_dist`` tendrás el paquete deb.

Más información en `https://wiki.debian.org/Python/Packaging`__

__ https://wiki.debian.org/Python/Packaging


Creación del paquete ``django`` en distros basadas en paquetería ``rpm``
========================================================================

Descarga el código del proyecto django cuya versión necesites y descomprímelo:

  .. code-block:: none

    wget https://www.djangoproject.com/download/1.6.2/tarball/ -O Django-1.6.2.tar.gz
    tar xzvf Django-1.6.2.tar.gz
    cd Django-1.6.2


Ahora crea el paquete:

  .. code-block:: none

    python setup.py bdist_rpm

En la carpeta ``dist`` tendrás el paquete rpm.

Para más información puedes consultar `http://docs.python.org/2.0/dist/creating-rpms.html`__

__ http://docs.python.org/2.0/dist/creating-rpms.html
