from celery import Celery 
import os 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_01.settings')
app = Celery('recipe_01')

app.config_from_object('django.conf.settings', namespace='CELERY')
app.autodiscover_tasks()

