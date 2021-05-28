"""
Django settings for api_droids project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import datetime
from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "!!!SET DJANGO_SECRET_KEY!!!")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = eval(os.environ.get('ALLOWED_HOSTS', "['*']"))


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'demands',
    'accounts',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_spectacular',
    'drf_yasg',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api_droids.urls'

ADMIN_URL = os.environ.get("DJANGO_ADMIN_URL", "admin/")

LOCALE_PATHS = (
    ROOT_DIR / 'locale',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(ROOT_DIR / "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'api_droids.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

POSTGRES_USER = os.environ.get("POSTGRES_USER", 'clebsonpy')
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", 'droidhub')
POSTGRES_DB = os.environ.get("POSTGRES_DB", 'droidhub')
POSTGRES_URL = os.environ.get("POSTGRES_URL", 'postgres')

DATABASES = {
    'default': dj_database_url.parse(
        f'postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_URL}:5432/{POSTGRES_DB}',
        conn_max_age=600
    ),
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Maceio'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/djstatic/'
STATIC_ROOT = ROOT_DIR / 'staticfiles'
STATICFILES_DIRS = (
    ROOT_DIR / 'media',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = ROOT_DIR / 'media/'

REST_FRAMEWORK = {
    'PAGE_SIZE': '10',
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
       'rest_framework_simplejwt.authentication.JWTAuthentication',
       'rest_framework.authentication.BasicAuthentication',
       'rest_framework.authentication.SessionAuthentication',)

}

SPECTACULAR_SETTINGS = {
    'COMPONENT_NO_READ_ONLY_REQUIRED': True
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'TOKEN_REFRESH_LIFETIME': datetime.timedelta(days=1),
}

SWAGGER_SETTINGS = {
    'LOGIN_URL': '/api/v1/accounts/login',
    'LOGOUT_URL': '/api/v1/accounts/logout',
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    },
    'USE_SESSION_AUTH': True
}



REDOC_SETTINGS = {
   'LAZY_RENDERING': False,
}
