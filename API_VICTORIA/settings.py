"""
Django settings for API_VICTORIA project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
import os
import dj_database_url
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG') == "True"


ALLOWED_HOSTS = ['victoria-api.up.railway.app','127.0.0.1']
CSRF_COOKIE_DOMAIN = 'victoria-api.up.railway.app'
EXTERNAL_HOSTNAME = False  #config('EXTERNAL_HOSTNAME')
if EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(EXTERNAL_HOSTNAME)
    
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'Hacienda',
    'Users',
    'Clima',
    'drf_yasg',
    "django_apscheduler",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
# Configuración de autenticación con JWT
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.AutoSchema',
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # Otros métodos de autenticación, si los necesitas
    ],
}

# Configuración de JWT
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',),
    # custom time expiration token JWT
    'ACCESS_TOKEN_LIFETIME': timedelta(days=15),
}
ROOT_URLCONF = 'API_VICTORIA.urls'
"""SWAGGER SETTINGS"""
SWAGGER_SETTINGS = {
    # ...
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'JWT Authorization header using the Bearer scheme'
        }
    },
    'VALIDATOR_URL': 'https://validator.swagger.io/validator',
    'OPERATIONS_SORTER': 'alpha',
    'JSON_EDITOR': True,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_INFO': 'myapp.api_info',  # Ajusta esto con tu propia información

    # ...
}
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'API_VICTORIA.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
print("\n"*1)
print("-"*100)
Mode = "Debugg" if DEBUG == True else "Production"
print(f"Info runing\nRuning server on mode:{Mode}")
print("-"*100)
print("\n"*1)
DATABASES = {}
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': config('DATABASE_ENGINE'),
            'NAME': config('DATABASE_NAME'),
            'USER': config('DATABASE_USER'),
            'PASSWORD': config('DATABASE_PASSWORD'),
            'HOST': config('DATABASE_HOST'),
            'PORT': config('DATABASE_PORT', default=''),
            #'OPTIONS': {
                #'unix_socket': '/opt/lampp/var/mysql/mysql.sock',
                #'sql_mode': 'STRICT_TRANS_TABLES',
            #},
        }
    }

DATABASE_URL = config('DATABASE_URL')
if DATABASE_URL and not DEBUG:
    DATABASES['default'] = dj_database_url.config(
        conn_max_age=600, ssl_require=True)
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es-ec'

TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Ruta a tus archivos estáticos (donde se encuentran los archivos CSS, JavaScript, imágenes, etc.)
STATIC_URL = '/static/'

# Directorio donde se encuentran tus archivos estáticos (debes ajustar esto según la estructura de tu proyecto)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Almacenamiento de archivos estáticos utilizando WhiteNoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

