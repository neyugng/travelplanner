from django.urls import path, include
from . import views

urlpatterns = [
    # path('dashboard', views.get_all, name='dashboard'),
    path('', views.index),
    path('myaccount/<int:user_id>', views.edit),
    path('myaccount/<int:user_id>/update', views.update),
    path('dashboard', views.get_all, name='dashboard'),
    path('add_plan', view.add_plan, name='new plan'), 
    path('update_plan/<str:id>', view.update_plan, name='change plan'),
    path('get_plan/<str:id>', view.get_plan, name='get plan'),
]