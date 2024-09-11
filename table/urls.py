from django.urls import path
from .views import table_form, create_table, table_list, table_detail, table_delete


urlpatterns = [
    path('', table_form, name='table_form'),
    path('create/', create_table, name='create_table'),
    path('list/', table_list, name='table_list'),
#     path('detail/<int:table_id>/', table_detail, name='table_detail'),
    path('delete/<int:id>/', table_delete, name='table_delete'),
]