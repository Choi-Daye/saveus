import os
import json
import sys
from pathlib import Path
from datetime import timedelta

# settings.py 맨 위에 추가
import django.utils.translation
django.utils.translation.ugettext_lazy = django.utils.translation.gettext_lazy

# Channels settings
from channels.security.websocket import AllowedHostsOriginValidator

SITE_ID=3

BASE_DIR = Path(__file__).resolve().parent.parent

# secret.json 파일 읽어오기
SECRET_BASE_FILE = os.path.join(BASE_DIR, "secrets.json")

# secret.json 파일을 읽고, json key/value 값들을 secrets 에 할당함
try:
    with open(SECRET_BASE_FILE) as f:
        secrets = json.load(f)
except FileNotFoundError:
    # 로그 또는 알림을 추가하여 파일이 없음을 알립니다
    print("secret 파일 읽기 실패!")

# setattr을 이용하여 key 값은 변수명, value 값은 값으로 각 변수에 할당
for key, value in secrets.items():
    setattr(sys.modules[__name__], key, value)

DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1', 
    'localhost',
    "3a145eca76f9.ngrok.app",  # 8080 서버
    secrets["NGROK_DOMAIN"].replace("https://", "").replace("http://", ""),
    ]

INSTALLED_APPS = [
    # Third-party apps
    'corsheaders',
    'rest_framework', # df_rest_auth 를 사용하려면 아래 app이 선행되어야 함
    'rest_framework.authtoken', 
    
    # 사용자 제작 django app
    # 'user',
    'main',
    'map',
    'odsay',
    'card',
    'calculate',

    # dj_rest_auth 의 registraiton 을 사용하기 위해서 app 추가 필요
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    
    # dj_rest_auth
    'dj_rest_auth',
    'dj_rest_auth.registration',
    
    #token
    'rest_framework_simplejwt',
]

MIDDLEWARE = [
    # 보안 middleware 는 가장 앞에 위치
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # CORS 관련 설정
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# Channel Layers 설정
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('127.0.0.1', 6379)],
        },
    },
}

# ASGI application 설정
ASGI_APPLICATION = 'saveus.asgi.application'


# CSRF 설정
CSRF_COOKIE_HTTPONLY = False  # 클라이언트에서 접근 가능하도록 설정
CSRF_COOKIE_SECURE = False    # HTTPS가 아닌 경우 False로 설정
CSRF_COOKIE_SAMESITE = None   # CSRF 쿠키가 교차 사이트 요청에서도 설정되도록 함

CORS_ALLOW_CREDENTIALS = True   # 자격 증명을 포함한 요청 허용
# CORS_ALLOW_ALL_ORIGINS = True   # 모든 출처에서의 요청 허용

# CORS_ALLOW_HEADERS 추가 (필요할 경우)
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "https://3a145eca76f9.ngrok.app",
    "https://d5bf569728f0.ngrok.app"
]

# CSRF 설정
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8080',
    "http://127.0.0.1:8080",
    "https://3a145eca76f9.ngrok.app",
    "https://d5bf569728f0.ngrok.app"
] # Vue.js 개발 서버 주소를 신뢰된 출처로 추가

ROOT_URLCONF = 'saveus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../FRONT', 'dist')],
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

WSGI_APPLICATION = 'saveus.wsgi.application'

# Database
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER' : 'root',
        'PASSWORD' : 'admin1234', # 설정한 비밀번호로 적어주면 된다.
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
    }
}

# Password validation
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
LANGUAGE_CODE = 'ko'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '../FRONT', 'dist'),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# rest framework 에 대한 설정
REST_FRAMEWORK = {
    # 기본 인증에 대한 설정
    'DEFAULT_AUTHENTICATION_CLASSES' : (
        # dj_rest_auth의 인증 절차 중 JWTCoojoeAuthentication을 사용
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    # 허가에 대한 설정
    'DEFAULT_PERMISSION_CLASSES': {
        # 인증이 완료된 사용자에 한해서 접근 허가
        'rest_framework.permissions.IsAuthenticated',
    }
}

# Cookie key 와 refresh cookie key 의 이름을 설정
JWT_AUTH_COOKIE = 'sociallogin-auth'
JWT_AUTH_REFRESH_COOKIE = 'sociallogin-refresh-token'

# JWT 사용을 위한 설정
REST_USE_JWT = True

# simiplejwt 에 대한 설정
SIMPLE_JWT = {
    # access token 의 유효기간
    'ACCESS_TOKEN_LIFETIME' : timedelta(minutes=60),
    # refresh token 의 유효기간
    'REFRESH_TOKEN_LIFETIME' : timedelta(days=2),
    # 토큰에 들어가는 알고리즘
    'ALGORITHM' : 'HS256',
    # 토큰을 만드는데 사용할 secret key
    'SIGNING_KEY' : SECRET_KEY,
}

# SOCIALACCOUNT_PROVIDERS 설정 추가
SOCIALACCOUNT_PROVIDERS = secrets.get("SOCIALACCOUNT_PROVIDERS", {})


# allauth backends
AUTHENTICATION_BACKENDS = (
    #Needed to login by username in Django admin, regardless of 'allauth'
    'django.contrib.auth.backends.ModelBackend',
    
)
