====================
Acerca de este libro
====================

Licencia y Copyright
====================

    Fun with migasfree

    Copyright (C)  2013  Alberto Gacías and contributors.
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the :ref:`GNU Free Documentation License`, Version 1.3
    or any later version published by the Free Software Foundation;
    with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
    A copy of the license is included in the section entitled "GNU
    Free Documentation License".

.. raw:: latex

   \newpage

Presentación
============
.. only:: not latex

   .. figure:: graphics/chapter01/fun.png
      :scale: 30
      :alt: Fun with migasfree.

.. only:: latex

   .. figure:: graphics/chapter01/fun.png
      :scale: 60
      :alt: Fun with migasfree.


*Hola. Soy Alberto Gacías. Bienvenidos al primer capítulo de "Alberto
Gacías presenta diversión con migasfree".
Durante las próximas páginas, usted y yo vamos a explorar el dinámico mundo
de la migasfreelogía.* [#f1]_

.. [#f1] Recordando a Sheldon Cooper en "Fun with Flags" en la serie The Big Bang Theory.

.. raw:: latex

   \newpage

`Migasfree`__ es una de las herramientas que estamos utilizando con éxito
en `AZLinux`__, el proyecto de migración a escritorio libre del `Ayuntamiento
de Zaragoza`__.

__ http://migasfree.org
__ http://zaragozaciudad.net/azlinux/
__ http://zaragoza.es

Se ocupa principalmente del proceso de la liberación de software y
de la posterior auditoría de los cambios producidos en los equipos como
consecuencia de esa liberación.

Este software se ha hecho indispensable en nuestro día a día,
y creo que es una buena solución para personalizar y administrar
escritorios de forma eficaz.

Este libro te introducirá en el uso de migasfree y lo escribo a medida
que mejoramos el software, con lo que si te lo descargaste hace tiempo
quizás ya esté obsoleto, tenlo en cuenta.

Estructura
==========

Conociendo migasfree
--------------------

En el segundo capítulo de este libro, repasaremos la Gestión de la
Configuración del Software. Conocer los aspectos básicos de este proceso
de la Ingeniería del Software te dará una visión de conjunto que
considero esencial porque es precisamente aquí donde se integra
migasfree.

En el capítulo tercero te explicaré las dificultades a las que un
administrador de escritorios va a encontrarse y cómo se pueden
sortear de forma sencilla basándome en la experiencia adquirida en
AZLinux.

Podrás conocer la historia, características y componentes que utiliza
migasfree en el cuarto capítulo.

En el capítulo quinto y sexto te explicaré como probar un servidor y
cliente migasfree con la configuración mínima para que puedas verlos en
funcionamiento cuanto antes.

Guía de Uso
-----------

Del capítulo 7 al 11 irás conociendo tanto el cliente como el servidor migasfree
más en detalle.

Desplegando migasfree en producción
-----------------------------------
Comprende los capítulos 12 y 13 en donde tratarás los aspectos a tener
en cuenta si quieres utilizar migasfree en un entorno de producción.

Resolución de problemas y referencias
-------------------------------------

En los capítulos 14 y 15 se tratan las FAQs y la resolución de problemas.

En los capítulos 16 y 17 podrás consultar los ajustes necesarios para
configurar correctamente tanto el servidor migasfree como los clientes.

El 18 detalla la API y en el 19 y 20 hay intrucciones para empaquetar
migasfree en cualquier Distribución.

A quién va dirigido
===================

Este libro puede serte útil si eres administrador de escritorios (y/o servidores)
y quieres personalizar y administrar de forma eficaz tus equipos
manteniendo la integridad de los sistemas.

Agradecimientos
===============

Detrás de cada proyecto hay personas que lo hacen posible, manteniendo,
animando, corrigiendo, colaborando, apoyando...

Deseo expresar en primer lugar mi gratitud a Eduardo Romero. Me dio
el estímulo necesario para liberar la primera versión de migasfree,
haciendo visible este proyecto en internet. También aportó la primera y
única donación que ha recibido migasfree (aunque fuera por una apuesta
perdida, no se lo tuve en cuenta y fue muy bien recibida).

A Jose Antonio Chavarría, compañero de fatigas (y alegrías), también
me siento agradecido. Ha sido y es piedra angular en migasfree. Ha
mejorado sustancialmente el proyecto reescribiendo el código spaguetti a
buen código [#f2]_, aportando ideas y soluciones. Me tranquiliza cuando
quiero correr en exceso, y es el guardián de la simplicidad de migasfree.

.. [#f2] Proceso conocido muy localmente como chavarrización.

A Jesús González por su empeño en crear equipos de trabajo donde las
personas nos sentimos a gusto trabajando.

Y a todo el grupo de Asistencia a Usuarios del Ayuntamiento de Zaragoza,
especialmente al equipo de Software Libre. Disfruto trabajando con ellos
y me hacen reír a diario.

.. only:: not latex

   .. figure:: graphics/chapter01/pioneers.png
      :scale: 80
      :alt: Grupo de Software del Ayuntamiento de Zaragoza.

      Grupo de Software Libre del Ayuntamiento de Zaragoza.

.. only:: latex

   .. figure:: graphics/chapter01/pioneers.png
      :scale: 80
      :alt: Grupo de Software del Ayuntamiento de Zaragoza.

      Grupo de Software Libre del Ayuntamiento de Zaragoza.

Acerca de mí
============

De joven me atraía la programación. Estudié electrónica, y aquí me
enseñaron a programar en código máquina el microcontrolador 8751.

Trabajé como electrónico mis primeros años laborales y poco después, con
el boom de la informática personal, empecé a desarrollar aplicaciones de
todo tipo.

Actualmente trabajo como técnico informático en el equipo de Software
Libre del Ayuntamiento de Zaragoza desarrollando y manteniendo
AZLinux, el escritorio libre que usamos los trabajadores municipales.

Aún me gusta cacharrear con transistores, condensadores, circuitos
integrados, leds... y enseñar lo poco que recuerdo de todo aquello Jesús.
A los dos nos gusta jugar con arduino__ scratch__ y s4a__.

__ http://www.arduino.cc/

__ http://seaside.citilab.eu/scratch?_s=uUPtRoAV9JudiOLQ&_k=kzuRwrWwE3SbPt4N

__ http://seaside.citilab.eu/scratch?_s=uUPtRoAV9JudiOLQ&_k=js6Ukm-xH8NtlSiD

Creo que el movimiento del software libre es, junto con otros, una
esperanza para que el Conocimiento vuelva a ser producido
por la sociedad y para la sociedad, en contraposición al Conocimiento creado,
comercializado y controlado por organizaciones y que en ocasiones
causa un perjuicio a la sociedad.

Me encanta mirar el cielo en las noches de verano de Peñiscola, la cerveza,
las migas, y los huevos rotos.

También me gusta escuchar música, el olor a tierra mojada y que me hagan
reír con cualquier tontada.

Amo a Patricia, y a Jesús nuestro hijo.

Enlaces
=======

Versión html: http://migasfree.org/repo/book/html/index.html

Versión pdf: http://migasfree.org/repo/book/pdf/fun-with-migasfree.pdf

Codigo Fuente: http://github.com/migasfree/fun-with-migasfree.

Twitter: `@migasfree`__ `@albertogacias`__

__ https://twitter.com/migasfree
__ https://twitter.com/albertogacias
