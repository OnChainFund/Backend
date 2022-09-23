import dj_database_url
from .settings import *

DEBUG = True

ALLOWED_HOSTS = ["*", "127.0.0.1"]
ALLOWED_ALL_HOST = True

DATABASES = {
    "default": dj_database_url.config(
        default=config("DEV_DATABASE_URL"), conn_max_age=1800
    ),
}

INSTALLED_APPS.append("test_app")

CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:3000",
    "http://127.0.0.1:9000",
]
