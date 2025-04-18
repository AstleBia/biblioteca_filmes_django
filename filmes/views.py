from django.shortcuts import render,redirect, get_object_or_404
import requests
from .secure import api_key
from .forms import FormFilme
from .models import Filme

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
    filmes_detalhes = [{"titulo":filme["title"], "descricao":filme["overview"],"id": filme["id"]} for filme in filmes]
    filmes_vistos = Filme.objects.all()
    id_filmes_vistos = [filme_visto.filme_id for filme_visto in filmes_vistos]

    return render(request,"home.html", context={"filmes":filmes_detalhes, "id_filmes_vistos": id_filmes_vistos})

def buscar_filmes_api(nome_filme):
    url = f"https://api.themoviedb.org/3/search/movie?query={nome_filme}&include_adult=false&language=pt-BR&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    filmes = data["results"]
    filmes_detalhes = [{"titulo":filme["title"], "descricao":filme["overview"],"id": filme["id"]} for filme in filmes]
    return filmes_detalhes

def buscar_filmes(request):
    nome_filme = request.GET.get('q')
    filmes_vistos = Filme.objects.all()
    id_filmes_vistos = [filme_visto.filme_id for filme_visto in filmes_vistos]
    return render(request, "busca_filmes.html", context={"filmes":buscar_filmes_api(nome_filme),"id_filmes_vistos":id_filmes_vistos})

def buscar_filme_id(filme_id):
    url = f"https://api.themoviedb.org/3/movie/{filme_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(url, headers=headers)
    filme = response.json()
    filme_detalhes = {"titulo":filme["original_title"]}
    return filme_detalhes

def adicionar_filme(request, filme_id):
    titulo = buscar_filme_id(filme_id)
    if request.method == 'POST':
        form = FormFilme(request.POST)
        if form.is_valid():
            filme = form.save(commit=False)
            filme.filme_id = filme_id
            filme.visto = True
            form.save()
            return redirect("lista_filmes")
    else:
        form = FormFilme(initial={'titulo':titulo["titulo"]})

    return render(request,'adicionar_filme.html',context={"form":form})

def listar_filmes(request):
    filmes = Filme.objects.all()
    return render(request, "lista_filmes.html", context = {"filmes":filmes})