import os

#from django.contrib.auth.models import User
from django.utils import timezone

import django
#import django.utils import timezone
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()
from django.db import models

class Question(models.Model):
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now())
    #active = models.BooleanField(default=True)

    class Meta:
        app_label = 'django_project'