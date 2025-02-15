from django.urls import path
from .views import OSListView, OSDetailView, OSCreateView, OSUpdateView, OSDeleteView, OSCompleteView

urlpatterns = [
    path('', OSListView.as_view(), name='os_list'),
    path('ordem_servico/<int:pk>/', OSDetailView.as_view(), name='os_detail'),
    path('ordem_servico/novo/', OSCreateView.as_view(), name='os_form'),
    path('ordem_servico/<int:pk>/editar/', OSUpdateView.as_view(), name='os_edit'),
    path('ordem_servico/<int:pk>/excluir/', OSDeleteView.as_view(), name='os_confirm_delete'),
    path('complete/<int:pk>/', OSCompleteView.as_view(), name='os_complete'),
    
]
