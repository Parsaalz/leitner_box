from django.contrib import admin
from .models import LitnerApp,Order,PremiumAccount,OrderDetail

@admin.register(LitnerApp)
class LitnerAppAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(PremiumAccount)
class PremiumAccountAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    pass