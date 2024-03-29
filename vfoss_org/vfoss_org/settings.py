# -*- coding: utf-8 -*-
import os

gettext = lambda s: s

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

LANGUAGES = [('en', 'en')]
DEFAULT_LANGUAGE = 0

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'mycms.db'),
        #'ENGINE': 'django.db.backends.mysql',
        #'NAME': 'thuydang_vfosscms',
				#'USER': 'vfosscmsdb',
				#'PASSWORD': 'vfosscmsdb',
				#'HOST': '',
				#'PORT': '',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 2

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

STATIC_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '0r6%7gip5tmez*vygfv+u14h@4lbt^8e2^26o#5_f_#b7%cm)u'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

STATICFILES_DIRS = (
	#os.path.join(PROJECT_DIR, 'static_dev'),
	os.path.join(PROJECT_DIR, 'themes'),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
#    'cmsplugin_blog.middleware.MultilingualBlogEntriesMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
		#'zinnia.context_processors.version', # Optional
)

THUMBNAIL_PROCESSORS = (
	'easy_thumbnails.processors.colorspace',
	'easy_thumbnails.processors.autocrop',
	#'easy_thumbnails.processors.scale_and_crop',
	'filer.thumbnail_processors.scale_and_crop_with_subject_location',
	'easy_thumbnails.processors.filters',
)

CMS_TEMPLATES = (
		('template_1.html', 'Template One'),
		('blog.html', 'Template blog'),
		('vfoss_org_v01/templates/index.html', 'vfoss_2col'),
)

ROOT_URLCONF = 'vfoss_org.urls'

TEMPLATE_DIRS = (
		# templates is not used
    os.path.join(PROJECT_DIR, 'templates'),
    os.path.join(PROJECT_DIR, 'themes'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.comments',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'cms',
    'menus',
    'mptt',
    'south',
    'filer',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    'cms.plugins.text',
## disabled due to filer
#'cms.plugins.picture',
#'cms.plugins.file',
##
    'cms.plugins.link',
    'cms.plugins.snippet',
    'cms.plugins.googlemap',
    'sekizai',
## cmsplugin-blog
    #'cmsplugin_blog',
    'simple_translation',
#'staticfiles',
    'tagging',
    'missing',
		'guardian', # optional
		'easy_thumbnails',
## zinnia
		'zinnia',
		'cmsplugin_zinnia',
)

JQUERY_JS = 'https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js'
JQUERY_UI_JS = 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/jquery-ui.min.js'
JQUERY_UI_CSS = 'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/themes/smoothness/jquery-ui.css'

# django-guardian
ANONYMOUS_USER_ID = '999'


# staticfiles
STATICFILES_FINDERS = (
		'django.contrib.staticfiles.finders.FileSystemFinder',
		'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

CMSPLUGIN_BLOG_PLACEHOLDERS = ('first', 'second', 'third')


# cmsplugin_zinnia (bridge btw django-cms and django-blog-zinnia)
CMSPLUGIN_ZINNIA_APP_MENUS = (
	'cmsplugin_zinnia.menu.EntryMenu',
	'cmsplugin_zinnia.menu.CategoryMenu',
	'cmsplugin_zinnia.menu.TagMenu',
	'cmsplugin_zinnia.menu.AuthorMenu'
)

ZINNIA_ENTRY_BASE_MODEL = 'cmsplugin_zinnia.placeholder.EntryPlaceholder'

CMSPLUGIN_ZINNIA_TEMPLATES = [
		('vfoss_org_v01/zinnia', 'zinnia_blog'),
]

CMSPLUGIN_ZINNIA_HIDE_ENTRY_MENU = True


