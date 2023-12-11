from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movies
# Create your views here.


def index(request):
    movies = Movies.objects.all()  # SELECT * FROM movies.movie

    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):

    movie = get_object_or_404(Movies, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
