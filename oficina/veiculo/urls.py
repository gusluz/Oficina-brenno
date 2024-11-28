from django.urls import path
from .views import VeiculoListView, VeiculoDetailView, VeiculoCreateView, VeiculoUpdateView, VeiculoDeleteView

urlpatterns = [
    path('', VeiculoListView.as_view(), name='veiculo_list'),
    path('veiculos/<int:pk>/', VeiculoDetailView.as_view(), name='veiculo_detail'),
    path('veiculos/novo/', VeiculoCreateView.as_view(), name='veiculo_form'),
    path('veiculos/<int:pk>/editar/', VeiculoUpdateView.as_view(), name='veiculo_edit'),
    path('veiculos/<int:pk>/excluir/', VeiculoDeleteView.as_view(), name='veiculo_confirm_delete'),
]
