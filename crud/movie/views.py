
# Create your views here.
from django.views.generic import ListView, CreateView, DeleteView, DetailView

from movie.models import Movie


class MovieListView(ListView):
    model = Movie

class MovieCreateView(CreateView):
    model = Movie
    fields = ['title']
    success_url = '/'


class MovieDeleteView(DeleteView):
    model = Movie
    success_url = '/'


class MovieDetailView(DetailView):
    model = Movie
