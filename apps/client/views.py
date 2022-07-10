from django.shortcuts import redirect, render
from django.views.generic import View


class SchedulerView(View):
    def get(self, request):
        return render(request, "scheduler.html")


class Main(View):
    def get(self, request):
        return redirect("scheduler")
