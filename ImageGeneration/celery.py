from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ImageGeneration.settings")

app = Celery("ImageGeneration")
app.config_from_object(settings, namespace="CELERY")
app.autodiscover_tasks()
app.conf.worker_max_tasks_per_child = 30
app.conf.worker_prefetch_multiplier = 1
app.conf.task_acks_late = True
