from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.register.models import Register


@admin.register(Register)
class RegisterAdmin(ImportExportModelAdmin):
    search_fields = ["first_name", "last_name", "email"]
    list_display = ["first_name", "last_name", "email"]
