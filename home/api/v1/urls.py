from django.urls import path
from home.views import my_api,my_api_detail
urlpatterns=[
    path('list/',my_api,name="blog_home_api"),
    path('list/<int:id>/',my_api_detail,name="blog_home_api"),
]