import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()

from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

class Question(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now())
    active = models.BooleanField(default=True)

    class Meta:
        app_label = 'django_project'
class answer(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now())
    active = models.BooleanField(default=True)
    votes = models.IntegerField(default=0)

    class Meta:
        app_label = 'django_project'