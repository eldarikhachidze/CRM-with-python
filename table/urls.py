from django.urls import path
from .views import table_form, create_table, table_list


urlpatterns = [
    path('', table_form, name='table_form'),
    path('create/', create_table, name='create_table'),
    path('list/', table_list, name='table_list'),

]