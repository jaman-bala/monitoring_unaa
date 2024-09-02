from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Устанавливаем модуль настроек для Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.config.settings')

app = Celery('backend', broker='redis://redis:6379/0')

# Загружаем настройки из файла Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически ищем задачи в установленных приложениях
app.autodiscover_tasks()
