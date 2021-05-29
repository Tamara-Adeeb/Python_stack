from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.login),
    path('welcome', views.welcome),
    path('logout', views.logout),
    path('add_fav_book', views.add_fav_book),
    path('fav_book/<int:id>/<int:uid>', views.fav_book),
    path('books/<int:id>', views.display_book),
    path('update/<int:id>', views.update_book),
    path('delete/<int:id>', views.delete_book),
    path('un_favorit/<int:id>/<int:uid>', views.un_favorit_book)
]