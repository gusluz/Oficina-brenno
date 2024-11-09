from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import OS
from .forms import OSForm

class OSListView(ListView):
    model = OS
    template_name = 'os_list.html'
    context_object_name = 'ordem_servico'

class OSDetailView(DetailView):
    model = OS
    template_name = 'os_detail.html'
    context_object_name = 'ordem_servico'

class OSCreateView(CreateView):
    model = OS
    form_class = OSForm
    template_name = 'os_form.html'
    success_url = reverse_lazy('os_list')

class OSUpdateView(UpdateView):
    model = OS
    form_class = OSForm
    template_name = 'os_form.html'
    success_url = reverse_lazy('os_list')

class OSDeleteView(DeleteView):
    model = OS
    template_name = 'os_confirm_delete.html'
    success_url = reverse_lazy('os_list')