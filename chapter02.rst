====================================
Gestión de la Configuración Software
====================================

   .. epigraph::

      Nada es permanente a excepción del cambio

      -- Heráclito de Éfeso.

Estamos acostumbrados a actualizar periódicamente nuestras
aplicaciones: los sistemas se hacen obsoletos rápidamente, aparecen
nuevas tecnologías, hay errores que son resueltos, surgen nuevas
necesidades. Sin importar en qué momento del ciclo de vida del
sistema nos encontremos, el sistema cambiará, y el deseo de cambiarlo
persistirá a lo largo de todo el ciclo de vida. [#f1]_

.. [#f1] Primera ley de la Ingeniería de Sistemas, Software
         Configuration Management, Bersoff, Henderson & Siegel,
         Prentice-Hall, 1980

Por tanto, el cambio en el software es **inevitable** y
**deseable** que ocurra.

Es inevitable porque los desarrolladores cometemos errores
y es mediante una modificación como los corregimos. A éste
tipo de cambios los llamamos **correctivos**.

Por otro lado el cambio es deseable ya que a menudo queremos incorporar
nuevas funcionalidades al software o mejorar aquellas que ya existían.
Mediante los cambios **evolutivos** es como mejoramos el software.

El cambio genera **confusión** e incertidumbre y se produce desde que
concebimos, construímos y tambien mientras mantenemos un proyecto
software.

El gran reto reside precisamente en gestionar de forma controlada
dichos cambios usando alguna estrategia que los favorezca y facilite.

De esto trata precisamente la Gestión de la Configuración Software (GCS),
un proceso de la Ingeniería del Software que identifica, hace
seguimiento y controla cada uno de los cambios que se producen en los
sistemas.

Objetivo
========

El objetivo de la GCS es **conservar la integridad** de los sistemas
frente a los cambios.

Un sistema será íntegro frente al cambio si:

* Mantiene correctamente las **relaciones** entre los distintos cambios a
  medida que se van produciendo (el típico problema de dependencias
  entre elementos).

* Permite la **auditoría** de cambios (conocimiento del estado de un
  sistema al que se le han ido aplicando cambios sucesivamente).


El proceso
==========

El proceso de la GCS es un conjunto de actividades que nos permitirá
garantizar dicha integridad, y que podemos resumir en:

* Petición de cambio

* Cambio

* Liberación.

Peticion de cambio
------------------

Cuando se nos reporta un error o una petición de mejora, lo primero que
hacemos es identificar el elemento de configuración software (ECS) al
que se refiere.

Un ECS es cualquier objeto software sometido a la GCS. Puede ser un
manual de usuario, una especificación, un conjunto de datos para
realizar tests, una aplicación, una librería, incluso las
herramientas que se usan para realizar dichos cambios, etc.

Una vez identificado el ECS se registra la petición de cambio.

Las herramientas típicas para registrar y hacer el seguimiento del
cambio son los denominados ``gestores de proyectos`` (Redmine,
Bugzilla, Tracker, etc. )

Cada petición de cambio es analizada más tarde pudiendo ser aceptada o
rechazada. Si es rechazada se avisa al informador y se cierra la petición;
si es aceptada se asigna la petición a alguien para que realice dicho cambio.

Cambio
------

El cambio es la actividad que modifica el ECS, generando una nueva
versión del ECS.

En esta actividad se utilizan un conjunto muy diverso de herramientas,
desde procesadores y editores de texto, sistemas de control de versiones,
entornos de desarrollo integrados (IDE), depuradores, compiladores...

Liberación
----------

La liberación es la actividad de situar la nueva versión del ECS
generada, en un repositorio o almacén para que posteriormente los
clientes del ECS puedan acceder a él e instalarlo.


Elemento de Configuracion Software
==================================

Si observamos cómo los diferentes proyectos de Software Libre realizan
la GCS, vemos que realizan las actividades mencionadas liberando
finalmente el código fuente del proyecto en internet.

Estos proyectos trabajan con distintos tipos de ECS (.png, .txt, .py,
.c, .bin, etc.) usando los Sistemas de Control de Versiones junto con
las plataformas de desarrollo colaborativo como sourceforge.net,
github.com, etc.

Este código fuente será posteriormente compilado por los mantenedores de
las Distribuciones GNU/Linux (Fedora, Red Hat, Debian, Ubuntu, etc.)
realizando su propia GCS, pero a diferencia de los primeros, las
Distribuciones GNU/Linux sólo trabajan sobre un único tipo de ECS:
**el paquete**, donde introducirán el programa ya compilado.

Este simple hecho permite garantizar la integridad frente a los cambios
de forma eficaz y sencilla como veremos a continuación.

El paquete
----------
Un paquete es un contenedor que encapsula un conjunto de ECS liberados
por un determinado proyecto, junto a su metainformación.

Contendrá, por tanto, el programa compilado para una determinada
Distribución y arquitectura, más un conjunto amplio de información como
puede ser:

* El autor del programa.

* La dirección del repositorio del proyecto.

* La versión del ECS.

* La arquitectura.

* El nombre y dirección e-mail del empaquetador.

* La fecha de empaquetado.

* El Nombre del equipo en que se produjo el empaquetado.

* Una descripción corta del contenido del paquete.

* Una descripción larga.

Pero además suelen incluir:

* Código a ejecutar antes y después de:

   - Instalar.

   - Actualizar.

   - Eliminar el paquete.

* Dependencias con otros paquetes.

Una vez que un mantenedor de una Distribución GNU/Linux ha
creado un paquete, lo libera poniéndolo en un repositorio público
a disposición de los clientes.

Puesta en producción
--------------------

Los encargados de aplicar los cambios son los programas denominados
**gestores de paquetes** tales como yum, zypper ó apt.

Un gestor de paquetes es un programa que permite poner en producción los
cambios que han sido liberados en los repositorios.

La actualización de un equipo se realiza comparando las versiones de los
paquetes instalados con los paquetes de los repositorios públicos,
detectando los que han aumentado su versión, resolviendo sus
dependencias y finalmente, si no hay conflictos, obtienen desde los
repositorios los paquetes necesarios.

Una vez han descargado los paquetes, dan órdenes a los **backends**
(rpm, dpkg, etc.) para que se produzca la desinstalación de los paquetes
antigüos y la instalación de los nuevos.

Los backends abren el paquete, y grosso modo:

1. Extraen los ficheros del programa copiándolos en el sistema, y
ejecutando además el código programado para antes y después de la
actualización.

2. La metainformación es extraída del paquete y se almacena en la base
de datos del backend.

Decía Ian Murdock, fundador de Debian, que el gran aporte del software
libre a la industria ha sido precisamente la invención del sistema de
paquetería (paquete, repositorio, gestor de paquetes).

Y no es para menos, ya que este sistema nos proporciona los dos
requisitos necesarios que garantizan la integridad frente a los cambios:

1. El control de dependencias, mediante el gestor de paquetes.

2. La auditoría, mediante las consultas a la base de datos del backend.

   .. note::

      Si estás acostumbrado a instalar programas mediante el típico
      “./configure, make, install”, tienes que ser consciente de que estás
      rompiendo la integridad frente a los cambios, ya que la base de datos
      del backend no es actualizada con este procedimiento. Todo lo que
      no sea instalar programas mediante el gestor de paquetes o el
      backend rompe la integridad.
