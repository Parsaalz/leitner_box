from django.contrib import admin
from .models import LitnerApp

@admin.register(LitnerApp)
class LitnerAppAdmin(admin.ModelAdmin):
    pass
