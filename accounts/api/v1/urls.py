from django.urls import path
from accounts.views import accountsapi
urlpatterns=[
    path('users/',accountsapi,name="accountsapi"),
]