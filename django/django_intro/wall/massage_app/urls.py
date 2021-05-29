from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.login),
    path('welcome', views.welcome),
    path('logout', views.logout),
    path('create_massage', views.create_massage),
    path('create_comment', views.create_comment),
    path('delete_massage',views.delete_massage),
    path('delete_comment',views.delete_comment),

]