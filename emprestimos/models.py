from django.db import models
from livros.models import Livro

# Create your models here.
class Aluno(models.Model):
  nome = models.CharField(max_length=200)
  turma = models.CharField(max_length=200)
  telefone = models.CharField(max_length=200)

  def __str__(self):
    return self.nome

class Emprestimos(models.Model):
  livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
  aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
  criadoEm = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.livro.titulo} | {self.aluno}"
