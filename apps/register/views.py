from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import CreateView, FormView

from apps.register.forms import RegisterForm


class RevisterFormView(CreateView):
    form_class = RegisterForm

    template_name = "register.html"
    success_url = reverse_lazy("register_sucess_view")

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class RegisterSucessView(View):
    def get(self, request):
        return render(
            request, "register_sucess.html", context={"message": "Cadastro realizado com Sucesso"}
        )
