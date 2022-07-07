from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count

from apps.scheduler.serializer import DaysWeekSerializer, HoursDayserializer, Schedulererializer
from apps.scheduler.models import DaysWeek, HoursDays, Scheduler


class DaysWeekList(APIView):
    def get(self, request, format=None):
        days_week = DaysWeek.objects.all()
        serializer = DaysWeekSerializer(days_week, many=True)
        return Response(serializer.data)


class HoursDaysApi(APIView):
    def get_object(self, days_week_id):
        hours_ids = (
            Scheduler.objects.values("hours_days")
            .annotate(hours_count=Count("hours_days"))
            .filter(hours_count__gte=2, days_week=days_week_id)
            .values_list("hours_days", flat=True)
        )

        return HoursDays.objects.exclude(pk__in=list(hours_ids))

    def get(self, request, days_week_id):
        hours_days = self.get_object(days_week_id)
        serializer = HoursDayserializer(hours_days, many=True)
        return Response(serializer.data)


class SchedulerApi(APIView):
    def post(self, request):
        serializer = Schedulererializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except:
                return Response(
                    {"error": ["NÃO É POSSIVEL FAZER MAIS AGENDAMENTO PARA ESTA HORA"]},
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
