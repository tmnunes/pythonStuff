# tnunesrepopy
Instalação / Start in Python:

Instalar Python 2.7.12 da net
Instalar Xcode e Command Line tools
Instalar Brew : /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
Instalar PIP: sudo easy_install pip
Instalar Sublime da net. O outdo editor de texto
Instalar virtualenv: pip install virtualenv
Instalar GIT: brew install git
Instalar Django : pip install django
Instalar Django Framework: pip install djangorestframework
Instalar Swagger: pip install Django-rest-swagger (pip install django-rest-swagger===0.3.5 , versão 1.9 do Django)


Criar ficheiro em branco da linha de comandos
touch xxxxx.py
Open do ficheiro
open xxxxx.py

Criar virtualenv: virtualenv env
entra: source env/bin/activate
instalar django e framework la dentro

sair virtualenv: deactivate

create new project: django-admin.py startproject tutorial
create a quickstart: cd tutorial
django-admin.py startapp quickstart



example to start: 
$ mkdir drf-demo; cd drf-demo 
$ virtualenv .env 
$ pip install "Django >= 1.9, < 1.10" 
$ django-admin startproject project --template=https://github.com/ambivalentno/django-skeleton/archive/master.zip 
$ mkdir log $ mkdir project/db
$ python project/manage.py runserver
http://localhost:8000/



sites:
https://tests4geeks.com/django-rest-framework-tutorial/
http://www.django-rest-framework.org/tutorial/quickstart/
https://realpython.com/blog/python/django-rest-framework-quick-start/
http://pythonclub.com.br/django-rest-framework-quickstart.html


