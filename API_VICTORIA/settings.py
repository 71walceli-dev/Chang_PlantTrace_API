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


ALLOWED_HOSTS = []
CSRF_COOKIE_DOMAIN = config('SITE')
SESSION_COOKIE_PATH = '/api/auth/admin/'  # Ruta del panel de administración
CSRF_COOKIE_PATH = '/api/auth/admin/'  # Ruta del panel de administración
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
CSRF_TRUSTED_ORIGINS = [config('SITE')]
DJANGO_ADMIN_URL='/api/auth/admin/'

EXTERNAL_HOSTNAME = config('EXTERNAL_HOSTNAME')
if EXTERNAL_HOSTNAME:
    EXTERNAL_HOSTNAME = EXTERNAL_HOSTNAME.split(",")
    for HOST in EXTERNAL_HOSTNAME:
        ALLOWED_HOSTS.append(HOST)
print(ALLOWED_HOSTS)
# Application definition
INSTALLED_APPS = [
    'corsheaders',
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
    'django_apscheduler',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'Users.middlewares.HaciendaMiddleware.HaciendaMiddleware',
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
#CORRs setings
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "OPTIONS",
]

#if DEBUG:
CORS_ALLOW_ALL_ORIGINS = False
origins=config("CORS_ALLOWED_ORIGINS")
if origins:
    CORS_ALLOWED_ORIGINS = origins.split(",")
    print(CORS_ALLOWED_ORIGINS)
#else:
#    origins=config("CORS_ALLOWED_ORIGINS")
#    if origins:
#        CORS_ALLOWED_ORIGINS = origins.split(",")
#        print(CORS_ALLOWED_ORIGINS)

# Configuración de JWT
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',),
    # custom time expiration token JWT
    'ACCESS_TOKEN_LIFETIME': timedelta(days=36500),
}
ROOT_URLCONF = 'API_VICTORIA.urls'
"""SWAGGER SETTINGS"""
SWAGGER_SETTINGS = {
    # ...
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.permissions.AllowAny',
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
""" APSCHEDULER CONFIG"""
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_TIMEZONE = "UTC"
APSCHEDULER_JOBSTORES = {
    'default': {
        'class': 'django_apscheduler.jobstores:DjangoJobStore',
        'OPTIONS': {
            'database_url': 'default',
            'tablename': 'apscheduler_djangojob',
            'idcol': 'id',
            'datecol': 'date',
        },
    },
}
SCHEDULER_AUTOSTART = True
SCHEDULER_CONFIG = {
    'apscheduler.jobstores.default': {
        'type': 'django_apscheduler.jobstores:DjangoJobStore',
    },
    'apscheduler.executors.default': {
        'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
        'max_workers': '20',  # Número máximo de trabajadores en el grupo de trabajadores
    },
    'apscheduler.timezone': 'UTC',  # Zona horaria (por ejemplo, 'UTC' o 'America/New_York')
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'Clima', 'template')],
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
else:
    INSTALLED_APPS.append('django.contrib.postgres')
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
    DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql'
    DATABASES['default']['NAME'] = str(config('DATABASE_NAME'))
    DATABASES['default']['USER'] = str(config('DATABASE_USER'))
    DATABASES['default']['PASSWORD'] = str(config('DATABASE_PASSWORD'))
    DATABASES['default']['HOST'] = str(config('DATABASE_HOST'))
    DATABASES['default']['PORT'] = str(config('DATABASE_PORT'))

""" DATABASE_URL = config('DATABASE_URL')
if DATABASE_URL and not DEBUG:
    DATABASES['default'] = dj_database_url.config(
        conn_max_age=600, ssl_require=True) """
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

"""Configure Mail Services"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'trabajocolaborativo.pis@gmail.com'  # Tu dirección de correo
EMAIL_HOST_PASSWORD = 'liou cfwa hgbz ndeu'  # La contraseña de aplicación generada

