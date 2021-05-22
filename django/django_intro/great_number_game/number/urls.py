from django.urls import path
from . import views

urlpatterns = [
    path('',views.random),
    path('check',views.check),
    path('try',views.try_again),
]