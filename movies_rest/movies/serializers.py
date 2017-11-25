from rest_framework import serializers
from movies.models import Movie
from persons.serializers import PersonSerializer


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    actors = PersonSerializer(many=True)
    director = PersonSerializer('director')

    class Meta:
        model = Movie
        fields = ('pk',
                  'title',
                  'description',
                  'director',
                  'actors',
                  'year',
                  'ranking',
                  'genre')

