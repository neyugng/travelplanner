from django.urls import path, include
from . import views

urlpatterns = [
    # path('dashboard', views.get_all, name='dashboard'),
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('myaccount/<int:user_id>', views.edit),
    path('myaccount/<int:user_id>/update', views.update),
]