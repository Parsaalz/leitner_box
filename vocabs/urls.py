from django.urls import path
from . import views
urlpatterns=[
    path('',views.vocabs_page,name="vocabs_page"),
    path('english/<int:category_id>/',views.english_page,name="english_page"),
    path('english/add/',views.add_english,name="add_english"),
    path('english/edit/<int:vocab_id>/',views.edit_english,name="edit_english"),
    path('english/delete/<int:vocab_id>/',views.delete_english,name="delete_english"),
    path('english/category/',views.category_page,name="category_page"),
    path('english/category/add',views.add_category_english,name="add_category_english"),
]