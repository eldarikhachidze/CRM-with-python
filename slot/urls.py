from django.urls import path
from .views import all_slot, create, delete, edit, create_pit, edit_pit, delete_pit, add_slot_to_pit


urlpatterns = [
    path('', all_slot, name='all_slot'),
    path('create/', create, name='create'),
    path('create_slot/', create, name='create_slot'),
    path('delete/<int:id>/', delete, name='delete'),
    path('edit/<int:id>/', edit, name='edit'),
    path('create_pit/', create_pit, name='create_pit'),
    path('edit_pit/<int:id>/', edit_pit, name='edit_pit'),
    path('delete_pit/<int:id>/', delete_pit, name='delete_pit'),
    path('add_slot_to_pit/', add_slot_to_pit, name='add_slot_to_pit'),

]