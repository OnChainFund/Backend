import os
from pathlib import Path
import django
from django.utils.encoding import force_str

django.utils.encoding.force_text = force_str
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-==7(e(+-+px9hen^u!&+@2-q$@x^==6a7t06aa##_lplhsukwq"

DEBUG = True
# ALLOWED_HOSTS = ["time-ledger.herokuapp.com"]
# CSRF_TRUSTED_ORIGINS = ["https://time-ledger.herokuapp.com"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "import_export",  # import export admin
    "django_q",
    "graphene_django",
    "contract",
    "fund",
    "management",
    "schedual",
    "try",
    "utils",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "zh-Hant"
TIME_ZONE = "Asia/Taipei"
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGES = (("en", "English"), ("zh-Hant", "Traditional chinese"))


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# django-mdeditor
X_FRAME_OPTIONS = "SAMEORIGIN"
MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")
MEDIA_URL = "/media/"
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, "static")

Q_CLUSTER = {
    "name": "ocf_backend",
    "workers": 8,
    "recycle": 500,
    "timeout": 60,
    "compress": True,
    "save_limit": 250,
    "queue_limit": 500,
    "cpu_affinity": 1,
    "label": "Django Q",
    "orm": "default",
}
