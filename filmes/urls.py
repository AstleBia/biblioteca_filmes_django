from django.urls import path
from .views import *

urlpatterns = [
    path("", listar_filmes_populares, name="home"),
    path("busca/", buscar_filmes, name="busca_filmes")
]