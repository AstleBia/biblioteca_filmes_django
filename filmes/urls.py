from django.urls import path
from .views import *

urlpatterns = [
    path("", listar_filmes_populares, name="home"),
    path("busca/", buscar_filmes, name="busca_filmes"),
    path('adicionar/<int:filme_id>/', adicionar_filme,name="adicionar_filme"),
    path("meus_filmes/", listar_filmes, name="lista_filmes"),
    path("editar_filme/<int:filme_id>", editar_filme, name = "editar_filme"),
    path("deletar_filme/<int:filme_id>", deletar_filme, name = "deletar_filme")
]