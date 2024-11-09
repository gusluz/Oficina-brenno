from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Veiculo
from .forms import VeiculoForm

class VeiculoListView(ListView):
    model = Veiculo
    template_name = 'veiculo_list.html'
    context_object_name = 'veiculos'

class VeiculoDetailView(DetailView):
    model = Veiculo
    template_name = 'veiculo_detail.html'
    context_object_name = 'veiculo'

class VeiculoCreateView(CreateView):
    model = Veiculo
    form_class = VeiculoForm
    template_name = 'veiculo_form.html'
    success_url = reverse_lazy('veiculo_list')

class VeiculoUpdateView(UpdateView):
    model = Veiculo
    form_class = VeiculoForm
    template_name = 'veiculo_form.html'
    success_url = reverse_lazy('veiculo_list')

class VeiculoDeleteView(DeleteView):
    model = Veiculo
    template_name = 'veiculo_confirm_delete.html'
    success_url = reverse_lazy('veiculo_list')
