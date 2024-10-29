from django.urls import path
from .views import ServicoListView, ServicoDetailView, ServicoCreateView, ServicoUpdateView, ServicoDeleteView

urlpatterns = [
    path('servicos/', ServicoListView.as_view(), name='servico_list'),
    path('servicos/<int:pk>/', ServicoDetailView.as_view(), name='servico_detail'),
    path('servicos/novo/', ServicoCreateView.as_view(), name='servico_create'),
    path('servicos/<int:pk>/editar/', ServicoUpdateView.as_view(), name='servico_update'),
    path('servicos/<int:pk>/excluir/', ServicoDeleteView.as_view(), name='servico_delete'),
]
