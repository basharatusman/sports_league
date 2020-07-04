from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = ['fitsnapr.herokuapp.com', '127.0.0.1']

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_DEFAULT_ACL = None
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

CLOUDFRONT_DOMAIN = os.environ.get('CLOUDFRONT_DOMAIN')
CLOUDFRONT_ID = os.environ.get('CLOUDFRONT_ID')

AWS_S3_CUSTOM_DOMAIN = CLOUDFRONT_DOMAIN

STATIC_LOCATION = 'static'
STATIC_URL = f'https://{CLOUDFRONT_DOMAIN}/{STATIC_LOCATION}/'
STATICFILES_STORAGE = 'fitsnapr.storage_backends.StaticStorage'
STATIC_ROOT = 'static'

MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{CLOUDFRONT_DOMAIN}/{MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'fitsnapr.storage_backends.PublicMediaStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
