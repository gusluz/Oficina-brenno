from django.urls import path
from .views import ProdutoListView, ProdutoDetailView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView

urlpatterns = [
    path('produtos/', ProdutoListView.as_view(), name='produto_list'),
    path('produtos/<int:pk>/', ProdutoDetailView.as_view(), name='produto_detail'),
    path('produtos/novo/', ProdutoCreateView.as_view(), name='produto_create'),
    path('produtos/<int:pk>/editar/', ProdutoUpdateView.as_view(), name='produto_update'),
    path('produtos/<int:pk>/excluir/', ProdutoDeleteView.as_view(), name='produto_delete'),
]
