# development settings file

from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'demosite',
        'USER': 'postgres',
        'PASSWORD': 'psql',
        'HOST': 'db',
        'PORT': '5432',
    }
}