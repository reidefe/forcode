#!/bin/sh
python manage.py makemigrations forcode
python manage.py migrate forcode
exec "$@"