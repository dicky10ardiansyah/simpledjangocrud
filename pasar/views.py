from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import TabelBuah

class IndexBuah(ListView):
    queryset = TabelBuah.objects.all()

class TambahBuah(CreateView):
    model = TabelBuah
    fields = '__all__'
    success_url = reverse_lazy('buah:index')

class UpdateBuah(UpdateView):
    model = TabelBuah
    fields = '__all__'
    success_url = reverse_lazy('buah:index')

class DetailBuah(DetailView):
    model = TabelBuah

class HapusBuah(DeleteView):
    model = TabelBuah
    success_url = reverse_lazy('buah:index')