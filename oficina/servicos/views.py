from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Servico
from .forms import ServicoForm

class ServicoListView(ListView):
    model = Servico
    template_name = 'servico_list.html'
    context_object_name = 'servicos'

class ServicoDetailView(DetailView):
    model = Servico
    template_name = 'servico_detail.html'
    context_object_name = 'servico'

class ServicoCreateView(CreateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'servico_form.html'
    success_url = reverse_lazy('servico_list')
    

class ServicoUpdateView(UpdateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'servico_form.html'
    success_url = reverse_lazy('servico_list')

class ServicoDeleteView(DeleteView):
    model = Servico
    template_name = 'servico_confirm_delete.html'
    success_url = reverse_lazy('servico_list')
