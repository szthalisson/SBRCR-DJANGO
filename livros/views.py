from django.shortcuts import render, redirect
from .models import Livro
from .forms import PesquisaForm, LivroForm
from django.db.models import Q
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def livros(request):
  livros = Livro.objects.all()

  if request.method != 'POST':
    form = PesquisaForm()
  else:
    form = PesquisaForm(request.POST)
    if form.is_valid():
      livro = form.cleaned_data['pesquisa']
      livros = Livro.objects.filter(
        Q(titulo__icontains=livro) | Q(autor__icontains=livro)
      )

  context = {'livros': livros, 'form': form}
  return render(request, 'html/livros/index.html', context)

@login_required
def cadastroLivro(request):
  if request.method != 'POST':
    form = LivroForm()
  else:
    form = LivroForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, f"Livro {form.cleaned_data['titulo']} cadastrado com sucesso!")
      return redirect('livros')

  context = {'form': form}

  return render(request, 'html/livros/cadastro.html', context)

@login_required
def edicaoLivro(request, id_livro):
  try:
    livro = Livro.objects.get(id=id_livro)
  except Livro.DoesNotExist:
    return redirect('livros')

  if request.method != 'POST':
    form = LivroForm(instance=livro)
  else:
    form = LivroForm(request.POST, instance=livro)
    if form.is_valid():
      form.save()
      return redirect('livros')
    
  context = {'form': form, 'livro': livro}

  return render(request, 'html/livros/edicao.html', context)

@login_required
def remocaoLivro(request, id_livro):
  try:
    livro = Livro.objects.get(id=id_livro)
  except Livro.DoesNotExist:
    return redirect('livros')

  if request.method != 'POST':
    form = LivroForm()
  else:
    livro.delete()
    messages.error(request, f"O livro {livro.titulo} foi removido com sucesso!")
    return redirect('livros')
  
  context = {'livro': livro, 'form': form}

  return render(request, 'html/livros/remocao.html', context)