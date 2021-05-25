from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.main),
    path('process',views.process),
    path('shows', views.show_table),
    path('shows/new', views.add_show),
    path('shows/<int:id>',views.view),
    path('shows/<int:id>/edit',views.edit),
    path('update',views.update),
    path('delete/<int:id>',views.delete)
]