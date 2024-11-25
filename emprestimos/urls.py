from django.urls import path
from . import views

urlpatterns = [
  path('', views.emprestimos, name='emprestimos'),
  path('livro-search/', views.livro_search, name='livro_search'),
  path('novoEmprestimo/', views.novoEmprestimo, name='novoEmprestimo'),
]