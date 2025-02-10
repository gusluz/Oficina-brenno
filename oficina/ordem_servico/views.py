from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import OS, OSProduto
from .forms import OSForm, OSProdutoForm
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
            # Usando o campo codigo da OS diretamente
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
        os = form.save()

        produtos_ids = self.request.POST.getlist("produto[]")
        quantidades = self.request.POST.getlist("quantidade[]")

        for produto_id, quantidade in zip(produtos_ids, quantidades):
            if quantidade and quantidade.isdigit() and produto_id:
                produto = get_object_or_404(Produto, id=produto_id)
                OSProduto.objects.create(
                    ordem_servico=os, produto=produto, quantidade=int(quantidade)
                )

        return redirect(self.success_url)

    def form_invalid(self, form):
        print("Erros no formulário:", form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clientes"] = Cliente.objects.all()
        context["veiculos"] = Veiculo.objects.all()
        context["produtos"] = Produto.objects.all()
        context["produtos_form"] = OSProdutoForm()
        return context


class OSUpdateView(UpdateView):
    model = OS
    form_class = OSForm
    template_name = "os_edit.html"
    success_url = reverse_lazy("os_list")

    def form_valid(self, form):
        os = form.save()

        print("Dados do POST:", self.request.POST)  # Imprime todos os dados do POST

        produtos_ids = self.request.POST.getlist("produto[]")
        quantidades = self.request.POST.getlist("quantidade[]")

        print("IDs dos produtos (antes da limpeza):", produtos_ids)
        print("Quantidades (antes da limpeza):", quantidades)

        # Limpa os produtos existentes
        OSProduto.objects.filter(ordem_servico=os).delete()

        print(
            "Produtos após a limpeza:", OSProduto.objects.filter(ordem_servico=os)
        )  # Lista vazia

        produtos_ids = self.request.POST.getlist(
            "produto[]"
        )  # pega os dados do post novamente, pois o delete apagou os dados.
        quantidades = self.request.POST.getlist("quantidade[]")

        print("IDs dos produtos (depois da limpeza):", produtos_ids)
        print("Quantidades (depois da limpeza):", quantidades)

        for produto_id, quantidade in zip(produtos_ids, quantidades):
            if quantidade and quantidade.isdigit() and produto_id:
                produto = get_object_or_404(Produto, id=produto_id)
                OSProduto.objects.create(
                    ordem_servico=os, produto=produto, quantidade=int(quantidade)
                )

        # Redireciona para a página de sucesso
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        print("Erros no formulário:", form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clientes"] = Cliente.objects.all()
        context["veiculos"] = Veiculo.objects.all()
        context["produtos"] = Produto.objects.all()
        context["produtos_form"] = OSProdutoForm(instance=self.object)
        context["ordem_servico"] = (
            self.get_object()
        )  # Certifique-se que isso retorna a instância correta
        return context


class OSDeleteView(DeleteView):
    model = OS
    template_name = "os_confirm_delete.html"
    success_url = reverse_lazy("os_list")
