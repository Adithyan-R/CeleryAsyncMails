# myproject/celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AsyncMails.settings')

app = Celery('AsyncMails')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

'''
from celery.schedules import crontab

app.conf.beat_schedule = {
    'run-periodic-task-every-minute': {
        'task': 'myapp.tasks.periodic_task',
        'schedule': crontab(minute='*/1'),  # every minute
    },
}'''

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')