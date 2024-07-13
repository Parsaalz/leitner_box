from django.urls import path
from .views import home_page,get_emails,my_api

urlpatterns=[
    path('',home_page,name="home_page"),
]