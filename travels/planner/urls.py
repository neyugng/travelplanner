from django.urls import path, include

urlpatterns = [
    path('dashboard', views.get_all, name='dashboard'),
]