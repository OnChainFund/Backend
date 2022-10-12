web: python src/manage.py makemigrations && python manage.py migrate && python manage.py collectstatic && gunicorn core.wsgi
worker: python src/manage.py qcluster --settings=core.settings
event_listener: python src/manage.py moniter_events qcluster --settings=core.settings