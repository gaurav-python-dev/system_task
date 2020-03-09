from .base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

INSTALLED_APPS += ['debug_toolbar',]
MIDDLEWARE_CLASSES +=['debug_toolbar.middleware.DebugToolbarMiddleware',]

#debug toolbar settings
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]
def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECT':False,
    'DISABLE_PANELS': ('debug_toolbar.panels.profiling.ProfilingPanel',),
    'SHOW_TOOLBAR_CALLBACK':show_toolbar
}

INTERNAL_IPS = ('127.0.0.1',)

DATABASES = {
    'default': {
        'NAME': 'account_detail',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER':'postgres',
        'PASSWORD':'root',
        'HOST': 'localhost',
        'PORT':'5432'
    },
    'database1': {
        'NAME': 'database1',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER':'postgres',
        'PASSWORD':'root',
        'HOST': 'localhost',
        'PORT':'5432'
    },
    'database2': {
        'NAME': 'database2',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER':'postgres',
        'PASSWORD':'root',
        'HOST': 'localhost',
        'PORT':'5432'
    },
    'database3':{
        'NAME': 'database3',
        'ENGINE': 'django.db.backends.mysql',
        'USER':'root',
        'PASSWORD':'root',
        'HOST': 'localhost',
        'PORT':'3306'
    },
    'database4':{
        'NAME': 'database4',
        'ENGINE': 'django.db.backends.mysql',
        'USER':'root',
        'PASSWORD':'root',
        'HOST': 'localhost',
        'PORT':'3306'
    },
    'database5':{
        'NAME': 'database5',
        'ENGINE': 'django.db.backends.mysql',
        'USER':'root',
        'PASSWORD':'root',
        'HOST': 'localhost',
        'PORT':'3306'
    }
}
