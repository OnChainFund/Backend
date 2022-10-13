web: python manage.py makemigrations && python manage.py migrate && python manage.py runserver 
worker: python manage.py qcluster --settings=core.settings
event_listener: python manage.py moniter_events qcluster --settings=core.settings