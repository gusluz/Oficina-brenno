from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Veiculo
from .forms import VeiculoForm
from cliente.models import Cliente


class VeiculoListView(ListView):
    model = Veiculo
    template_name = "veiculo_list.html"
    context_object_name = "veiculos"

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("search", "")
        if search_query:
            queryset = queryset.filter(modelo__icontains=search_query)
        return queryset


class VeiculoDetailView(DetailView):
    model = Veiculo
    template_name = "veiculo_detail.html"
    context_object_name = "veiculo"


class VeiculoCreateView(CreateView):
    model = Veiculo
    form_class = VeiculoForm
    template_name = "veiculo_form.html"
    success_url = reverse_lazy("veiculo_list")

    def form_valid(self, form):
        veiculo = form.save(commit=False)
        veiculo.cliente_nome = form.cleaned_data["cliente_nome"]
        veiculo.save()
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clientes"] = Cliente.objects.all()
        return context


class VeiculoUpdateView(UpdateView):
    model = Veiculo
    form_class = VeiculoForm
    template_name = "veiculo_edit.html"
    success_url = reverse_lazy("veiculo_list")

    # def form_valid(self, form):
    #     veiculo = form.save(commit=False)
    #     veiculo.cliente_nome = form.cleaned_data["cliente_nome"]
    #     veiculo.save()
    #     print("Veiculo atualizado com sucesso: ", veiculo)
    #     return redirect(self.success_url)
    
    # def form_invalid(self, form):
    #     print("Erros no formulário: ", form.errors)
    #     return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clientes"] = Cliente.objects.all()
        return context


class VeiculoDeleteView(DeleteView):
    model = Veiculo
    template_name = "veiculo_confirm_delete.html"
    success_url = reverse_lazy("veiculo_list")
