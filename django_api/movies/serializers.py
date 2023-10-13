from movies.models import Filmwork, Person
from rest_framework import serializers


class FilmworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Filmwork
        fields = ['id', 'title', 'description', 'creation_date', 'rating', 'persons']


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['full_name']
