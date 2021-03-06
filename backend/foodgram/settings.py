

import os

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.getenv('SECRET_KEY', default='default')

DEBUG = False
ALLOWED_HOSTS = ['51.250.32.175', '127.0.0.1', 'localhost', 'backend']
INSTALLED_APPS = [
    'logic.apps.LogicConfig',
    'users.apps.UsersConfig',
    'recipes.apps.RecipesConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'django.contrib.admin',
    'django.contrib.auth',
    'django_filters',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djoser',
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

ROOT_URLCONF = 'foodgram.urls'

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

WSGI_APPLICATION = 'foodgram.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', default='django.db.backends.postgresql'),
        'NAME': os.getenv('DB_NAME', default='postgres'),
        'USER': os.getenv('POSTGRES_USER', default='postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', default='postgres'),
        'HOST': os.getenv('DB_HOST', default='db'),
        'PORT': os.getenv('DB_PORT', default='5432')
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
     'NAME':
     'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
    },
    {
     'NAME':
     'django.contrib.auth.password_validation.MinimumLengthValidator'
    },
    {
     'NAME':
     'django.contrib.auth.password_validation.CommonPasswordValidator'
    },
    {
     'NAME':
     'django.contrib.auth.password_validation.NumericPasswordValidator'
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

AUTH_USER_MODEL = 'users.User'


DJOSER = {
    'USER_ID_FIELD': 'id',
    'LOGIN_FIELD': 'email',
}

USERNAME_ERROR_MESSAGE = 'Данное имя пользователя уже зарегистрировано.'
FOLLOW_YOURSELF_ERROR_MESSAGE = 'Нельзя подписаться на самого себя.'
FOLLOW_ERROR_MESSAGE = 'Вы уже подписаны на этого автора.'
IN_FAVORITE_MESSAGE = 'Данный рецепт уже находится в избранном'
IN_SHOPPING_LIST_MESSAGE = 'Данный рецепт уже в вашем списке покупок.'
EMAIL_ERROR_MESSAGE = 'Данный адрес электронной почты уже зарегистрирован.'
COOKING_TIME_MESSAGE = 'Время приготовления не может быть ниже минуты.'
INGREDIENT_AMOUNT_MESSAGE = 'Количество ингредиента не может быть отрицательно'
UNIQUE_INGREDIENT_MESSAGE = 'Такой ингредиент уже есть.'
ADD_TAG_MESSAGE = 'Добавьте тэг!!'
