#!/bin/bash

python /srv/project/manage.py migrate --noinput &
python /srv/project/manage.py collectstatic --noinput &
yes| python /srv/project/manage.py compilemessages &
gunicorn  --bind=0.0.0.0:8000 --workers=4 --error-logfile -  --log-level debug --reload --env DJANGO_SETTING_MODULE=core.settings.py core.wsgi