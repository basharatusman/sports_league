from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join('static'), )

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:3000',
]  # If this is used, then not need to use `CORS_ORIGIN_ALLOW_ALL = True`
CORS_ORIGIN_REGEX_WHITELIST = [
    'http://127.0.0.1:3000',
]
