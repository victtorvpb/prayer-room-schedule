from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.client import views

urlpatterns = [
    path("", views.SchedulerView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
