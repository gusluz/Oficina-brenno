from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Veiculo
from .forms import VeiculoForm
from cliente.models import Cliente

class VeiculoListView(ListView):
    model = Veiculo
    template_name = 'veiculo_list.html'
    context_object_name = 'veiculos'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(modelo__icontains=search_query)
        return queryset

class VeiculoDetailView(DetailView):
    model = Veiculo
    template_name = 'veiculo_detail.html'
    context_object_name = 'veiculo'

class VeiculoCreateView(CreateView):
    model = Veiculo
    form_class = VeiculoForm
    template_name = 'veiculo_form.html'
    success_url = reverse_lazy('veiculo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona os dados extras para o template
        context['clientes'] = Cliente.objects.all()
        return context

class VeiculoUpdateView(UpdateView):
    model = Veiculo
    form_class = VeiculoForm
    template_name = 'veiculo_edit.html'
    success_url = reverse_lazy('veiculo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona todos os clientes e veículos ao contexto
        context['clientes'] = Cliente.objects.all()
        return context

class VeiculoDeleteView(DeleteView):
    model = Veiculo
    template_name = 'veiculo_confirm_delete.html'
    success_url = reverse_lazy('veiculo_list')
