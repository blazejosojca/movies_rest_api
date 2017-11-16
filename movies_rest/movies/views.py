from django.shortcuts import render, Http404
from rest_framework.views import Response, APIView
from .models import Movie, Person
from .serializers import MovieSerializer


class ApiMovieDetailView(APIView):

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie,
                                     context={"request": request})
        return Response(serializer.data)

    def delete(self, request, pk):
        pass


class ApiMovieListView(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


