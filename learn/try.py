from decouple import config

SECRET_KEY = config('PRIVATE_KEY')
print(SECRET_KEY)