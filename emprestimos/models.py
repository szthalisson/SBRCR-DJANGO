from django.db import models
from livros.models import Livro

# Create your models here.
class Emprestimos(models.Model):
  livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
  aluno = models.TextField(max_length=200)
  criadoEm = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.livro.titulo} | {self.aluno}"