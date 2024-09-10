from django.urls import path
from .views import create, chips, delete


urlpatterns = [
    path('', create, name='create'),
    path('delete/<int:id>/', delete, name='delete'),
]
