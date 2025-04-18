
<h1 align="center">🎥 Biblioteca de Filmes 🎥</h1>

### 📍 Sobre o Projeto
Web app de biblioteca de filmes desenvolvido em Django, que permite que o usuário organize os filmes que já assistiu. Ele se integra à api do TMDB para fornecer uma vasta lista de filmes e informações sobre.

No app é possível:
* Pesquisar e ver informações sobre filmes
* Adicionar filmes assistidos à sua biblioteca
* Fazer um review e dar nota aos filmes já assistidos

### 🚀 Tecnologias
* <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
* <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green" />
* <img src="https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
* <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" />

### ⚙️ Instalação
1. Pegue uma key para API em [TMDB](https://developer.themoviedb.org/reference/intro/getting-started)

2. Clone o repositório
```
git clone https://github.com/AstleBia/biblioteca_filmes_django.git
```
3. Crie um arquivo secure.py e cole sua key em:
```
api_key = {sua_key}
```
4. Instale os requirements

` pip install -r requirements.txt `

5. Rode as migrações
```
python manage.py makemigrations
python manage.py migrate
```
6. Rode o projeto
` python manage.py runserver `