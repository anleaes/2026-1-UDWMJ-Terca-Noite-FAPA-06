from django.urls import path
from . import views

app_name = 'especies'

urlpatterns = [
    path('adicionar/', views.add_especie, name='add_especie'),
    path('listar/', views.list_especies, name='list_especies'),
    path('editar/<int:id_especie>/', views.edit_especie, name='edit_especie'),
    path('excluir/<int:id_especie>/', views.delete_especie, name='delete_especie'),
]
