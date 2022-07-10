from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from apps.client import views

urlpatterns = [
    path("scheduler", views.SchedulerView.as_view(), name="scheduler"),
    path("", views.Main.as_view(), name="main"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
