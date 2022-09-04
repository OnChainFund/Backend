web: python manage.py collectstatic && python manage.py makemigrations && python manage.py migrate && gunicorn core.wsgi
worker: python manage.py qcluster --settings=core.settings