from __future__ import absolute_import, unicode_literals

import os
import time
from celery import Celery,shared_task
# from api.models import student
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rfw.settings')

app = Celery('rfw')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# celer was working driectly in windwo 

# celery -A <module> worker -l info -P gevent   
# celery -A rfw.celery worker -l info -P gevent 





@app.task(bind=True)
#
def debug_task(self):
    for i in range(6): 
    
        time.sleep(5)
        # s=student(5+i,"s"+str(i))
        # s.create() 
        print(i,'hiiiiiiiiiiii')

    