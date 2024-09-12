from django.urls import path
from .views import all_slot, create, delete, edit


urlpatterns = [
    path('', all_slot, name='all_slot'),
    path('create/', create, name='create'),
    path('create_slot/', create, name='create_slot'),
    path('delete/<int:id>/', delete, name='delete'),
    path('edit/<int:id>/', edit, name='edit'),
]