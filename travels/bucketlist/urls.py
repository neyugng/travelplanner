from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="bucketlist/index"),
    path('bucketlist-create', views.create_list, name="bucketlist/create"),
    path('add-list', views.add_list, name="bucketlist/add_list"),
    path('create-location/<int:list_id>', views.create_location, name="bucketlist/create_location"),
    path('add-location/<int:list_id>', views.add_location, name="bucketlist/add_location"),
    path('view-list-locations/<int:list_id>', views.view_list_locations, name="bucketlist/view_list_locations"),
    path('delete-list/<int:list_id>', views.delete_list, name="bucketlist/delete"),
    path('delete-location/<int:location_id>', views.delete_location, name="bucketlist/delete_location"),
]