from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cliente
from .forms import ClienteForm

class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente_list.html'
    context_object_name = 'clientes'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(nome__icontains=search_query)
        return queryset

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente_detail.html'
    context_object_name = 'cliente'

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_edit.html'
    success_url = reverse_lazy('cliente_list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')
