from django.shortcuts import render
from django.views.generic import ListView
from .models import Universitet, Malumot

class UniversitetListView(ListView):
    model = Universitet
    template_name = 'universitet_list.html'
    context_object_name = 'universitetlar'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')  # Qidiruv so'rovini olish
        if query:
            queryset = queryset.filter(nomi__icontains=query)  # Qidiruv bo'yicha filter
        return queryset



class MalumotListView(ListView):
    model = Malumot
    template_name = 'malumot_list.html'
    context_object_name = 'malumotlar'


