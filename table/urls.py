from django.urls import path
from .views import table_form, create_table


urlpatterns = [
    path('', table_form, name='table_form'),
    path('create/', create_table, name='create_table'),

]