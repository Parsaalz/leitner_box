from django.urls import path
from . import views
urlpatterns=[
    path('login/',views.login_page,name="login_page"),
    path('signup/',views.signup_page,name="signup_page"),
    path('logout/',views.logout_page,name="logout_page"),
    path('forget_password/',views.forget_password,name="forget_password"),
    path('reset_password/<int:user_id>/',views.reset_password,name="reset_password"),
]