from rest_framework import serializers
from movies.models import Person, Movie, Role


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ("pk", "first_name", "last_name")


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

