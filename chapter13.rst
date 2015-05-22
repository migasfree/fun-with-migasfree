========================
Creando tu propia Distro
========================

 .. epigraph::

   No tratéis de guiar al que pretende elegir por sí su propio camino.

   -- William Shakespeare

Una Distro no es más que un conjunto de software seleccionado y preparado
para instalarse fácilmente.

Existen `herramientas`__ que te permiten personalizar una Distribución Linux
fácilmente sin grandes complicaciones, y también puedes crear tu
`Linux desde cero`__, eso sí armándote de paciencia.

__ http://www.techradar.com/news/software/operating-systems/10-scripts-to-create-your-own-linux-distribution-665247
__ http://www.linuxfromscratch.org/


Pero como te decía, para crear tu Distribución personalizada debes:

    * Seleccionar el software que incluirás en ella.

    * Preparar un sistema sencillo para instalar todo ese software.

En este capítulo te describo diferentes opciones que he utilizado
para realizar estas dos tareas.

La selección de paquetes
========================

La idea principal al trabajar con migasfree es que todo debe ser empaquetado,
incluida la personalización del software. Así que debes elegir que software
incluirá tu Distribución y crear los paquetes que la personalicen.

El método que te expongo a continuación es muy versatil, y es el de utilizar
migasfree para especificar esta selección de paquetes.

Se trata de usar los campos del ``Repositorio``:

    * ``default preinclude packages``. Lista de paquetes que configuran repositorios
      externos.

    * ``default include packages``: Lista de paquetes a instalar.

    * ``default exclude packages``: Lista de paquetes a desinstalar.

y asignar al ``Repositorio`` el ``Atributo`` ``SET-ALL SYSTEMS``

No tienes porque indicar todos los paquetes. Como vamos a partir de una
Distribución generalista como Debian, Ubuntu, RedHat, etc. indicamos sólo los
paquetes que queremos añadir o eliminar a la Distro.

También puedes hacer una selección de los paquetes que compondrían unos "sabores",
y en vez de usar el ``Atributo`` ``SET-ALL SYSTEMS``, crear una ``Etiqueta`` por sabor
y asignarla en diferentes ``Repositorios``

La creación de etiquetas la viste en :ref:`La configuración del sistema migasfree`


La instalación de tu Distribución
=================================

Ahora que has elegido y creado uno o varios ``Repositorios`` en migasfree con
los paquetes que debe llevar tu Distribución, es el momento de ver varios
métodos para instalar tu Distribución personalizada y controlada desde un
servidor migasfree.

El método de "andar por casa"
-----------------------------

Recomendado si no quieres complicarte la vida y tienes pocos equipos en los que
instalar tu Distro:

    1. Instala la Distribución generalista en el equipo.

    2. Instala y configura el cliente migasfree. Si es preciso registra el ordenador
       mediante ``migasfree --register``.

    3. Ejecuta ``migasfree-tags --set``.


Generando un Live/CD
--------------------

Es el método recomendado si la instalación la puede realizar cualquier persona.
Se trata de hacer básicamente lo mismo que en el método anterior pero sustituyendo
el primer paso por el empleo de un Live/CD en un entorno "chroot".

    1. Prepara un entorno chroot con el Live/CD de partida.

    2. Instala y configura el cliente migasfree en el entorno chroot. Si es
       preciso registra el ordenador mediante ``migasfree --register``.

    3. Ejecuta ``migasfree-tags --set`` dentro del entorno.

    4. Finalmente genera una imagen iso del entorno

Puedes ver un ejemplo de cómo se hace en vitalinux con `vx-create-iso`__.

__ http://github.com/vitalinux/vx-create-iso


Clonación de imagen
-------------------

Es el método que usamos en AZLinux y está recomendado si tienes muchos equipos
y eres tú quien hace las instalaciones.

    1. Instala la Distribución generalista en un equipo que hará de "master".

    2. Instala y configura el cliente migasfree. Si es preciso registra el ordenador
       mediante ``migasfree --register``.

    3. Ejecuta ``migasfree-tags --set``.

    4. Prepara el equipo para clonar y crea una imagen para su clonación.

    5. Clona la imagen en los equipos.


Reinstalando la selección de paquetes
=====================================

Una vez instalada tu Distro, en cualquier momento podrás cambiar de sabor
ejecutando otra vez ``migasfree-tags --set``. Observa que has podido decidir
cambiar la selección de paquetes en migasfree entre tanto, esto te permite ir
probando tu Distro fácilmente mientras aún la estás definiendo.

