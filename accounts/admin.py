from django.contrib import admin
from .models import banusers,Image_Users,Moreinformation


@admin.register(banusers)
class banusers_admin(admin.ModelAdmin):
    pass
@admin.register(Image_Users)
class Image_users_Admin(admin.ModelAdmin):
    pass
@admin.register(Moreinformation)
class more_info_admin(admin.ModelAdmin):
    pass
