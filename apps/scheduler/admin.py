from django.contrib import admin
from .models import Scheduler, DaysWeek, HoursDays


@admin.register(Scheduler)
class SchedulerAdmin(admin.ModelAdmin):
    search_fields = ['name','email']
    list_display = ('name','email', 'days_week', 'hours_days')


@admin.register(DaysWeek)
class DaysWeekAdmin(admin.ModelAdmin):
    pass


@admin.register(HoursDays)
class HoursDaysAdmin(admin.ModelAdmin):
    pass
