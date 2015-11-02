from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from movie.models import Movie

@csrf_exempt
def api_movie_list_create(request):
    if request.POST:
        movie = request.POST.get("title")
        Movie.objects.create(movie=movie)
        return HttpResponse(json.dumps({"message": "Success"}), content_type="application/json")
    all_movies = Movie.objects.all()
    data = [{"id": movie.id, "movie": movie.title} for movie in all_movies]
    data = json.dumps(data)
    return HttpResponse(data, content_type="application/json")

def api_movie_detail(request, pk):
    movie = Movie.objects.get(id=pk)
    serialized_movie = json.dumps({"id": movie.id, "movie": movie.title})
    return HttpResponse(serialized_movie, content_type="application/json")
