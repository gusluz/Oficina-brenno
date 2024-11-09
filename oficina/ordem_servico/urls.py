from django.urls import path
from .views import OSListView, OSDetailView, OSCreateView, OSUpdateView, OSDeleteView

urlpatterns = [
    path('ordem_servico/', OSListView.as_view(), name='os_list'),
    path('ordem_servico/<int:pk>/', OSDetailView.as_view(), name='os_detail'),
    path('ordem_servico/novo/', OSCreateView.as_view(), name='os_create'),
    path('ordem_servico/<int:pk>/editar/', OSUpdateView.as_view(), name='os_update'),
    path('ordem_servico/<int:pk>/excluir/', OSDeleteView.as_view(), name='os_delete'),
]
