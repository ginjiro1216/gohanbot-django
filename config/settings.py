import os.path
from distutils.util import strtobool
from pathlib import Path

import environ
from django.contrib import messages

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env(f"{BASE_DIR}/env/.env")

SECRET_KEY = env("SECRET_KEY")

DEBUG = strtobool(env("DEBUG"))

ALLOWED_HOSTS = ["*"]
if not DEBUG:
    ALLOWED_HOSTS = [""]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.gohanbot.apps.GohanbotConfig",
    "apps.accounts.apps.AccountsConfig",
    "django_extensions",
    "debug_toolbar",
    "django_bootstrap5",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth."
        "password_validation.UserAttributeSimilarityValidator"
    },
    {
        "NAME": "django.contrib.auth."
        "password_validation.MinimumLengthValidator"
    },
    {
        "NAME": "django.contrib.auth."
        "password_validation.CommonPasswordValidator"
    },
    {
        "NAME": "django.contrib.auth."
        "password_validation.NumericPasswordValidator"
    },
]

LOGIN_URL = "accounts/login"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


LANGUAGE_CODE = "ja"

TIME_ZONE = "Asia/Tokyo"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
if DEBUG:
    STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, "www", "static")


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MESSAGE_TAGS = {
    messages.INFO: "alert alert-info",
    messages.SUCCESS: "alert alert-success",
    messages.ERROR: "alert alert-danger",
    messages.WARNING: "alert alert-warning",
}
