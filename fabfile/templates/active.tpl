from settings.production import *

CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
		'LOCATION': '%(memcache_location)s',
		'KEY_PREFIX': 'FEED_SCRAPER',
		'VERSION'	: 1,
	}
}

EMAIL_HOST = '%(email_host)s'
EMAIL_PORT = '%(email_port)s'
EMAIL_USE_TLS = %(email_use_tls)s
EMAIL_HOST_USER = '%(email_user)s'
EMAIL_HOST_PASSWORD = '%(email_password)s'
DEFAULT_FROM_EMAIL = '%(email_from)s'
SERVER_EMAIL = '%(email_server_email)s'

SECRET_KEY = '%(secret_key)s'
