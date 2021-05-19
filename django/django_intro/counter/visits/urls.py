from django.urls import path
from . import views
import visits

urlpatterns = [
    path('', views.root),
    path('destroy_session',views.clear),
    path('add2',views.add_2),
    path('add_random', views.add_random)
]