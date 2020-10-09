from .base import *  # isort:skip


ALLOWED_HOSTS = ['*']
DEBUG = True

PROJECT_PROFILE = 'LOCAL'
PROJECT_VERSION = os.getenv('PROJECT_VERSION')

DATABASES = {}
