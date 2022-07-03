from rest_framework import serializers
from apps.scheduler.models import DaysWeek, HoursDays, Scheduler


class DaysWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaysWeek
        fields = ["name", "pk"]


class HoursDayserializer(serializers.ModelSerializer):
    class Meta:
        model = HoursDays
        fields = ["hours", "pk"]


class Schedulererializer(serializers.ModelSerializer):
    nome_day = serializers.SerializerMethodField()
    nome_hora = serializers.SerializerMethodField()

    class Meta:
        model = Scheduler
        exclude = ["id", "created", "modified"]

    def get_nome_day(self, obj):
        return obj.days_week.name

    def get_nome_hora(self, obj):
        return obj.hours_days.hours
