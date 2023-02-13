import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()
from django.contrib import admin
from django.urls import path, include

from pages import views

urlpatterns = [
    #path("", views.index, name='index'),
    path("", include("pages.urls")),
    path('admin/', admin.site.urls),
    #path('about/', views.about, name='about'),
]
