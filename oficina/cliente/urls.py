from django.urls import path
from .views import ClienteListView, ClienteDetailView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView

urlpatterns = [
    path('', ClienteListView.as_view(), name='cliente_list'),
    path('cliente/<int:pk>/', ClienteDetailView.as_view(), name='cliente_detail'),
    path('cliente/novo/', ClienteCreateView.as_view(), name='cliente_form'),
    path('cliente/<int:pk>/editar/', ClienteUpdateView.as_view(), name='cliente_edit'),
    path('cliente/<int:pk>/excluir/', ClienteDeleteView.as_view(), name='cliente_confirm_delete'),
]
