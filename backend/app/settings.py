from garpixcms.settings import *  # noqa

INSTALLED_APPS += [
    'home',
    'hotels',
]

FEEDBACK_EVENT = 1

NOTIFY_EVENTS = {
    FEEDBACK_EVENT: {
        'title': 'бронирование',
    },
}

CHOICES_NOTIFY_EVENT = sorted([(k, v['title']) for k, v in NOTIFY_EVENTS.items()], key=lambda x: x[1])


CELERY_ENABLE_UTC = False
DJANGO_CELERY_BEAT_TZ_AWARE = False
