from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
   path("",views.index,name='home'),
   path("form",views.add,name='form'),
   path("home",views.index,name='home'),
   path("delete/<int:id>",views.delete_stu,name='delete'),
   path("update/<int:id>",views.update_stu,name='update'),
   path("update/do_update/<int:id>",views.do_update,name='do_update')
]
