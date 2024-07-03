from django.contrib import admin
from .models import Poster,CustomerClub

@admin.register(Poster)
class PosterAdmin(admin.ModelAdmin):
    list_display=['title','is_active']
    list_filter=["created_date"]
@admin.register(CustomerClub)
class CustomerClubAdmin(admin.ModelAdmin):
    pass