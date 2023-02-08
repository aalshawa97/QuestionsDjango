import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
from .views import homePageView
from django.test import RequestFactory


def test_my_test():
    request = RequestFactory().get('/')
    response = homePageView(request)
    #Success return code
    assert response.status_code == 200
