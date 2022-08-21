from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Campsite
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class TrekListView(ListView):
    template_name = 'pages/trek-list.html'
    model = Campsite


class TrekDetailView(DetailView):
    template_name = 'pages/trek-detail.html'
    model = Campsite


class TrekCreateView(CreateView):
    template_name = 'pages/trek_create.html'
    model = Campsite
    fields = ['title', 'description', 'distance', 'backpacker']


class TrekUpdateView(UpdateView):
    template_name = 'pages/trek-update.html'
    model = Campsite
    fields = ['title', 'description', 'distance', 'backpacker']


class TrekDeleteView(DeleteView):
    template_name = 'pages/trek-delete.html'
    model = Campsite
    success_url = reverse_lazy('pages/list_trek')
