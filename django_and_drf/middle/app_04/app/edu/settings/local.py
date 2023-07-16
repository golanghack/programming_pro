from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.backends.sqlite3',
        'NAME': BASE_DIR / 'db.db.sqlite3',
    }
}