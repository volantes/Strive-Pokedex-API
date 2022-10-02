from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from pokedex.serializers import PokemonSerializer, TypeSerializer
from pokedex.models import Pokemon, Type
from django_filters.rest_framework import DjangoFilterBackend


def index(request):
    return HttpResponse("Welcome to the Backend Coding Challenge Pokedex app index page.")

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'types', 'is_caught']

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
