from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from . import models, forms


class BrandListView(ListView):
    model = models.Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'

    def get_queryset(self): #Sobreescrevendo e Filtrando uma Brand pelo nome
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        print("VALOR NAME", name)

        if name:
            queryset = queryset.filter(name__icontains=name)
        print("Queryset:", queryset)
        return queryset

class BrandCreateView(CreateView):
    model = models.Brand
    template_name = 'brand_create.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brand_list')

class BrandDetailView(DetailView):
    model = models.Brand
    template_name = 'brand_detail.html'

class BrandUpdateView(UpdateView):
    model = models.Brand
    template_name = 'brand_update.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brand_list')
