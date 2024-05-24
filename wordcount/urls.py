from django.urls import path
from .views import countword
urlpatterns=[
    path('',countword,name="countword")
]