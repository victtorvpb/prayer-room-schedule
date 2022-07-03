from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.scheduler import api_views

urlpatterns = [
    path("days_weeks/", api_views.DaysWeekList.as_view()),
    path("scheduler/", api_views.SchedulerApi.as_view()),
    path("hours_day/<int:days_week_id>/", api_views.HoursDaysApi.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
