import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()
from django.contrib import admin
from django.urls import path, include

from pages import views as poll_views

urlpatterns = [
    #path("", views.index, name='index'),
    #Home
    path("", include("pages.urls")),
    #Django adminstration
    path('admin/', admin.site.urls),
    path('create/', poll_views.createPageView, name="create"),
    #path('vote/<poll_id>/', poll_views.home, name="home"),
    #path('', pages.Templates)
    #path('about/', views.about, name='about'),
]
