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
    path('dashboard', views.get_all, name='dashboard'),
    path('add_plan', views.add_plan, name='new plan'), 
    path('create_plan', views.create_plan, name='create plan'), 
    path('get_plan/<str:id>', views.get_plan),
    path('add_activity/<int:plan_id>', views.add_activity),
    path('delete_activity/<str:plan_id>/<str:act_id>', views.delete_activity),
    path('delete_plan/<str:id>', views.delete_plan),
]