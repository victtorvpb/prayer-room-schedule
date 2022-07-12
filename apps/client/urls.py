from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from apps.client import views

urlpatterns = [
    path("scheduler", views.SchedulerView.as_view(), name="scheduler"),
    path(
        "scheduler_presbitery",
        views.SchedulerPresbiteryView.as_view(),
        name="scheduler_presbitery",
    ),
    path("", views.Main.as_view(), name="main"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
