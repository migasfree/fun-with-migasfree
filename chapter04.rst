============================
Características de migasfree
============================

 .. epigraph::

   Las cosas no se dicen, se hacen, porque al hacerlas se dicen solas.

   -- Woody Allen.

El nacimiento de migasfree
==========================

En el año 2005 todos grupos políticos del Ayuntamiento de Zaragoza
manifestaron por unanimidad en pleno de gobierno municipal apoyar las
políticas de uso de Software Libre y, en concreto, el fomento de los
programas de SL en el entorno de escritorio del funcionario municipal.
La Dirección General de Ciencia y Tecnología asume, inicia y potencia
este importante reto. [#f5]_

.. [#f5] Eduardo Romero Moreno, `Migración Escritorio Software Libre`__, 2011

__ http://www.zaragoza.es/contenidos/azlinux/migracionescritoriosl.pdf

Este proyecto se planificó en tres etapas:


* Primera: Migrar a aplicaciones que presentaban un impacto bajo sobre
  usuarios y técnicos en el SO actual.

* Segunda: Migrar la plataforma ofimática  Microsoft Office 97 por la
  suite libre OpenOffice.

* Tercera: Sustituir el SO Windows XP por un sistema operativo basado en
  Linux. Esta etapa se inició en 2008 y todavía sigue abierta.

Para iniciar la tercera etapa se tuvieron que realizar los primeros
prototipos de lo que llegaría a ser la primera version de AZLinux.
En estos prototipos la personalización se realizaba manualmente en un
equipo cuya imagen del disco duro nos servía para clonarla en otros
equipos y hacer las pertinentes pruebas.

En aquel tiempo aprendimos a empaquetar y empezamos a introducir nuestra
personalización en nuestros propios paquetes. La ventaja frente a la
personalización manual era muy significativa.

Con los primeras migraciones reales, nos surgió la necesidad de actualizar
nuestros paquetes y despues de probar sin éxito Zenworks for Linux,
decidimos crear nuestros propios repositorios de paquetes. Quisimos
emular lo que ya estabamos haciendo con los escritorios XP, esto es,
distribuir software basándonos en el contexto al que pertenecía un
usuario en nuestro LDAP. Con un poco de scripting bash en Mayo de 2009
implementamos lo que serían unos repositorios dinámicos que se
configuraban en el cliente en función del contexto.

Esto fue ,sin duda, una gran idea pero la gestión de estos repositorios
dinámicos era manual y muy propensa a errores.

La gestión de estos repositorios dinámicos recayó en mí, por lo que
decidí simplificarla inmediatamente y crear el primer prototipo de
migasfree. Dos semanas de programación, en horas no laborales,
fueron suficientes para presentar a mis compañeros de trabajo un
prototipo, que fue puesto en producción en Junio de 2009.

   .. note::
      Una de las ventajas de trabajar con software libre es
      la facilidad con la que puedes crear proyectos ya que puedes
      mezclar, como si de piezas de puzzle fueran, diferentes componentes
      sin preocuparte en exceso del tema de las licencias. Un ejemplo
      de esto ha sido la incorporación de la funcionalidad de captura del
      hardware en los equipos. Utilicé el comando lshw__ y unas
      pocas líneas de código para adaptarlo a la base de datos de migasfree.

__ http://ezix.org/project/wiki/HardwareLiSter

Versiones
=========

El primer prototipo solo trabajaba con paquetería rpm y gestor de
paquetes yum, y el código bash que se ejecutaba en el cliente se
generaba en el servidor.

Despues de usar migasfree un tiempo en producción vimos que podría ser
un buen sistema para otras organizaciones, y mis compañeros me dieron el
impulso necesario para publicar el codígo, y así durante el verano de
2009, reorganice los menús, limpié un poco el código, e
hice que migasfree pudiera trabajar con distintas versiones de SO y de
sistemas de paquetería. Fue publicado__ en github__ en abril de 2010 y
bautizado como "migasfree with fried eggs", porque mis compañeros decían
que el logotipo se parecía a un huevo frito, ¡Qué sabrán ellos de Arte!.

__ https://github.com/migasfree/migasfree

__ https://github.com/

En Noviembre de 2011, Jose Antonio Chavarría desarrollador de AZLinux
reescribe y publica el `cliente migasfree`__. Realizó tambien grandes
cambios en la estructura del servidor. Tuvimos que definir la API con
la que el cliente y el servidor debían comunicarse. Usamos claves
asimétricas para dotar de seguridad al sistema. Esta nueva versión fue
denominada "migasfree no trans" supongo que por incorporar un código más
"limpio", por decirlo de alguna manera.

__ https://github.com/migasfree/migasfree-client

Poco a poco fuímos dotando al sistema de nuevas funcionalidades, y para
principios de 2013 Jose Antonio Chavarría cambió la navegación y aspecto
del servidor. Esta nueva versión fue denominada "migasfree with
chocolate".

En febrero de 2014 liberamos la versión 4 del servidor (migasfree grape). Esta
versión hace uso de bootstrap__ con el fin de dotar a la aplicación de un diseño
web adaptable a distintos dispositivos. Además incorpora distintas mejoras
de todo tipo y utiliza la última versión estable de Django, la 1.6.2. Actualmente
esta es la versíón que utilizamos en AZLinux.

__ http://getbootstrap.com/

Características
===============

* Migasfree es simple, y hacemos esfuerzos por mantenerlo así. Tendemos a
  lo que denominamos gestión cero, es decir, procuramos que la gestión de
  añadir nuevas entradas en migasfree no requiera ninguna tarea
  administrativa.

* Está basado en la arquitectura cliente / servidor.

* Es Seguro. Las comunicaciones entre cliente y servidor están firmadas con
  claves asimétricas.

* Es adaptable. Puedes programar las propiedades para adaptarlas a tus
  necesidades.

* Es Software Libre licenciado bajo la GNU Public License.

* Captura de datos. Almacena tanto el inventario software y hardware de
  los equipos, permitiendo hacer consultas sobre ellos. Almacena también
  información de los equipos tales como sus atributos, actualizaciones,
  migraciones que se han realizado, etc.

* Consultas. Puedes programar consultas contra la base de datos de
  migasfree.

* Gestión de errores. Los errores que se producen en los equipos son
  enviados al servidor y almacenados permitiendo hacer su seguimiento.

* Gestión de fallas. Puedes programar código que será ejecutado en los
  clientes con el fin de obtener información de los equipos.

* Alertas. Permite conocer en tiempo real el estado del sistema facilitando
  al administrador su trabajo.

* Estadísticas.

Principales componentes empleados
=================================

* Django__ un framework de desarrollo web.

__ https://www.djangoproject.com/

* Servidor web Apache__. Puedes emplear otro si quieres.

__ http://www.apache.org/

* Lenguaje de programación Python__.

__ http://www.python.org/

* Base de datos Posgresql__. Puedes usar otras.

__ http://www.postgresql.org/

* Intérprete de comandos Bash__.

__ http://www.gnu.org/software/bash/manual/bashref.html

* Sistemas de paquetería como APT__ ó RPM__.

__ https://launchpad.net/apt-project

__ http://www.rpm.org/

* Información Hardware: Lshw__.

__ http://ezix.org/project/wiki/HardwareLiSter

* Bootstrap__ un framework para desarrollo web.

__ http://getbootstrap.com/

* Flot__ una librería gráfica.

__ http://www.flotcharts.org/
