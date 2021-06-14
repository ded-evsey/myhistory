#!/bin/bash
export FLASK_APP=app.py
export FLASK_ENV=development
gunicorn --workers=2 --bind=0.0.0.0:5000 --reload app:app
