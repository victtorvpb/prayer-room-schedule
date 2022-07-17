from django.db import models
from django_extensions.db.models import TimeStampedModel

from apps.core.models import EmailField


class Register(TimeStampedModel):
    class Distance(models.IntegerChoices):
        distance_10 = 10, "Ate 10 KM"
        distance_20 = 20, "Ate 20 KM"
        distance_30 = 30, "Ate 30 KM"
        distance_40 = 40, "Ate 40 KM"
        distance_50 = 50, "Ate 50 KM"
        distance_100 = 100, "Mais 100 KM"

    GENDER = [("M", "Masculino"), ("F", "Feminino")]

    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = EmailField(max_length=254, blank=False, unique=True, null=False)
    zion_member = models.BooleanField(blank=False, null=False, default=False)
    gender = models.CharField(max_length=1, choices=GENDER, null=False, blank=False)
    leader = models.BooleanField(blank=False, null=False, default=False)
    zion_distance = models.IntegerField(choices=Distance.choices, null=False, blank=False)
    birth_date = models.DateField(null=False, blank=False)
