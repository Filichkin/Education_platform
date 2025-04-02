from .base import *


DEBUG = False
ADMINS = [
    ('Alexey F', 'filichkin_a@.com'),
]
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
