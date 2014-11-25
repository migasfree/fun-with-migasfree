#/bin/bash

_USER=$1

cd ..
make latexpdf html
cd bin

ftp -inv migasfree.org<<FINFTP
       user $_USER
       binary
       lcd ../_build/latex
       cd /httpdocs/repo/book/pdf
       put fun-with-migasfree.pdf
       lcd ../html
       cd /httpdocs/repo/book/html
       mput *.html
       mput *.js
       mput _images/*
       mput _static/*
       mput _sources/*.txt
       bye
FINFTP
