from django.urls import path 
from . import views
urlpatterns=[
    path('',views.litner_page,name="litner_page"),
    path('add/',views.addwords,name="addwords"),
    path('app/',views.litner_app,name="litner_app"),
    path('app/correct/<int:word_id>/',views.correct_ans,name="correct_ans"),
    path('app/wrong/<int:word_id>/',views.wrong_ans,name="wrong_ans"),
    path('app/account_management/',views.account_management,name="accountmanagement"),
    path('app/account_management/premium/',views.premium_accounts,name="premium_accounts"),
    path('app/account_management/basket/',views.basket,name="basket"),
    path('app/account_management/basket/delete/<int:id>/',views.delete_basket,name="deletebasket"),
]