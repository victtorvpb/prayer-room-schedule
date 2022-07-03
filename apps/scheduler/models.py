import uuid
from django.dispatch import receiver

from django_extensions.db.models import TimeStampedModel
from django.db import models
from apps.core.models import EmailField
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError


class DaysWeek(TimeStampedModel):
    name = models.CharField(max_length=20, blank=False, unique=True, null=False)

    def __str__(self) -> str:
        return str(self.name)


class HoursDays(TimeStampedModel):
    hours = models.TimeField(blank=False, null=False)
    active = models.BooleanField(default=True, blank=False, null=False)

    def __str__(self) -> str:
        return str(self.hours)


class Scheduler(TimeStampedModel):
    name = models.CharField(max_length=200, blank=False, unique=True, null=False)
    email = EmailField(max_length=254, blank=False, unique=True, null=False)
    cellphone = models.CharField(max_length=12, blank=False, unique=True, null=False)

    days_week = models.ForeignKey(DaysWeek, on_delete=models.PROTECT)

    hours_days = models.ForeignKey(HoursDays, on_delete=models.PROTECT)


def prevent_save_three_hours(sender, instance, **kwargs):
    if not instance.pk:
        check_day_hours = (
            sender.objects.filter(
                days_week=instance.days_week, hours_days=instance.hours_days
            ).count()
            >= 2
        )

        if check_day_hours:
            raise ValidationError("NÃO FOI POSSIVEL FAZER AGENDAMENT")


pre_save.connect(prevent_save_three_hours, sender=Scheduler)
