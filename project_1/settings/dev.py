from project_1.settings.base import *

# DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



try:
	from project_1.settings.local import *
except:
	pass