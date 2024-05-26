from django.urls import path 
from . import views
urlpatterns=[
    path('',views.litner_page,name="litner_page"),
    path('add/',views.addwords,name="addwords"),
    path('app/',views.litner_app,name="litner_app"),
    path('app/correct/<int:word_id>/',views.correct_ans,name="correct_ans"),
    path('app/wrong/<int:word_id>/',views.wrong_ans,name="wrong_ans"),
]