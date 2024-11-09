from django.urls import path
from .views import VeiculoListView, VeiculoDetailView, VeiculoCreateView, VeiculoUpdateView, VeiculoDeleteView

urlpatterns = [
    path('veiculos/', VeiculoListView.as_view(), name='veiculo_list'),
    path('veiculos/<int:pk>/', VeiculoDetailView.as_view(), name='veiculo_detail'),
    path('veiculos/novo/', VeiculoCreateView.as_view(), name='veiculo_create'),
    path('veiculos/<int:pk>/editar/', VeiculoUpdateView.as_view(), name='veiculo_update'),
    path('veiculos/<int:pk>/excluir/', VeiculoDeleteView.as_view(), name='veiculo_delete'),
]
