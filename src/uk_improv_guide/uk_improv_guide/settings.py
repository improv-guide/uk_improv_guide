"""
Django settings for uk_improv_guide project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

import pkg_resources

SITE_NAME: str = "European Improv Gude"
SITE_CANONICAL_URL = "http://improv.guide"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "1n*$a4#0$5g&*esz0zlnfjty30tk$wp1)$6+y#z1b8o0vv(4xv"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

COUNTRIES_FIRST = ["GB"]

ALLOWED_HOSTS = ["improv.guide", "impro.guide", "localhost"]


# Application definition

INSTALLED_APPS = [
    # 'captcha',
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
            ]
        },
    },
]

WSGI_APPLICATION = "uk_improv_guide.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": os.environ["POSTGRES_HOST"],
        "PORT": os.environ["POSTGRES_PORT"],
    }
}

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

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/uk_improv_guide.static/"

AUTHENTICATION_BACKENDS = [
    "social_core.backends.linkedin.LinkedinOAuth2",
    "social_core.backends.instagram.InstagramOAuth2",
    "social_core.backends.facebook.FacebookOAuth2",
    "django.contrib.auth.backends.ModelBackend",
]

# STATIC_ROOT = os.path.join(BASE_DIR, '')
#

MEDIA_URL = "media/"
#
# print(f"Media Root: {MEDIA_ROOT}")

_static_dir = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = (_static_dir,)

MEDIA_ROOT = os.path.join(_static_dir, "media")

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'locale': 'uk_GB',
    'fields': 'id, name, email, age_range'
}

SITE_ID=1