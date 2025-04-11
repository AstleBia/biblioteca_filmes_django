from django.urls import path
from .views import *

urlpatterns = [
    path("", listar_filmes_populares, name="home")
]