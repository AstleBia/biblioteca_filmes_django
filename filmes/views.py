from django.shortcuts import render
import requests
from .secure import api_key

# Create your views here.
def listar_filmes_populares(request):
    url = "https://api.themoviedb.org/3/movie/popular?language=pt-BR&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    filmes = data["results"]
    filmes_detalhes = [{"titulo":filme["title"], "descricao":filme["overview"]} for filme in filmes]

    return render(request,"home.html", context={"filmes":filmes_detalhes})

def buscar_filmes_api(nome_filme):
    url = f"https://api.themoviedb.org/3/search/movie?query={nome_filme}&include_adult=false&language=pt-BR&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    filmes = data["results"]
    filmes_detalhes = [{"titulo":filme["title"], "descricao":filme["overview"]} for filme in filmes]
    return filmes_detalhes

def buscar_filmes(request):
    nome_filme = request.GET.get('q')
    return render(request, "busca_filmes.html", context={"filmes":buscar_filmes_api(nome_filme)})