from django.urls import path
from . import views

urlpatterns = [
    path('',views.random1),
    path('check',views.check),
    path('try',views.try_again),
]