from django.urls import path
from .views import FornecedorListView, FornecedorDetailView, FornecedorCreateView, FornecedorUpdateView, FornecedorDeleteView

urlpatterns = [
    path('fornecedor/', FornecedorListView.as_view(), name='fornecedor_list'),
    path('fornecedor/<int:pk>/', FornecedorDetailView.as_view(), name='fornecedor_detail'),
    path('fornecedor/novo/', FornecedorCreateView.as_view(), name='fornecedor_create'),
    path('fornecedor/<int:pk>/editar/', FornecedorUpdateView.as_view(), name='fornecedor_update'),
    path('fornecedor/<int:pk>/excluir/', FornecedorDeleteView.as_view(), name='fornecedor_delete'),
]
