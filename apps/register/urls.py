from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from apps.client import views
from apps.register import views

urlpatterns = [
    path("/", views.RevisterFormView.as_view(), name="register_view"),
    re_path("register_sucess", views.RegisterSucessView.as_view(), name="register_sucess_view"),
]


urlpatterns = format_suffix_patterns(urlpatterns)
