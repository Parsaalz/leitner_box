from django.contrib import admin
from .models import Articles_page,Category_Articles


@admin.register(Articles_page)
class Articles_Admin(admin.ModelAdmin):
    pass
@admin.register(Category_Articles)
class Category_admin(admin.ModelAdmin):
    pass