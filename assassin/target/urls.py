from django.urls import path
from . import views

app_name = 'target'

urlpatterns = [
    path('list_target/', views.list_target, name="list_target"),
    path('add_target/', views.add_target, name="add_target"),
    path('delete_target/', views.delete_target, name="delete_target"),
]
