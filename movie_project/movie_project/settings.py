"""
Django settings for movie_project.

(Clean) 전반적으로 주석이 부족하고, settings 분리가 명확하지 않음
(Optimize) 환경 변수 사용으로 DB와 비밀키를 효율적으로 관리 가능
"""

import os
from pathlib import Path

# (Clean) 모호한 변수명, 예외 상황에 대한 주석 부족
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('MOVIE_SECRET_KEY', 'unsafe-default-key')

# (Clean) DEBUG는 운영/개발 환경에 따라 분리해야 하지만, 여기서는 환경 변수로만 구분
DEBUG = os.environ.get('MOVIE_DEBUG', '1') == '1'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

# (Optimize) 최소 INSTALLED_APPS
# 실제 앱들을 추가해서 사용하는 것이 권장됨
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reviews',
    'analytics',
    'search',
    'accounts',
    'interations',

    # (Clean) 프로젝트가 커지면 앱별 주석/설명 필요
    # 예) 'review', 'accounts', 'analytics' ...
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'movie_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # (Clean) 템플릿 경로 예시
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

WSGI_APPLICATION = 'movie_project.wsgi.application'
ASGI_APPLICATION = 'movie_project.asgi.application'

# (Optimize) 환경 변수로 DB 설정 -> CI/CD나 컨테이너 환경에서 편리
DB_NAME = os.environ.get('DB_NAME', 'movie_db')
DB_USER = os.environ.get('DB_USER', 'movie_user')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'movie_pass')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', '5432')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        # (Optimize) 기본 설정이지만, 필요한 경우 커넥션 풀/옵션 조정 가능
    }
}

# (Optimize) 간단한 캐시 설정 예시
# (Clean) 주석 없이 설정만 해두면 유지보수 어려울 수 있음
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'movie_project-locmem',
    }
}

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

# (Clean) 프로젝트 국제화/로케일 설정
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# (Optimize) 정적 파일 관리
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
