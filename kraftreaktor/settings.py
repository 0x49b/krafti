import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 't%g=4g8w6f-s-2(!ah_+#%3j@9y&o-k#*c_gjr8q8c4@&28(^q'
DEBUG = True
ALLOWED_HOSTS = ["33339.hostserv.eu", "kr.thievent.org", "127.0.0.1", "https://kr.thievent.org"]
PERMANENT_CLOSED = os.getenv('PERMANENT_CLOSED', '01.01.1900 00:00:00')
OPENING_TIMES = os.getenv('OPENING_TIMES',
                          {0: ("13:00", "22:00"), 1: ("09:00", "22:00"), 2: ("09:00", "22:00"), 3: ("09:00", "22:00"),
                           4: ("13:00", "22:00"), 5: ("09:00", "20:00"), 6: ("09:00", "20:00")})

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'drf_yasg',
    'django_filters',
    'colorfield',
    'tinymce',
    'location_field.apps.DefaultConfig',
    'drf_multiple_model',

    'counter',
    'routes',
    'climber',
    'meta',
    'trophy'
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'kraftreaktor.urls'
TEMPLATES = [
    {'BACKEND': 'django.template.backends.django.DjangoTemplates',
     'DIRS': [BASE_DIR / 'templates']
        ,
     'APP_DIRS': True,
     'OPTIONS': {
         'context_processors': [
             'django.template.context_processors.debug',
             'django.template.context_processors.request',
             'django.contrib.auth.context_processors.auth',
             'django.contrib.messages.context_processors.messages',
         ],
     },
     },
]

WSGI_APPLICATION = 'kraftreaktor.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kraftreaktor',
        'USER': 'krdb',
        'PASSWORD': 'aVeikie6noochaerathu',
        'HOST': '33339.hostserv.eu',
        'PORT': '5432', #uNg8epeigoo
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'de-de'
TIME_ZONE = 'Europe/Zurich'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

MAPBOX_KEY = "pk.eyJ1IjoiZmxvamVyZW1pYXMiLCJhIjoiY2txNW4zNjFxMDljczJvbW14aW5hczFndCJ9.WovWxlPOYsXXiIiPJeeiGA"
SECURE_SSL_REDIRECT = False
