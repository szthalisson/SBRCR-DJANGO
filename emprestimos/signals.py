from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Emprestimos
from livros.models import Livro

@receiver(post_save, sender=Emprestimos)
def diminuir_quantidade_livro(sender, instance, created, **kwargs):
    if created:
        # A quantidade de livros deve diminuir após a criação do empréstimo
        livro = instance.livro
        if livro.quantidade > 0:  # Verifica se há livros disponíveis
            livro.quantidade -= 1
            livro.save()  # Salva o livro com a nova quantidade

@receiver(post_delete, sender=Emprestimos)
def aumentar_quantidade_livro(sender, instance, **kwargs):
    # A quantidade de livros deve aumentar após a exclusão do empréstimo
    livro = instance.livro
    livro.quantidade += 1
    livro.save()  # Salva o livro com a quantidade atualizada