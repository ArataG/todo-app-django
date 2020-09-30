#!/bin/bash

python3 -m venv myvenv
echo "setup virtual enviroment"

source ./myvenv/bin/activate
echo "activate venv"

python -m pip install --upgrade pip
echo "update pip"

pip install -r requirements.txt
echo "install django"

django-admin startproject config .
echo "django start project"
echo "setup config directory"











