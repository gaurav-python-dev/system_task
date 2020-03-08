from .base import *
DEBUG = True
ALLOWED_HOSTS = ['domail-ip','www.systango.com']

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

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

