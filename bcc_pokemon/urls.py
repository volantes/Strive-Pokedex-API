from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from pokedex.views import PokemonViewSet, TypeViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'pokemon', PokemonViewSet)
router.register(r'types', TypeViewSet)

urlpatterns = [
    path('', views.index, name="index"),
    path('pokedex/', include('pokedex.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
