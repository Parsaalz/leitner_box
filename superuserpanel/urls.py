from django.urls import path
from .views import panel_page
from .views import allusers,groups,groups_remove,groups_detail,groups_login
urlpatterns=[
    path('',panel_page,name="panel_page"),
    path('allusers/',allusers,name="allusers"),
    path('groups/',groups,name="groups"),
    path('groups/remove/<int:group_id>/',groups_remove,name="group_remove"),
    path('groups/detail/<int:group_id>/',groups_detail,name="groups_detail"),
    path('groups/login/<int:user_id>/',groups_login,name="groups_login")
]