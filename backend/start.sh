#! /usr/bin/env sh
python manage.py migrate
set -e
exec gunicorn -k egg:meinheld#gunicorn_worker -c "$GUNICORN_CONF" "$APP_MODULE"
