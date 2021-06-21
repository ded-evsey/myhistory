#!/bin/bash

python /srv/project/manage.py migrate --noinput &
python /srv/project/manage.py collectstatic --noinput &
yes| python /srv/project/manage.py compilemessages &
gunicorn  --bind=0.0.0.0:8000 --workers=4 --max-requests 30 --reload --log-level debug --env DJANGO_SETTING_MODULE=core.settings.py core.wsgi