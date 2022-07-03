from django.shortcuts import render
from django.views.generic import View


class SchedulerView(View):
    def get(self, request):
        return render(request, "scheduler.html")
