from urllib import request

from django.shortcuts import redirect, render
from django.views.generic import View


class SchedulerView(View):
    def get(self, request):
        return render(request, "scheduler.html")


class SchedulerPresbiteryView(View):
    def get(self, request):
        return redirect("scheduler")


class Main(View):
    def get(self, request):
        return redirect("register_view")


class PDFsVews(View):
    def get(self, request):
        return render(request, "pdf_views.html")
