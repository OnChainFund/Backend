web: python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic && gunicorn core.wsgi
worker: python manage.py qcluster --settings=core.settings