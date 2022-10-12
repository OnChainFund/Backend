web: python src/manage.py makemigrations && python src/manage.py migrate && python src/manage.py runserver 
worker: python src/manage.py qcluster --settings=core.settings
event_listener: python src/manage.py moniter_events qcluster --settings=core.settings