from django.urls import path
from .views import table_form, create_table, table_list, table_delete, table_edit, table_close, close


urlpatterns = [
    path('', table_form, name='table_form'),
    path('create/', create_table, name='create_table'),
    path('list/', table_list, name='table_list'),
    path('edit/<int:id>/', table_edit, name='table_edit'),
    path('delete/<int:id>/', table_delete, name='table_delete'),
    path('close/<int:id>/', table_close, name='table_close'),
    path('close_table/<int:id>/', close, name='close'),
]