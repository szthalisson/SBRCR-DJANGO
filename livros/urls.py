from django.urls import path
from . import views

urlpatterns = [
  path('', views.livros, name='livros'),
  path('cadastro/', views.cadastroLivro, name="cadastro"),
  path('edicao/<id_livro>/', views.edicaoLivro, name='edicao'),
  path('remocao/<id_livro>/', views.remocaoLivro, name='remocao'),
]