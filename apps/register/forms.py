from django.forms import DateField, DateInput, ModelForm, SplitDateTimeWidget

from apps.register.models import Register


class DatePickerInput(DateInput):
    input_type = "date"


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = [
            "first_name",
            "last_name",
            "email",
            "zion_member",
            "gender",
            "leader",
            "zion_distance",
            "birth_date",
        ]

        widgets = {"birth_date": DatePickerInput()}

        error_messages = {
            "email": {"unique": "Esse e-mail já estar cadastrado"},
        }
