from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('here', views.test),
    path('/<color>', views.name)
]