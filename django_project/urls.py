from django.contrib import admin
from django.urls import path, include  # new

from django_project import settings
from pages import views
#settings.configure()
urlpatterns = [
    #path('', views.index, name='index'),
    #path("admin/", admin.site.urls),
    path("", include("pages.urls")),  # new
    path('admin/', admin.site.urls),
]
