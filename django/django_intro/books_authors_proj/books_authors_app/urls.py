from django.urls import path
from . import views
urlpatterns = [
    path('',views.book),
    path('book',views.book_data),
    path('books/<int:id>',views.book_show),
    path('many_to_many2', views.select_auth),
    path('authors',views.author),
    path('authors/data',views.author_data),
    path('authors/<int:id>',views.author_show),
    path('many_to_many', views.select_book)

]