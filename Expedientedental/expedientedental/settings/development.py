import json
from django.core.exceptions import ImproperlyConfigured
from .base import *

with open(BASE_DIR.child('cfg.json')) as cfg:
    config = json.loads(cfg.read())


def get_config(setting, config=config):
    ''' Get configuration variables or return detailed exception. '''
    try:
        return config[setting]
    except KeyError:
        error_msg = 'Configura la variable de entorno {0}'.format(setting)
        raise ImproperlyConfigured(error_msg)

DEBUG = True

SECRET_KEY = get_config('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_config('DATABASE')['NAME'],
        'USER': get_config('DATABASE')['USER'],
        'PASSWORD': get_config('DATABASE')['PASSWORD'],
        'HOST': get_config('DATABASE')['HOST'],
        'PORT': '',
    }
}
