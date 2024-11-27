from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models, forms


class InflowListView(ListView):
    model = models.Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10

    def get_queryset(self): #Sobreescrevendo e Filtrando uma Brand pelo nome
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        print("VALOR NAME", name)

        if name:
            queryset = queryset.filter(name__icontains=name)
        print("Queryset:", queryset)
        return queryset

class InflowCreateView(CreateView):
    model = models.Inflow
    template_name = 'inflow_create.html'
    form_class = forms.InflowForm
    success_url = reverse_lazy('inflow_list')

class InflowDetailView(DetailView):
    model = models.Inflow
    template_name = 'inflow_detail.html'

class InflowUpdateView(UpdateView):
    model = models.Inflow
    template_name = 'inflow_update.html'
    form_class = forms.InflowForm
    success_url = reverse_lazy('inflow_list')

class InflowDeleteView(DeleteView):
    model = models.Inflow
    template_name = 'inflow_delete.html'
    success_url = reverse_lazy('inflow_list')
