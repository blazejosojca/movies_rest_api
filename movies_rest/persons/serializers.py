from rest_framework import serializers
from persons.models import Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ("pk", "first_name", "last_name")
