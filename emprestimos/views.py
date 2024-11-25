from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse, Http404
from .models import Emprestimos, Aluno
from .forms import PesquisaForm, EmprestimoForm, AlunoForm
from django.db.models import Q
from django.utils import timezone
from datetime import datetime, timedelta
from livros.models import Livro
from dal import autocomplete


class LivroAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Certifique-se de que o usuário está autenticado (se necessário)
        if not self.request.user.is_authenticated:
            return Livro.objects.none()  # Sem resultados para usuários não autenticados

        # Obtenha todos os objetos do modelo Livro
        qs = Livro.objects.filter(quantidade__gt=0)

        # Filtrar com base na consulta (q) enviada pelo Select2
        if self.q:
            qs = qs.filter(titulo__icontains=self.q)  # Substitua 'titulo' pelo campo correto do modelo

        return qs

class AlunoAutocomplete(autocomplete.Select2QuerySetView):
   def get_queryset(self):
      if not self.request.user.is_authenticated:
         return Aluno.objects.none()
      
      qs = Aluno.objects.all()

      if self.q:
         qs = qs.filter(nome__icontains=self.q)

      return qs

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
        Q(livro__titulo__icontains=pesquisa) | Q(aluno__nome__icontains=pesquisa)
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
      messages.success(request, 'Novo empréstimo cadastrado com sucesso!')
      return redirect('emprestimos')

  context = {'emprestimos': emps, 'form': form} 

  return render(request, 'emprestimos/cadastro.html', context)

def conclusao_emprestimo(request, id_emprestimo):
  try:
    emprestimo = Emprestimos.objects.get(id=id_emprestimo)
  except Emprestimos.DoesNotExist:
    return redirect('emprestimos')

  if request.method != 'POST':
    form = EmprestimoForm()
  else:
    emprestimo.delete()
    messages.success(request, f"O emprestimo foi concluído com sucesso!")
    return redirect('emprestimos')
  
  context = {'emprestimo': emprestimo, 'form': form}

  return render(request, 'emprestimos/remocao.html', context)

def livro_search(request):
  search_text = request.GET.get('search', '')
  if search_text:
      livros = Livro.objects.filter(titulo__icontains=search_text)
      results = [{'id': livro.id, 'title': livro.titulo} for livro in livros]
      return JsonResponse({'results': results})
  return JsonResponse({'results': []})

def novo_aluno(request):
  if request.method != 'POST':
     form = AlunoForm()
  else:
     form = AlunoForm(request.POST)
     if form.is_valid():
        form.save()
        messages.success(request, f'Aluno cadastrado com sucesso!')
        return redirect('novoEmprestimo')

  context = {'form': form}

  return render(request, 'aluno/cadastro.html', context)