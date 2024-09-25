from django.urls import path
from .views import slot_pit, delete_slot_machine_from_pit



urlpatterns = [
    path('', slot_pit, name='slot_pit'),
    path('delete_slot_machine_from_pit/<int:hall_id>/<int:slot_id>/', delete_slot_machine_from_pit, name='delete_slot_machine_from_pit'),
]