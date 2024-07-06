from django.urls import path
from .views import home_page,get_emails

urlpatterns=[
    path('',home_page,name="home_page"),
]