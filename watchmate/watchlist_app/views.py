from django.shortcuts import render
from .models import Movie
from rest_framework.decorators import api_view
from .serializers import MovieSerializer
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def movie_list(request):
    
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many = True)
        return Response(serializer.data)