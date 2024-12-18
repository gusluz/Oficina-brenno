from django.urls import path
from .views import FornecedorListView, FornecedorDetailView, FornecedorCreateView, FornecedorUpdateView, FornecedorDeleteView

urlpatterns = [
    path('', FornecedorListView.as_view(), name='fornecedor_list'),
    path('fornecedor/<int:pk>/', FornecedorDetailView.as_view(), name='fornecedor_detail'),
    path('fornecedor/novo/', FornecedorCreateView.as_view(), name='fornecedor_form'),
    path('fornecedor/<int:pk>/editar/', FornecedorUpdateView.as_view(), name='fornecedor_edit'),
    path('fornecedor/<int:pk>/excluir/', FornecedorDeleteView.as_view(), name='fornecedor_confirm_delete'),
]
