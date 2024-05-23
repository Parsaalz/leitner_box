from django.urls import path
from . import views
urlpatterns=[
    path('dashboard/<int:user_id>/',views.dashboard_page,name="dashboard_page"),
    path('setting/changeinformation/',views.changeinformation,name="changeinformation"),
]
