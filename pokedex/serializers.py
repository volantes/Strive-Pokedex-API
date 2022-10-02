from pokedex.models import Pokemon, Type
from rest_framework import serializers


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'type']

class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    types = serializers.SerializerMethodField()
    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'types', 'is_caught', 'hp']
    
    def get_types(self, obj):
        type_names = obj.types.all().values_list('type', flat=True)
        return type_names