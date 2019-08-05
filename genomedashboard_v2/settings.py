"""
Django settings for genomedashboard_v2 project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

# Imports and module dependencies.
import os
import logging


# Secrets file.
from genomedashboard_v2 import secrets


# Helper methods.
gettext = lambda s: s


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bv6*hn@0g$qg-2=vjc@rfu$g7vnwz#+o&fpjevnh_ky3@bs=of'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # Custom apps.
    'polls.apps.PollsConfig',
    # Django.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ROOT_URLCONF = 'genomedashboard_v2.urls'
WSGI_APPLICATION = 'genomedashboard_v2.wsgi.application'
GATEWAY_NAMESPACE = secrets._GATEWAY_NAMESPACE


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        # sqlite3
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

        # Postgres
        'ENGINE': secrets._DJANGO_DB_ENGINE,
        'NAME': secrets._DJANGO_DB_NAME,
        'USER': secrets._DJANGO_DB_USER,
        'PASSWORD': secrets._DJANGO_DB_PASSWORD,
        'HOST': secrets._DJANGO_DB_HOST,
        'PORT': secrets._DJANGO_DB_PORT
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# STATIC_ROOT is the location you wasnt to serve your files from AFTER you run python manage.py collectstatic.

# Development paths.
# STATIC_ROOT = os.path.join(BASE_DIR, '../static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Production paths.
# STATIC_ROOT = "/var/www/example.com/static/"

STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'static'),
    # Add specific app static resources here.
    # Remember to run: python manage.py collectstatic.
    os.path.join(BASE_DIR, 'genomedashboard_v2/static'),
    os.path.join(BASE_DIR, 'polls/static'),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


# Media files.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../media')


# Internationalization.
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = 'en'   # 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


LANGUAGES = (
    ('en', gettext('en')),
)


# Logging./
logger = logging.getLogger(__file__)


# Google Analytics.
GOOGLE_ANALYTICS_PROPERTY_ID = secrets._GOOGLE_ANALYTICS_PROPERTY_ID
GOOGLE_ANALYTICS_PRELOAD = secrets._GOOGLE_ANALYTICS_PRELOAD


# Exported settings.
SETTINGS_EXPORT = [
    'GOOGLE_ANALYTICS_PROPERTY_ID',
    'GOOGLE_ANALYTICS_PRELOAD'
]
