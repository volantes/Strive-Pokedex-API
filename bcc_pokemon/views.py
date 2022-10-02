from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from pokedex.serializers import PokemonSerializer, TypeSerializer
from pokedex.models import Pokemon, Type
from django_filters.rest_framework import DjangoFilterBackend


def index(request):
    return HttpResponse("Welcome to the Strive Backend Coding Challenge index page. Visit /api/ for more fun.")
