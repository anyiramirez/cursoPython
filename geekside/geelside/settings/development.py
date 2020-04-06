from .base import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h#t%6t0mi@&=$b3-n4*l9!=m!o6(y^7#9!_c$876&^j%q5uo03'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
