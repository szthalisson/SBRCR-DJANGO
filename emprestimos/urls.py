from django.urls import path
from . import views

urlpatterns = [
  path('', views.emprestimos, name='emprestimos'),
  path('livro-search/', views.livro_search, name='livro_search'),
  path('novoEmprestimo/', views.novoEmprestimo, name='novoEmprestimo'),
  path('livro-autocomplete/', views.LivroAutocomplete.as_view(), name='livro-autocomplete'),
  path('novo-aluno/', views.novo_aluno, name='novo_aluno'),
  path('aluno-autocomplete/', views.AlunoAutocomplete.as_view(), name='aluno-autocomplete'),
  path('conclusao-emprestimo/<id_emprestimo>', views.conclusao_emprestimo, name='conclusao_emprestimo'),
]