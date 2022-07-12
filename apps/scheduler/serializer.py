from rest_framework import serializers

from apps.scheduler.models import (
    DaysWeek,
    DaysWeekPresbytery,
    HoursDays,
    HoursDaysPresbytery,
    Scheduler,
    SchedulerPresbytery,
)


class DaysWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaysWeek
        fields = ["name", "pk"]


class DaysWeekPresbyterySerializer(DaysWeekSerializer):
    class Meta:
        model = DaysWeekPresbytery
        fields = ["name", "pk"]


class HoursDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = HoursDays
        fields = ["hours", "pk"]


class HoursDaysPresbyterySerializer(HoursDaySerializer):
    class Meta:
        model = HoursDaysPresbytery
        fields = ["hours", "pk"]


class SchedulerSerializer(serializers.ModelSerializer):
    nome_day = serializers.SerializerMethodField()
    nome_hora = serializers.SerializerMethodField()

    class Meta:
        model = Scheduler
        exclude = ["id", "created", "modified"]
        extra_kwargs = {
            "name": {
                "error_messages": {
                    "blank": "Nome é obrigatório",
                    "unique": "Nome já cadastrado",
                    "null": "Nome é obrigatório",
                }
            },
            "email": {
                "error_messages": {
                    "blank": "Email é obrigatório",
                    "unique": "Email já cadastrado",
                    "null": "Email é obrigatório",
                }
            },
            "cellphone": {
                "error_messages": {
                    "blank": "Telefone é obrigatório",
                    "unique": "Telefone já cadastrado",
                    "null": "Telefone é obrigatório",
                }
            },
            "days_week": {
                "error_messages": {
                    "blank": "Dia da semana é obrigatório",
                    "unique": "Dia da semana já cadastrado",
                    "null": "Dia da semana é obrigatório",
                }
            },
            "hours_days": {
                "error_messages": {
                    "blank": "Hora é obrigatório",
                    "unique": "Hora já cadastrado",
                    "null": "Hora é obrigatório",
                }
            },
        }

    def get_nome_day(self, obj):
        return obj.days_week.name

    def get_nome_hora(self, obj):
        return obj.hours_days.hours


class SchedulerPresbyterySerializer(SchedulerSerializer):
    class Meta:
        model = SchedulerPresbytery
        exclude = ["id", "created", "modified"]
        extra_kwargs = {
            "name": {
                "error_messages": {
                    "blank": "Nome é obrigatório",
                    "unique": "Nome já cadastrado",
                    "null": "Nome é obrigatório",
                }
            },
            "email": {
                "error_messages": {
                    "blank": "Email é obrigatório",
                    "unique": "Email já cadastrado",
                    "null": "Email é obrigatório",
                }
            },
            "cellphone": {
                "error_messages": {
                    "blank": "Telefone é obrigatório",
                    "unique": "Telefone já cadastrado",
                    "null": "Telefone é obrigatório",
                }
            },
            "days_week": {
                "error_messages": {
                    "blank": "Dia da semana é obrigatório",
                    "unique": "Dia da semana já cadastrado",
                    "null": "Dia da semana é obrigatório",
                }
            },
            "hours_days": {
                "error_messages": {
                    "blank": "Hora é obrigatório",
                    "unique": "Hora já cadastrado",
                    "null": "Hora é obrigatório",
                }
            },
        }
