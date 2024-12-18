from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Fornecedor
from .forms import FornecedorForm


class FornecedorListView(ListView):
    model = Fornecedor
    template_name = 'fornecedor_list.html'
    context_object_name = 'fornecedores'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(nome__icontains=search_query)
        return queryset

class FornecedorDetailView(DetailView):
    model = Fornecedor
    template_name = 'fornecedor_detail.html'
    context_object_name = 'fornecedor'

class FornecedorCreateView(CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'fornecedor_form.html'
    success_url = reverse_lazy('fornecedor_list')

class FornecedorUpdateView(UpdateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'fornecedor_edit.html'
    success_url = reverse_lazy('fornecedor_list')

class FornecedorDeleteView(DeleteView):
    model = Fornecedor
    template_name = 'fornecedor_confirm_delete.html'
    success_url = reverse_lazy('fornecedor_list')
