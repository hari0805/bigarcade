"""
Django settings for bigarcade project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    "home",
    "search",
    "blog",
    "wagtailcodeblock",
    "django_comments_xtd",
    "django_comments",
    "widget_tweaks",

    "django.contrib.sites",
    "wagtail.contrib.table_block",
    "wagtail.contrib.modeladmin",
    "wagtail.contrib.styleguide",
    "wagtail.contrib.settings",


    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "bigarcade.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
            ],
        },
    },
]

WSGI_APPLICATION = "bigarcade.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/4.1/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


# Wagtail settings

WAGTAIL_SITE_NAME = "bigarcade"

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "localhost:8000"  #"http://example.com"


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# codeblock settings

WAGTAIL_CODE_BLOCK_LINE_NUMBERS = False

WAGTAIL_CODE_BLOCK_THEME = None

WAGTAIL_CODE_BLOCK_COPY_TO_CLIPBOARD = True

WAGTAIL_CODE_BLOCK_LANGUAGES = (
    ('bash', 'Bash/Shell'),
    ('css', 'CSS'),
    ('diff', 'diff'),
    ('html', 'HTML'),
    ('javascript', 'Javascript'),
    ('json', 'JSON'),
    ('python', 'Python'),
    ('scss', 'SCSS'),
    ('yaml', 'YAML'),
)

# post comment settings

COMMENTS_XTD_CONFIRM_EMAIL = False

COMMENTS_XTD_MODEL = 'blog.models.CustomComment'

SITE_ID = 1

#smpt EmailBackend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL_* settings so that Django can send emails:
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = "587"
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'sk.hari0805@gmail.com'
EMAIL_HOST_PASSWORD = 'karan@2000'
DEFAULT_FROM_EMAIL = "sk.hari0805@gmail.com"

COMMENTS_APP = 'django_comments_xtd'
COMMENTS_XTD_SALT = (b"Timendi causa est nescire. "
                     b"Aequam memento rebus in arduis servare mentem.")
COMMENTS_XTD_FROM_EMAIL = "noreply@example.com"
COMMENTS_XTD_CONTACT_EMAIL = "helpdesk@example.com"

COMMENTS_XTD_MAX_THREAD_LEVEL = 1  # default is 0
COMMENTS_XTD_LIST_ORDER = ('-thread_id', 'order')  # default is ('thread_id', 'order')
COMMENTS_XTD_APP_MODEL_OPTIONS = {
    'blog.BlogPage': {
        'allow_flagging': False,
        'allow_feedback': True,
        'show_feedback': True,
    }
}