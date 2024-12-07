from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Produto
from .forms import ProdutoForm
from fornecedor.models import Fornecedor

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto_list.html'
    context_object_name = 'produtos'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(nome__icontains=search_query)
        return queryset

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto_detail.html'
    context_object_name = 'produto'

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produto_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona os fornecedores ao contexto
        context['fornecedores'] = Fornecedor.objects.all()
        return context

class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto_edit.html'
    success_url = reverse_lazy('produto_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona todos os fornecedores ao contexto
        context['fornecedores'] = Fornecedor.objects.all()
        return context

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto_confirm_delete.html'
    success_url = reverse_lazy('produto_list')


def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, "Produto excluído com sucesso.")
        return redirect('listar_produtos')  # Redireciona para a lista de produtos
    return render(request, 'confirmar_exclusao.html', {'produto': produto})
