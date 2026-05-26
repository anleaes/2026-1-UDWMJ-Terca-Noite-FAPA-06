from django.urls import path
from . import views

app_name = 'animal'

urlpatterns = [
    path('listar/', views.list_products, name='list_animal'),
    path('adicionar/', views.add_product, name='add_animal'),
    path('editar/<int:id_product>/', views.edit_product, name='edit_animal'),
    path('excluir/<int:id_product>/', views.delete_product, name='delete_animal'),
]
