from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import OS
from .forms import OSForm
from cliente.models import Cliente
from veiculo.models import Veiculo
from produto.models import Produto

class OSListView(ListView):
    model = OS
    template_name = 'os_list.html'
    context_object_name = 'ordem_servico'

class OSDetailView(DetailView):
    model = OS
    template_name = 'os_detail.html'
    context_object_name = 'ordens_servico'

class OSCreateView(CreateView):
    model = OS
    form_class = OSForm
    template_name = 'os_form.html'
    success_url = reverse_lazy('os_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona os dados extras para o template
        context['clientes'] = Cliente.objects.all()
        context['veiculos'] = Veiculo.objects.all()
        context['produtos'] = Produto.objects.all()
        return context

class OSUpdateView(UpdateView):
    model = OS
    form_class = OSForm
    template_name = 'os_edit.html'
    success_url = reverse_lazy('os_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona todos os clientes e veículos ao contexto
        context['clientes'] = Cliente.objects.all() 
        context['veiculos'] = Veiculo.objects.all()  
        context['produtos'] = Produto.objects.all()  # Se necessário
        return context
    


class OSDeleteView(DeleteView):
    model = OS
    template_name = 'os_confirm_delete.html'
    success_url = reverse_lazy('os_list')