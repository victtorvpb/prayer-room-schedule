import pdb
from pdb import Pdb

from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from yaml import serialize

from apps.scheduler.models import (
    DaysWeek,
    DaysWeekPresbytery,
    HoursDays,
    HoursDaysPresbytery,
    Scheduler,
    SchedulerPresbytery,
)
from apps.scheduler.serializer import (
    DaysWeekPresbyterySerializer,
    DaysWeekSerializer,
    HoursDaySerializer,
    HoursDaysPresbytery,
    HoursDaysPresbyterySerializer,
    SchedulerPresbyterySerializer,
    SchedulerSerializer,
)


class DaysWeekList(APIView):
    model_days = DaysWeek
    model_serialize = DaysWeekSerializer

    def get(self, request, format=None):
        days_week = self.model_days.objects.all()
        serializer = self.model_serialize(days_week, many=True)
        return Response(serializer.data)


class DaysWeekPresbyteryList(DaysWeekList):
    model_days = DaysWeekPresbytery
    model_serialize = DaysWeekPresbyterySerializer


class HoursDaysApi(APIView):
    model_scheduler = Scheduler
    model_hours = HoursDays
    model_serialize = HoursDaySerializer

    def get_object(self, days_week_id):

        hours_ids = (
            self.model_scheduler.objects.values("hours_days")
            .annotate(hours_count=Count("hours_days"))
            .filter(hours_count__gte=1, days_week=days_week_id)
            .values_list("hours_days", flat=True)
        )

        result = self.model_hours.objects.exclude(pk__in=list(hours_ids))

        return result

    def get(self, request, days_week_id):
        hours_days = self.get_object(days_week_id)
        serializer = self.model_serialize(hours_days, many=True)
        return Response(serializer.data)


class HoursDaysPresbyteryApi(HoursDaysApi):
    model_scheduler = SchedulerPresbytery
    model_hours = HoursDaysPresbytery
    model_serialize = HoursDaysPresbyterySerializer


class SchedulerApi(APIView):
    model_serialize = SchedulerSerializer

    def post(self, request):
        serializer = self.model_serialize(data=request.data)
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


class SchedulerPresbyteryApi(SchedulerApi):
    model_serialize = SchedulerPresbyterySerializer
