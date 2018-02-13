===
FAQ
===

 .. epigraph::

   Uno reconoce a las personas inteligentes por sus respuestas. A los sabios
   se los reconoce por sus preguntas.

   -- Naguib Mahfuz


Sobre el servidor migasfree
===========================

Cuando accedo al servidor web me aparece: ``Server error (500)``
----------------------------------------------------------------

Causa
*****

Este error puede estar motivado por múltiples causas. La más probable
es que la contraseña del usuario ``migasfree`` en ``Posgresql`` no sea la
misma que la que está configurada en el servidor.

Solución
********

Comprueba la contraseña que tienes en ``/var/lib/migasfree/FQDN/conf/settings.py``
es la misma que la del usuario ``migasfree`` en Postgresql. Si no existe
este fichero, la contraseña por defecto es ``migasfree``.

Si necesitas cambiarla, haz esto:

  .. code-block:: none

    # su postgres
    # psql
    # ALTER USER migasfree WITH PASSWORD 'mipassword';


¿Cómo hago una fórmula para obtener el contexto LDAP de un usuario?
---------------------------------------------------------------------

Necesitas que los clientes tengan instalado el paquete ``python-ldap``.
En el servidor tendrás que crear una nueva fórmula:

  Prefijo: ``CTX``

  Nombre: ``CONTEXTO LDAP``

  Lenguaje: ``python``

  Clase: ``Añadir por la derecha``

  Código:

  .. code-block:: none

    import sys
    import ldap
    import migasfree_client.utils

    LDAP_SERVER = 'ldap.miservidor.es'
    LDAP_BASE = ''
    LDAP_SCOPE = ldap.SCOPE_SUBTREE

    def get_ldap_property(filter_str, property_str, base = LDAP_BASE, scope = LDAP_SCOPE):
        global global_ldap_object

        try:
            _result = global_ldap_object.search_s(base, scope, filter_str, [property_str])
        except ldap.LDAPError, e:
            print e
            sys.exit(errno.ENOMSG) # no result

        if _result == None or not _result:
            print 'No result in LDAP search'
            sys.exit(errno.ENOMSG) # no result

        if property_str == 'dn': # special case: dn is getted in other field
            return _result[0][0]

        try:
            _ret = _result[0][1][property_str]
            if len(_ret) == 1: # only one result?
                return _ret[0]
        except KeyError:
            return '' # empty value

        return _ret

    def get_dn(user):
        # cn=oXXXXx,ou=XXXX,o=XXXXXX
        return get_ldap_property('(cn=%s)' % user, 'dn')

    def get_context(user):
        result = get_dn(user).split(',')

        ret = ''
        for item in result[:]:
            tmp = item.split('=')
            if tmp[0] == 'ou' or tmp[0] == 'o':
                ret = '%s%s.' % (ret, tmp[1])

        return ret[:-1] # remove trailing '.'

    def run():
        global global_ldap_object
        global_ldap_object = ldap.initialize('ldap://%s:389' % LDAP_SERVER)

        user=migasfree_client.utils.get_current_user().split("~")[0]
        print get_context(user)

    if __name__ == '__main__':
        run()


¿Cómo hago una fórmula para obtener los grupos LDAP de un usuario?
--------------------------------------------------------------------

Necesitas que los clientes tengan instalado el paquete python-ldap.
En el servidor tendrás que crear una nueva fórmula:

  Prefijo: ``GRP``

  Nombre: ``GRUPOS LDAP``

  Lenguaje: ``python``

  Clase: ``Lista``

  Código:

  .. code-block:: none

    import sys
    import ldap
    import migasfree_client.utils
    LDAP_SERVER = 'ldap.miservidor.es'
    LDAP_BASE = ''
    LDAP_SCOPE = ldap.SCOPE_SUBTREE

    def get_ldap_property(filter_str, property_str, base = LDAP_BASE, scope = LDAP_SCOPE):
        global global_ldap_object

        try:
            _result = global_ldap_object.search_s(base, scope, filter_str, [property_str])
        except ldap.LDAPError, e:
            print e
            sys.exit(errno.ENOMSG) # no result

        if _result == None or not _result:
            print 'No result in LDAP search'
            sys.exit(errno.ENOMSG) # no result

        if property_str == 'dn': # special case: dn is getted in other field
            return _result[0][0]

        try:
            _ret = _result[0][1][property_str]
            if len(_ret) == 1: # only one result?
                return _ret[0]
        except KeyError:
            return '' # empty value

        return _ret

    def get_groups(user):
        # TODO only groups of organization or all of them?
        _result = get_ldap_property('(cn=%s)' % user, 'groupMembership')
        if not _result:
            return '' # no groups found

        # only one result?
        if type(_result) is str:
            _result = [_result]

        _ret = ''
        for _item in _result:
            _t = _item.split(',')
            if '=' in _t[0]:
                _ret = '%s%s, ' % (_ret, _t[0].split('=')[1])

        return _ret[:-2] # remove trailing ',

    def run():
        global global_ldap_object
        global_ldap_object = ldap.initialize('ldap://%s:389' % LDAP_SERVER)

        user=migasfree_client.utils.get_current_user().split("~")[0]
        print get_groups(user),

    if __name__ == '__main__':
        run()

Sobre el cliente migasfree
==========================

El cliente migasfree devuelve el mensaje: "firma no válida"
-----------------------------------------------------------

Causa
*****

Las claves almacenadas en el cliente no coinciden con el proyecto indicado
en ``/etc/migasfree.conf``.

Solución
********

Borra las claves del equipo cliente.

Para la versión de migasfree-client 4.6 ó inferior usa:

  .. code-block:: none

    # rm /root/.migasfree-keys/*

Para la versión de migasfree-client 4.7 ó superior usa:

  .. code-block:: none

    # rm -rf /var/migasfree-client/keys/[server]/*

  .. note::

     Si es necesario, vuelve a registrar el cliente ejecutando: ``migasfree --register``.


Imposible obtener /PKGS/binary-amd64/Packages  404  Not Found
-------------------------------------------------------------

Causa
*****

Por defecto los repositorios físicos en el servidor se generan para la
arquitectura i386.

Solución
********

Accede a ``Configuracion - Sistemas de gestión de paquetes - apt-get`` y modifica el campo
``crear repositorio`` de esta manera:

  .. code-block:: none

    cd %PATH%
    mkdir -p %REPONAME%/PKGS/binary-i386/
    mkdir -p %REPONAME%/PKGS/binary-amd64/
    mkdir -p %REPONAME%/PKGS/sources/
    cd ..
    dpkg-scanpackages -m dists/%REPONAME%/PKGS /dev/null | gzip -9c > dists/%REPONAME%/PKGS/binary-i386/Packages.gz
    dpkg-scanpackages -m dists/%REPONAME%/PKGS /dev/null | gzip -9c > dists/%REPONAME%/PKGS/binary-amd64/Packages.gz
    dpkg-scansources dists/%REPONAME%/PKGS /dev/null | gzip -9c > dists/%REPONAME%/PKGS/sources/Sources.gz


No se consige ejecutar el cliente de migasfree en un ``cron``.
--------------------------------------------------------------

Causa
*****

Las variables de entorno no están disponibles.

Solución
********

En vez de programar el cron así:

  .. code-block:: none

    00 07 * * * root /usr/bin/migasfree --update

debemos forzar el **entorno de usuario** de esta forma:

  .. code-block:: none

    00 07 * * * root su -c 'migasfree --update' --login
