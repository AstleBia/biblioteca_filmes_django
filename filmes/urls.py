from django.urls import path
from .views import *

urlpatterns = [
    path("", listar_filmes_populares, name="home"),
    path("busca/", buscar_filmes, name="busca_filmes"),
    path('adicionar/<str:titulo>/', adicionar_filme,name="adicionar_filme"),
    path("meus_filmes/", listar_filmes, name="lista_filmes"),
]