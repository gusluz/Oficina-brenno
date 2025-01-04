from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import OS
from .forms import OSForm
from cliente.models import Cliente
from veiculo.models import Veiculo
from produto.models import Produto


class OSListView(ListView):
    model = OS
    template_name = "os_list.html"
    context_object_name = "ordem_servico"

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("search", "")
        if search_query:
            # Usando o campo cliente_nome diretamente
            queryset = queryset.filter(codigo__icontains=search_query)
        return queryset


class OSDetailView(DetailView):
    model = OS
    template_name = "os_detail.html"
    context_object_name = "ordem_servico"


class OSCreateView(CreateView):
    model = OS
    form_class = OSForm
    template_name = "os_form.html"
    success_url = reverse_lazy("os_list")

    def form_valid(self, form):
        os = form.save(commit=False)
        os.save()
        form.save_m2m()  # Para salvar os ManyToManyFields
        print("Produto atualizado com sucesso: ", os)
        return redirect(self.success_url)

    def form_invalid(self, form):
        print("Erros no formulário: ", form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona os dados extras para o template
        context["clientes"] = Cliente.objects.all()
        context["veiculos"] = Veiculo.objects.all()
        context["produtos"] = Produto.objects.all()
        return context


class OSUpdateView(UpdateView):
    model = OS
    form_class = OSForm
    template_name = "os_edit.html"
    success_url = reverse_lazy("os_list")

    def form_valid(self, form):
        os = form.save(commit=False)
        os.save()
        form.save_m2m()  # Para salvar os ManyToManyFields
        print("\nOrdem de serviço atualizada com sucesso: ", os)
        return redirect(self.success_url)

    def form_invalid(self, form):
        print("\nErros no formulário: ", form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clientes"] = Cliente.objects.all()
        context["veiculos"] = Veiculo.objects.all()
        context["produtos"] = Produto.objects.all()
        context["ordem_servico"] = self.get_object()
        return context


class OSDeleteView(DeleteView):
    model = OS
    template_name = "os_confirm_delete.html"
    success_url = reverse_lazy("os_list")
