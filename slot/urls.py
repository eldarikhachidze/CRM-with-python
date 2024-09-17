from django.urls import path
from .views import all_slot, create, delete, edit, add_to_pit, remove_from_pit


urlpatterns = [
    path('', all_slot, name='all_slot'),
    path('create/', create, name='create'),
    path('create_slot/', create, name='create_slot'),
    path('delete/<int:id>/', delete, name='delete'),
    path('edit/<int:id>/', edit, name='edit'),
    path('add_to_pit/<int:id>/', add_to_pit, name='add_to_pit'),
    path('remove_from_pit/<int:id>/', remove_from_pit, name='remove_from_pit'),
]