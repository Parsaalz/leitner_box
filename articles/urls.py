from django.urls import path
from . import views
urlpatterns=[
    path('',views.articles_page,name="articles_page"),
    path('article/<int:id>/',views.detals_articles,name='detail_page')
]