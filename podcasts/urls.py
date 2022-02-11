from unicodedata import name
from django.urls import re_path

from .views import HomePageView

urlpatterns = [
    re_path("", HomePageView.as_view(), name="homepage"),
]