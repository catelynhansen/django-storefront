from .common import *


DEBUG = True

if DEBUG:
    MIDDLEWARE += 'silk.middleware.SilkyMiddleware',

SECRET_KEY = 'django-insecure-a69n$z*k^2ks-7&mwk&51e*27(hyn-_4i#k9n9$=jd55#@l2en'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront3',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'not4uorme2c',
    }
}

