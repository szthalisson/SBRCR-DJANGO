from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Emprestimos
from .forms import PesquisaForm, EmprestimoForm
from django.db.models import Q
from django.utils import timezone
from datetime import datetime, timedelta
from livros.models import Livro

def diferenca_datas(data2):
  try:
    data1 = timezone.now()
    data2 = datetime.strptime(data2, '%Y-%m-%d %H:%M:%S.%f%z')
    diferenca = data2 - data1
    return diferenca.days
  except ValueError:
    pass

def somar_dias_a_data(data, dias):
    data_obj = datetime.strptime(data[:10], '%Y-%m-%d')
    nova_data = data_obj + timedelta(days=dias)
    
    return nova_data

# Create your views here.
def emprestimos(request):
  emps = Emprestimos.objects.all()
  criadosEm = [e.criadoEm for e in emps]
  dataValidade = [somar_dias_a_data(str(data), 15) for data in criadosEm]

  if request.method != 'POST':
    form = PesquisaForm()
  else:
    form = PesquisaForm(request.POST)
    if form.is_valid():
      pesquisa = form.cleaned_data['pesquisa']
      emps = Emprestimos.objects.filter(
        Q(livro__titulo__icontains=pesquisa) | Q(aluno__icontains=pesquisa)
      )

  combinado = zip(emps, dataValidade)

  context = {'emprestimos': emps, 'form': form, 'combinado': combinado}
  
  return render(request, 'emprestimos/index.html', context)

def novoEmprestimo(request):
  emps = Emprestimos.objects.all()
  if request.method != 'POST':
    form = EmprestimoForm()
  else:
    form = EmprestimoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('emprestimos')

  context = {'emprestimos': emps, 'form': form} 

  return render(request, 'emprestimos/cadastro.html', context)

def livro_search(request):
  search_text = request.GET.get('search', '')
  if search_text:
      livros = Livro.objects.filter(titulo__icontains=search_text)
      results = [{'id': livro.id, 'title': livro.titulo} for livro in livros]
      return JsonResponse({'results': results})
  return JsonResponse({'results': []})