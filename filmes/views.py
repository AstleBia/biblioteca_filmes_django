from django.shortcuts import render
import requests,secure

# Create your views here.
def listar_filmes_populares(request):
    url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {secure.api_key}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    filmes = data["results"]
    filmes_detalhes = [{"titulo":filme["original_title"], "descricao":filme["overview"]} for filme in filmes]

    return render(request,"home.html", context={"filmes":filmes_detalhes})