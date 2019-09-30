# genomedashboard/settings.py

"""
Django settings for genomedashboard project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import logging
from genomedashboard import secrets

def gettext(s): return s

# Build paths relative to the project root like this: os.path.join(DATA_DIR, ...)
# DATA_DIR = os.path.dirname(os.path.dirname(__file__))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets._SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = secrets._DEBUG

ALLOWED_HOSTS = secrets._ALLOWED_HOSTS

# Application definition
ROOT_URLCONF = 'genomedashboard.urls'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'genomedashboard', 'static'),
    os.path.join(BASE_DIR, 'polls', 'static'),
    os.path.join(BASE_DIR, 'dashboard', 'static'),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'genomedashboard', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                # 'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                # 'cms.context_processors.cms_settings'
            ],
            # WARNING: You cannot use 'loaders' and 'APP_DIRS' at the same time!!!
            # 'loaders': [
            #     'django.template.loaders.filesystem.Loader',
            #     'django.template.loaders.app_directories.Loader',
            #     'django.template.loaders.eggs.Loader'
            # ],
        },
    },
]

MIDDLEWARE = [
    # 'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'cms.middleware.user.CurrentUserMiddleware',
    # 'cms.middleware.page.CurrentPageMiddleware',
    # 'cms.middleware.toolbar.ToolbarMiddleware',
    # 'cms.middleware.language.LanguageCookieMiddleware'
]

INSTALLED_APPS = [
    # Django.
    # 'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',

    # CMS (optional).
    # 'cms',
    # 'menus',
    # 'sekizai',
    # 'treebeard',  # Replaces mptt.
    # 'djangocms_text_ckeditor',
    # 'filer',
    # 'easy_thumbnails',
    # 'djangocms_audio',   # Doesn't work right.
    # 'djangocms_column',
    # 'djangocms_file',
    # 'djangocms_link',
    # 'djangocms_picture',
    # 'djangocms_style',
    # 'djangocms_snippet',
    # 'djangocms_googlemap',
    # 'djangocms_video',
    # 'djangocms_icon',
    # 'djangocms_bootstrap4',
    # 'djangocms_bootstrap4.contrib.bootstrap4_alerts',
    # 'djangocms_bootstrap4.contrib.bootstrap4_badge',
    # 'djangocms_bootstrap4.contrib.bootstrap4_card',
    # 'djangocms_bootstrap4.contrib.bootstrap4_carousel',
    # 'djangocms_bootstrap4.contrib.bootstrap4_collapse',
    # 'djangocms_bootstrap4.contrib.bootstrap4_content',
    # 'djangocms_bootstrap4.contrib.bootstrap4_grid',
    # 'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
    # 'djangocms_bootstrap4.contrib.bootstrap4_link',
    # 'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
    # 'djangocms_bootstrap4.contrib.bootstrap4_media',
    # 'djangocms_bootstrap4.contrib.bootstrap4_picture',
    # 'djangocms_bootstrap4.contrib.bootstrap4_tabs',
    # 'djangocms_bootstrap4.contrib.bootstrap4_utilities',

    # Custom apps.
    'genomedashboard.apps.GenomedashboardConfig',
    'polls.apps.PollsConfig',
    'dashboard.apps.DashboardConfig'
]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': secrets._DJANGO_DB_ENGINE,
        'NAME': secrets._DJANGO_DB_NAME,
        'USER': secrets._DJANGO_DB_USER,
        'PASSWORD': secrets._DJANGO_DB_PASSWORD,
        'HOST': secrets._DJANGO_DB_HOST,
        'PORT': secrets._DJANGO_DB_PORT
    }
}

MIGRATION_MODULES = {

}

# SSL Setup.
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = (
    # Customize this if needed.
    ('en', gettext('en')),
)

WSGI_APPLICATION = 'genomedashboard.wsgi.application'
GATEWAY_NAMESPACE = secrets._GATEWAY_NAMESPACE

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

# Logging./
logger = logging.getLogger(__file__)

# DjangoCMS configuration.
# Commented out because CMS is not installed.
"""
SITE_ID = secrets._SITE_ID

CMS_LANGUAGES = {
    # Customize this
    1: [
        {
            'code': 'en',
            'name': gettext('en'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

CMS_TEMPLATES = secrets._CMS_TEMPLATES
CMS_PERMISSION = True
CMS_PLACEHOLDER_CONF = {}

THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

DJANGOCMS_PICTURE_NESTING = True
DJANGOCMS_PICTURE_RESPONSIVE_IMAGES = True
DJANGOCMS_PICTURE_RATIO = 1.618
# Custom picture templates - if required.
# DJANGOCMS_PICTURE_TEMPLATES = [
#     ('background', _('Background image')), # Need to design these first!
# ]

DJANGOCMS_AUDIO_ALLOWED_EXTENSIONS = ['mp3', 'ogg', 'wav']
# Custom audio templates - if required.
# DJANGOCMS_AUDIO_TEMPLATES = [
#     ('feature', _('Featured Version')),
# ]

"""

# Google Analytics.
GOOGLE_ANALYTICS_PROPERTY_ID = secrets._GOOGLE_ANALYTICS_PROPERTY_ID
GOOGLE_ANALYTICS_PRELOAD = secrets._GOOGLE_ANALYTICS_PRELOAD

# Exported settings.
SETTINGS_EXPORT = [
    'GOOGLE_ANALYTICS_PROPERTY_ID',
    'GOOGLE_ANALYTICS_PRELOAD'
]
