from django.shortcuts import render
import requests

# Create your views here.
def listar_filmes_populares(request):
    url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzNWZjNTg3YzUyODAwZWRiMDMzMjU4OTgxY2I0OWUxZCIsIm5iZiI6MTc0Mzc2NjgwNS4yMTgsInN1YiI6IjY3ZWZjNTE1OGIxZjMyZWI3OWQ5MjI2ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.95uBxYf8ZtbgGH6ZIkPT0sttZBi-cE_zFeM2uMUm8q0"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    filmes = data["results"]
    filmes_detalhes = [{"titulo":filme["original_title"], "descricao":filme["overview"]} for filme in filmes]

    return render(request,"home.html", context={"filmes":filmes_detalhes})