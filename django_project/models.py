import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)

    class Meta:
        app_label = 'django_project'