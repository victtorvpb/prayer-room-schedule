from rest_framework import serializers

from apps.scheduler.models import DaysWeek, HoursDays, Scheduler


class DaysWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaysWeek
        fields = ["name", "pk"]


class HoursDayserializer(serializers.ModelSerializer):
    seet = serializers.SerializerMethodField()

    class Meta:
        model = HoursDays
        fields = ["hours", "pk", "seet"]

    def get_seet(self, obj):
        try:
            seet = Scheduler.objects.filter(
                days_week=self.context.get("days_week_id", 0), hours_days=obj
            ).count()
            return 2 - seet
        except:
            return 2


class Schedulererializer(serializers.ModelSerializer):
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
