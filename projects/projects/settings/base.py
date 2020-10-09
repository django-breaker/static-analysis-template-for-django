import os

from pathlib import Path

from corsheaders.defaults import default_headers


BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ()
CORS_ORIGIN_WHITELIST = ()
CORS_ALLOW_HEADERS = default_headers + ('X-PROJECTS-API-TOKEN',)
CSRF_COOKIE_HTTPONLY = True
DEBUG = False
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
SECURE_BROWSER_XSS_FILTER = True

EXTERNAL_APPS = (
    'corsheaders',
    'rest_framework',
)
PROJECT_APPS = (
    'commons',
    'projects',
)
INSTALLED_APPS = EXTERNAL_APPS + PROJECT_APPS

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

APPEND_SLASH = False
ROOT_URLCONF = 'projects.urls'

WSGI_APPLICATION = 'projects.wsgi.application'

AUTH_PASSWORD_VALIDATORS = (
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
)
AUTH_USER_MODEL = None

LANGUAGE_CODE = 'en-us'
LANGUAGE_COOKIE_HTTPONLY = True
LANGUAGE_COOKIE_SAMESITE = 'Lax'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = True

TEMPLATES = ()
STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
    'DEFAULT_PAGINATION_CLASS': None,
    'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer',),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FileUploadParser',
    ),
    'DATETIME_FORMAT': '%s',
    'UNAUTHENTICATED_USER': None,
}

handler400 = 'rest_framework.exceptions.bad_request'
handler500 = 'rest_framework.exceptions.server_error'
