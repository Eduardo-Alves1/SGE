from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models, forms


class SupplierListView(ListView):
    model = models.Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 10

    def get_queryset(self): #Sobreescrevendo e Filtrando uma Brand pelo nome
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        print("VALOR NAME", name)

        if name:
            queryset = queryset.filter(name__icontains=name)
        print("Queryset:", queryset)
        return queryset

class SupplierCreateView(CreateView):
    model = models.Supplier
    template_name = 'supplier_create.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('supplier_list')

class SupplierDetailView(DetailView):
    model = models.Supplier
    template_name = 'supplier_detail.html'

class SupplierUpdateView(UpdateView):
    model = models.Supplier
    template_name = 'supplier_update.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('supplier_list')

class SupplierDeleteView(DeleteView):
    model = models.Supplier
    template_name = 'supplier_delete.html'
    success_url = reverse_lazy('supplier_list')