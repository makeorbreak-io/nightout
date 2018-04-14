"""
Django settings for nightout project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainsite',
    'social_django',
    'sslserver',
    'letsencrypt',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'nightout.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ './templates',
                  'mainsite/templates',
                ],
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

WSGI_APPLICATION = 'nightout.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
 
AUTHENTICATION_BACKENDS = ( 
    'social_core.backends.facebook.FacebookOAuth2', 
    'django.contrib.auth.backends.ModelBackend', 
) 
 
#Facebook Authentication 
SOCIAL_AUTH_FACEBOOK_KEY = '1312905502189567'  # App ID 
SOCIAL_AUTH_FACEBOOK_SECRET = 'c4cfa911ca84c7efc64461323c7033e4'  # App Secret 
 
# Internationalization 
# https://docs.djangoproject.com/en/2.0/topics/i18n/ 
 
LANGUAGE_CODE = 'en-us' 
 
TIME_ZONE = 'UTC' 
 
USE_I18N = True 
 
USE_L10N = True 
 
USE_TZ = True 
 
 
# Static files (CSS, JavaScript, Images) 
# https://docs.djangoproject.com/en/2.0/howto/static-files/ 
 
STATIC_ROOT = '' 
STATIC_URL = '/static/' 
STATICFILES_DIRS = ( os.path.join('static'), ) 
 
LOGIN_URL = 'login' 
LOGOUT_URL = 'logout' 
LOGIN_REDIRECT_URL = 'mainpage' 
