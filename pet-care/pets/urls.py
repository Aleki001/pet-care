from django.urls import path
from . import views

urlpatterns = [
    path('pets/', views.pets, name='pets'),
    path('add/', views.add_pets, name='add_pets'),
    path('delete-pet/<int:pk>/', views.delete_pet, name='delete_pet'),
    path('adopt/<int:pet_id>/', views.adopt_pet, name='adopt_pet'),
    path('adoption-requests/', views.adoption_requests_list, name='adoption_requests_list'),
]