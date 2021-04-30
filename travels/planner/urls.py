from django.urls import path, include
from . import views

urlpatterns = [
    # path('dashboard', views.get_all, name='dashboard'),
    path('', views.index),
    path('myaccount/<int:user_id>', views.edit),
    path('myaccount/<int:user_id>/update', views.update),
]