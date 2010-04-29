# -*- coding: utf-8 -*-
# Django settings for cms project.
import os
PROJECT_DIR = os.path.dirname(__file__)
PROJECT_NAME = 'vsad'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ("pokutnik@gmail.com",)
REPORT_EMAILS = ("pokutnik@gmail.com",)
EMAIL_HOST = "localhost"
#EMAIL_PORT = 1025
MANAGERS = ADMINS


CACHE_BACKEND = 'locmem:///'




DATABASE_ENGINE = 'sqlite3'     #postgresql_psycopg2'       # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'vsad.db'           # Or path to database file if using sqlite3.
DATABASE_USER = ''           # Not used with sqlite3.
DATABASE_PASSWORD = ''       # Not used with sqlite3.
DATABASE_HOST = ''     # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''              # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be avilable on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Ukraine/Kyiv'
DATE_FORMAT = "d.m.Y"
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media/')
#ADMIN_MEDIA_ROOT = os.path.join(PROJECT_DIR, '../admin_media/')
MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/admin/'


# Make this unique, and don't share it with anybody.
SECRET_KEY = '*xq7m@)*sdf213f2awo3#33s5;j!spa0(jibsrz9%c0d=e(g)v*!17y(vx0ue_3'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.debug",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
)



CUSTOM_USER_MODEL = 'vip.VipUser'

INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'pages.middleware.PageFallbackMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',

    #'django.contrib.csrf.middleware.CsrfMiddleware',
    #'cms.middleware.user.CurrentUserMiddleware',
    #'cms.middleware.page.CurrentPageMiddleware',
    #'cms.middleware.multilingual.MultilingualURLMiddleware',
    #'cms.middleware.toolbar.ToolbarMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates'),
)

#EMAIL_HOST = 'localhost'
#EMAIL_PORT = 1025
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''
#EMAIL_USE_TLS = False
#EFAULT_FROM_EMAIL = 'admin@vishneviy-sad.org.ua'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    #'django.contrib.admindocs',
    'django.contrib.sites',
    
    'django_extensions',
    #'debug_toolbar',
    'south',
    'sorl.thumbnail',
    'markitup',
	
    PROJECT_NAME +'.menu',
    PROJECT_NAME +'.pizza',
    PROJECT_NAME +'.guestbook',
    PROJECT_NAME +'.zayavka',
    PROJECT_NAME +'.pages',
)


gettext = lambda s: s

LANGUAGE_CODE = "uk-UA.utf-8"

LANGUAGES = (
    ('uk', gettext('Ukrainian')),
)

MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': True})
MARKITUP_PREVIEW_FILTER = ('markdown.markdown', {'safe_mode': True})
MARKITUP_SET = 'markitup/sets/markdown'
MARKITUP_SKIN = 'markitup/skins/markitup'


APPEND_SLASH = True

try:
    from local_settings import *
except ImportError:
    pass


