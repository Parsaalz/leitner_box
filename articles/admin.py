from django.contrib import admin
from .models import Articles_page


@admin.register(Articles_page)
class Articles_Admin(admin.ModelAdmin):
    pass
