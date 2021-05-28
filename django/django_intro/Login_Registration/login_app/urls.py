from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.login),
    path('welcome', views.welcome),
    path('logout', views.logout),

]