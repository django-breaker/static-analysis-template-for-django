from .base import *

CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

PROJECT_PROFILE = 'TEST'
PROJECT_VERSION = os.getenv('PROJECT_VERSION')

DATABASES = {}