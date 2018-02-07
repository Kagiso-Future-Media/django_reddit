from .common import *  # noqa

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = default=True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.console.EmailBackend')

# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND' : 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}
