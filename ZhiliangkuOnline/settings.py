"""
Django settings for ZhiliangkuOnline project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import datetime
import os
import sys

import six

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'propaganda'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vz3i%_j-f&vw2=1um@ru%!m5s-7z)vw1_pez8_r0mp5doooh21'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# 自定义认证，设置'邮箱'用户名'手机号'均可登录
AUTHENTICATION_BACKENDS = (
	'users.backends.CustomBackend',
	'social_core.backends.weibo.WeiboOAuth2',
	'social_core.backends.qq.QQOAuth2',
	'social_core.backends.weixin.WeixinOAuth2',
	'social_core.backends.weixin.WeixinOAuth2APP',
	'django.contrib.auth.backends.ModelBackend',
)

# 此处重载是为了使我们的UserProfile生效
AUTH_USER_MODEL = "users.UserProfile"

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	'corsheaders',
	'rest_framework',
	'rest_framework.authtoken',
	'social_django_mongoengine',  # 第三方登录
	'django_filters',
	'debug_toolbar',
	'rest_framework_swagger',
	'raven.contrib.django.raven_compat',

	'banner',  # 轮播
	'users',  # 用户
	'user_operation',  # 用户的操作
	'user_resumes',  # 用户简历
	'directory_tree',  # 项目结构树
	'project',  # 项目
	"course",  # 课程
	'video',  # 视频
	"exercise",  # 练习
	'assessments',  # 考核
	'community',  # 社区
	'live_streaming',  # 直播
	'medal',  # 勋章
	'notification',  # 消息管理
	'technical_label',  # 技术标签

	# 企业宣传
	'wechat_promotion',
	"questionnaire",
	"user_score",
]

MIDDLEWARE = [
	'corsheaders.middleware.CorsMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'debug_toolbar.middleware.DebugToolbarMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'ZhiliangkuOnline.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates')],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'social_django.context_processors.backends',
				'social_django.context_processors.login_redirect',
			],
		},
	},
]

WSGI_APPLICATION = 'ZhiliangkuOnline.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'djongo',
		'NAME': 'zhiliangku',
		"USER": "",
		"PASSWORD": "",
		"HOST": "localhost",
		"PORT": 27017,
		'ENFORCE_SCHEMA': False,
	}
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# 与drf的jwt相关的设置
JWT_AUTH = {
	'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=60 * 60 * 24),
	'JWT_AUTH_HEADER_PREFIX': 'Bearer',
	'JWT_ALLOW_REFRESH': True,  # 启用JWT，token刷新功能
}

# drf，配置
REST_FRAMEWORK = {
	# 权限
	'DEFAULT_PERMISSION_CLASSES': (
		'rest_framework.permissions.IsAuthenticated',
	),

	# 认证
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
		'rest_framework.authentication.BasicAuthentication',
		'rest_framework.authentication.SessionAuthentication',
	),

	# 接口数据分页
	'PAGE_SIZE': 10,
	'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',

	# # 截流
	# 'DEFAULT_THROTTLE_CLASSES': (
	# 	'rest_framework.throttling.AnonRateThrottle',
	# 	'rest_framework.throttling.UserRateThrottle'
	# ),
	# 'DEFAULT_THROTTLE_RATES': {
	# 	'anon': '1000/day',
	# 	'user': '1000/day',
	# }

	# 过滤
	'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)

}

# corsheaders
CORS_ORIGIN_WHITELIST = (
	# '*'
	'127.0.0.1:8000',  # 请求的域名
	'localhost:8000',
	'localhost',
)

# 缓存过期时间
REST_FRAMEWORK_EXTENSIONS = {
	'DEFAULT_CACHE_RESPONSE_TIMEOUT': 60 * 60,
	'DEFAULT_USE_CACHE': 'default',
	'DEFAULT_CACHE_ERRORS': False,
	'DEFAULT_OBJECT_CACHE_KEY_FUNC':
		'rest_framework_extensions.utils.default_object_cache_key_func',
	'DEFAULT_LIST_CACHE_KEY_FUNC':
		'rest_framework_extensions.utils.default_list_cache_key_func',
}

CACHES = {
	"default": {
		"BACKEND": "django_redis.cache.RedisCache",
		"LOCATION": "redis://127.0.0.1:6379/",
		"OPTIONS": {
			"CLIENT_CLASS": "django_redis.client.DefaultClient",
		}
	}
}

# 使用redis管理session
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# 阿里云短信设置
APPKEY = '23764268'
SECRET = "00181054a64e2d9eb69711912d7a372a"

# django调试工具，debug_toolbar
DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = ("127.0.0.1",)
DEBUG_TOOLBAR_PANELS = [
	'debug_toolbar.panels.versions.VersionsPanel',
	'debug_toolbar.panels.timer.TimerPanel',
	'debug_toolbar.panels.settings.SettingsPanel',
	'debug_toolbar.panels.headers.HeadersPanel',
	'debug_toolbar.panels.request.RequestPanel',
	'debug_toolbar.panels.sql.SQLPanel',
	'debug_toolbar.panels.staticfiles.StaticFilesPanel',
	'debug_toolbar.panels.templates.TemplatesPanel',
	'debug_toolbar.panels.cache.CachePanel',
	'debug_toolbar.panels.signals.SignalsPanel',
	'debug_toolbar.panels.logging.LoggingPanel',
	'debug_toolbar.panels.redirects.RedirectsPanel',
]
CONFIG_DEFAULTS = {
	# Toolbar options
	'DISABLE_PANELS': {'debug_toolbar.panels.redirects.RedirectsPanel'},
	'INSERT_BEFORE': '</body>',
	'JQUERY_URL': '//cdn.bootcss.com/jquery/2.1.4/jquery.min.js',
	'RENDER_PANELS': None,
	'RESULTS_CACHE_SIZE': 10,
	'ROOT_TAG_EXTRA_ATTRS': '',
	'SHOW_COLLAPSED': False,
	'SHOW_TOOLBAR_CALLBACK': 'debug_toolbar.middleware.show_toolbar',
	# Panel options
	'EXTRA_SIGNALS': [],
	'ENABLE_STACKTRACES': True,
	'HIDE_IN_STACKTRACES': (
		'socketserver' if six.PY3 else 'SocketServer',
		'threading',
		'wsgiref',
		'debug_toolbar',
		'django',
	),
	'PROFILER_MAX_DEPTH': 10,
	'SHOW_TEMPLATE_CONTEXT': True,
	'SKIP_TEMPLATE_PREFIXES': (
		'django/forms/widgets/',
		'admin/widgets/',
	),
	'SQL_WARNING_THRESHOLD': 500,  # milliseconds
}

# 第三方认证
SOCIAL_AUTH_STORAGE = 'social_django_mongoengine.models.DjangoStorage'
SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_WEIBO_KEY = ''
SOCIAL_AUTH_TWITTER_SECRET = ''

SOCIAL_AUTH_QQ_KEY = ''
SOCIAL_AUTH_QQ_SECRET = ''

SOCIAL_AUTH_WEIXIN_KEY = ''
SOCIAL_AUTH_WEIXIN_SECRET = ''

# 第三方登录成功后跳转页面
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/index/'

# 创建日志的路径
LOG_PATH = os.path.join(BASE_DIR, 'log')
# 如果地址不存在，则会自动创建log文件夹
if not os.path.isdir(LOG_PATH):
	os.mkdir(LOG_PATH)

REGEX_MOBILE = "^1[345789]\d{9}$|^147\d{8}$|^176\d{8}$"

# 文档页面
LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'

# 文档页面
SWAGGER_SETTINGS = {
	# 'SECURITY_DEFINITIONS': {
	# 	'basic': {
	# 		'type': 'basic'
	# 	}
	# },
	'SECURITY_DEFINITIONS': {
		'api_key': {
			'type': 'apiKey',
			'in': 'header',
			'name': 'Authorization'
		}
	},
	'LOGIN_URL': 'rest_framework:login',
	'LOGOUT_URL': 'rest_framework:logout',
	'DOC_EXPANSION': "list",
	'JSON_EDITOR': True,
	'OPERATIONS_SORTER': 'method',
	'SHOW_REQUEST_HEADERS': True,
	"is_superuser": True,
	"is_authenticated": True,
}

RAVEN_CONFIG = {
	'dsn': '',
}

# 邮箱
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = '18146560703@163.com'
EMAIL_HOST_PASSWORD = 'xhl1991'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# # 日志
# LOGGING = {
# 	# version 值只能为1
# 	'version': 1,
#
# 	# True 表示禁用loggers
# 	'disable_existing_loggers': True,
#
# 	# < 格式化 >
# 	'formatters': {
# 		# 可以设置多种格式，根据需要选择保存的格式
# 		'default': {'format': '%(levelname)s %(funcName)s %(module)s %(asctime)s %(message)s'},
# 		'simple': {'format': '%(levelname)s %(module)s %(asctime)s %(message)s'},
# 		'standard': {
# 			'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
# 	},
#
# 	'filters': {
# 		'require_debug_false': {
# 			'()': 'django.utils.log.RequireDebugFalse'
# 		}
# 	},
#
# 	# < 处理信息 >
# 	'handlers': {
# 		'mail_admins': {
# 			'level': 'ERROR',
# 			'filters': ['require_debug_false'],
# 			'class': 'django.utils.log.AdminEmailHandler',
# 			'include_html': True,
#
# 		},
# 		'default': {
# 			'level': 'DEBUG',
# 			'class': 'logging.handlers.RotatingFileHandler',
# 			'filename': '%s/all.txt' % LOG_PATH,  # 日志输出文件
# 			'maxBytes': 1024 * 1024 * 5,  # 文件大小
# 			'backupCount': 5,  # 备份份数
# 			'formatter': 'standard',  # 使用哪种formatters日志格式
# 		},
# 		'error': {
# 			'level': 'ERROR',
# 			'class': 'logging.handlers.RotatingFileHandler',
# 			'filename': '%s/error.txt' % LOG_PATH,
# 			'maxBytes': 1024 * 1024 * 5,
# 			'backupCount': 5,
# 			'formatter': 'standard',
# 		},
# 		'console': {
# 			'level': 'DEBUG',
# 			'class': 'logging.StreamHandler',
# 			'formatter': 'standard'
# 		},
# 		'request_handler': {
# 			'level': 'DEBUG',
# 			'class': 'logging.handlers.RotatingFileHandler',
# 			'filename': '%s/console.txt' % LOG_PATH,
# 			'maxBytes': 1024 * 1024 * 5,
# 			'backupCount': 5,
# 			'formatter': 'standard',
# 		},
# 		'scprits_handler': {
# 			'level': 'DEBUG',
# 			'class': 'logging.handlers.RotatingFileHandler',
# 			'filename': '%s/scprits.txt' % LOG_PATH,
# 			'maxBytes': 1024 * 1024 * 5,
# 			'backupCount': 5,
# 			'formatter': 'standard',
# 		}
# 	},
# 	'loggers': {
# 		'django': {
# 			'handlers': ['default', 'console'],
# 			'level': 'DEBUG',
# 			'propagate': False
# 		},
# 		'django.request': {
# 			'handlers': ['request_handler'],
# 			'level': 'DEBUG',
# 			'propagate': False,
# 		},
# 		'scripts': {
# 			'handlers': ['scprits_handler'],
# 			'level': 'INFO',
# 			'propagate': False
# 		},
# 		'sourceDns.webdns.views': {
# 			'handlers': ['default', 'error'],
# 			'level': 'DEBUG',
# 			'propagate': True
# 		},
# 		'sourceDns.webdns.util': {
# 			'handlers': ['error'],
# 			'level': 'ERROR',
# 			'propagate': True
# 		}
# 	}
# }
