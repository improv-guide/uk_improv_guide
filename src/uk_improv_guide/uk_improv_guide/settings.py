"""
Django settings for uk_improv_guide project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import logging
import os
from typing import Mapping, Union

import pkg_resources

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# import rollbar

log = logging.getLogger(__name__)

FILE_CHARSET: str = "utf-8"

SITE_NAME: str = "Improv Gude"
SITE_CANONICAL_URL = "http://improv.guide"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY: str = os.environ.get("PRODUCTION_SECRET") or "secret_key!"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG: bool = True if os.environ.get("DEBUG", None) else False

if DEBUG:
    log.info("Running in DEBUG mode!")
else:
    log.info("Running in PRODUCTION mode!")

COUNTRIES_FIRST = ["GB"]

ALLOWED_HOSTS = ["improv.guide", "impro.guide", "localhost", "improvguide.uk"]


# Application definition

INSTALLED_APPS = [
    "imagekit",
    "reversion",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "social_django",
    "sass_processor",
    "uk_improv_guide",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "rollbar.contrib.django.middleware.RollbarNotifierMiddleware",
]

ROOT_URLCONF = "uk_improv_guide.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.jinja2.Jinja2",
        "DIRS": [pkg_resources.resource_filename("uk_improv_guide.html", "jinja2")],
        "APP_DIRS": True,
    },
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [pkg_resources.resource_filename("uk_improv_guide.html", "django")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
            ],
            "libraries": {
                "improv_guide_extras": "uk_improv_guide.templatetags.improv_guide_extras"
            },
            # "loaders": [
            #     "django.template.loaders.filesystem.Loader",
            #     "django.template.loaders.app_directories.Loader",
            #     "apptemplates.Loader",
            # ],
        },
    },
]

WSGI_APPLICATION = "uk_improv_guide.wsgi.application"


def get_database_settings() -> Mapping[str, Union[str, Mapping[str, str]]]:
    result = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ["POSTGRES_DB"],
            "USER": os.environ["POSTGRES_USER"],
            "PASSWORD": os.environ["POSTGRES_PASSWORD"],
            "HOST": os.environ["POSTGRES_HOST"],
            "PORT": os.environ["POSTGRES_PORT"],
            "OPTIONS": {"sslmode": "allow"},
        }
    }
    return result


DATABASES = get_database_settings()


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"

AUTHENTICATION_BACKENDS = [
    "social_core.backends.linkedin.LinkedinOAuth2",
    "social_core.backends.instagram.InstagramOAuth2",
    "social_core.backends.facebook.FacebookOAuth2",
    "django.contrib.auth.backends.ModelBackend",
]

_static_dir = os.path.join(BASE_DIR, "_static")

STATICFILES_DIRS = (_static_dir,)

STATIC_ROOT = "/static/"

MEDIA_ROOT = "/media/"

MEDIA_URL = "/media/"

SOCIAL_AUTH_FACEBOOK_SCOPE = ["email"]
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    "locale": "uk_GB",
    "fields": "id, name, email, age_range",
}

SITE_ID = 1

SLACK_WEB_HOOK = os.environ["SLACK_WEB_HOOK"]

SASS_PROCESSOR_ROOT = _static_dir

SASS_PROCESSOR_ENABLED: bool = True

USE_TZ = True

ENIRONMENT_NAME: str = os.environ.get(
    "ENVIRONMENT_NAME", "development" if DEBUG else "production"
)

# ROLLBAR = {
#     "access_token": "9227e96158a8446c8a6eed836a6aa681",
#     "environment": ENIRONMENT_NAME,
#     "root": BASE_DIR,
# }
# rollbar.init(**ROLLBAR)


sentry_sdk.init(
    dsn="https://74a9130b6e564cce944b3fdf39c11b9d@sentry.io/1531137",
    integrations=[DjangoIntegration()],
    environment=ENIRONMENT_NAME,
    release=pkg_resources.get_distribution("uk_improv_guide").version,
)

SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get("FACEBOOK_APP_KEY")
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get("FACEBOOK_SECRET")
OCIAL_AUTH_FACEBOOK_SCOPE = ["email", "user_link"]

if not all([SOCIAL_AUTH_FACEBOOK_KEY, SOCIAL_AUTH_FACEBOOK_SECRET]):
    log.warning("Facebook keys are not set!")

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "home"
LOGOUT_URL = "logout"
LOGOUT_REDIRECT_URL = "login"
