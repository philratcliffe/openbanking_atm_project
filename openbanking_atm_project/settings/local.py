from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backend.console.EmailBackend'

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

INSTALLED_APPS += ['debug_toolbar', 'django_extensions']

ALLOWED_HOSTS += ['localhost', '192.168.1.103']

