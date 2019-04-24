from .base import *  # NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_db',
        'USER': 'blog',
        'PASSWORD': 'blog123.',
        'HOST': '192.168.174.130',
        'PORT': 3306
    }
}
