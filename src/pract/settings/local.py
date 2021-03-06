from .base import *

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'discusiones',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
            ],
        },
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),

    # '/var/www/static/',
]

SOCIAL_AUTH_FACEBOOK_KEY = '135213603618845'
SOCIAL_AUTH_FACEBOOK_SECRET = '40f61e5e0418dd9f362152b44cabe463'

SOCIAL_AUTH_TWITTER_KEY = 'TtaObKv9aSwTK3oqiMWXW1CqI'
SOCIAL_AUTH_TWITTER_SECRET = 'dyLRsBzXjY3zUOLA9m1HsbFFX9qjTQllyRq4h9MsbyJ597Wdhb'

MANDRILL_API_KEY = 'L3VE91yaZA7IXPgIHa8QdA'

