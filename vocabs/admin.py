from django.contrib import admin
from .models import english_vocabs,category_languages

@admin.register(english_vocabs)
class english_page(admin.ModelAdmin):
    pass
@admin.register(category_languages)
class category_ll(admin.ModelAdmin):
    pass