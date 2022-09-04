web: python manage.py migrate && gunicorn core.wsgi
worker: python manage.py qcluster --settings=core.settings