import os
from pathlib import Path
from decouple import config
import django
from django.utils.encoding import force_str
import dj_database_url

django.utils.encoding.force_text = force_str
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")

DEBUG = True
ALLOWED_HOSTS = [config("BACKEND_DOAMIN")]
CSRF_TRUSTED_ORIGINS = [config("FRONTEND_DOMAIN")]
CORS_ALLOWED_ORIGINS = [config("FRONTEND_DOMAIN")]

INSTALLED_APPS = [
    "admin_interface",
    "colorfield",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "import_export",  # import export admin
    "strawberry.django",
    "strawberry_django_jwt.refresh_token",
    "django_jsonform",
    "django_q",
    "solo",
    "django_ethereum_events",
    "management",
    "fund",
    "abi",
    "utils",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
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
    "default": dj_database_url.config(
        default=config("DATABASE_URL"), conn_max_age=1800
    ),
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

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# admin interface
X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

STATIC_URL = "static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
DISABLE_COLLECTSTATIC = 0

Q_CLUSTER = {
    "name": "ocf_backend",
    "workers": 8,
    "recycle": 0,
    "timeout": 60,
    "compress": True,
    "save_limit": 250,
    "queue_limit": 500,
    "cpu_affinity": 1,
    "label": "Django Q",
    "orm": "default",
}

STRAWBERRY_DJANGO = {
    "FIELD_DESCRIPTION_FROM_HELP_TEXT": True,
    "TYPE_DESCRIPTION_FROM_MODEL_DOCSTRING": True,
}


# Django Sign-In with Ethereum Auth Settings
# AUTH_USER_MODEL = "user.Wallet"
AUTHENTICATION_BACKENDS = [
    "strawberry_django_jwt.backends.JSONWebTokenBackend",
    "django.contrib.auth.backends.ModelBackend",
    #    "user.backend.SiweBackend",
]
LOGIN_URL = "/"
SESSION_COOKIE_AGE = 3 * 60 * 60
CREATE_GROUPS_ON_AUTHN = False  # defaults to False
CREATE_ENS_PROFILE_ON_AUTHN = True  # defaults to True


# django_ethereum_events
ETHEREUM_NODE_URI = "https://api.avax-test.network/ext/bc/C/rpc"
ETHEREUM_LOGS_FILTER_AVAILABLE = True
ETHEREUM_GETH_POA = True
