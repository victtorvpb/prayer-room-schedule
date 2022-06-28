import uuid

from django_extensions.db.models import TimeStampedModel
from django.db import models
from apps.core.models import EmailField


class DaysWeek(TimeStampedModel):
    name = models.CharField(max_length=20, blank=False, unique=True, null=False)


class HoursDays(TimeStampedModel):
    hours = models.TimeField(blank=False, null=False)
    active = models.BooleanField(default=True, blank=False, null=False)


class Scheduler(TimeStampedModel):
    name = models.CharField(max_length=200, blank=False, unique=True, null=False)
    email = EmailField(max_length=254, blank=False, unique=True, null=False)
    cellphone = models.CharField(max_length=12, blank=False, unique=True, null=False)

    days_week = models.ForeignKey(DaysWeek, on_delete=models.PROTECT)

    hours_days = models.ForeignKey(HoursDays, on_delete=models.PROTECT)
