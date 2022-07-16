from dataclasses import fields

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

from .models import (
    DaysWeek,
    DaysWeekPresbytery,
    HoursDays,
    HoursDaysPresbytery,
    Scheduler,
    SchedulerPresbytery,
)


class Scheduleresource(resources.ModelResource):
    week_day = Field(attribute="days_week__name", column_name="dia_da_semana")
    hours_days = Field(attribute="hours_days__hours", column_name="horario")

    class Meta:
        model = Scheduler
        fields = ("name", "areas", "cellphone")


@admin.register(SchedulerPresbytery)
@admin.register(Scheduler)
class SchedulerAdmin(ImportExportModelAdmin):
    search_fields = ["name", "email"]
    list_display = ["days_week", "hours_days", "name", "email"]
    ordering = ["days_week", "hours_days", "name", "email"]
    resource_class = Scheduleresource


@admin.register(DaysWeekPresbytery)
@admin.register(DaysWeek)
class DaysWeekAdmin(admin.ModelAdmin):
    pass


@admin.register(HoursDaysPresbytery)
@admin.register(HoursDays)
class HoursDaysAdmin(admin.ModelAdmin):
    pass
