from django.urls import path
from .views import slot_pit



urlpatterns = [
    path('', slot_pit, name='slot_pit'),
]