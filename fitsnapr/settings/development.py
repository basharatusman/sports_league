from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join('static'), )

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
