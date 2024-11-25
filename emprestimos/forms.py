from django import forms
from .models import Emprestimos, Aluno
from livros.models import Livro
from dal import autocomplete

class PesquisaForm(forms.Form):
  pesquisa = forms.CharField(max_length=100, label='', required=False)

class EmprestimoForm(forms.ModelForm):
  livro = forms.ModelChoiceField(
    queryset=Livro.objects.filter(quantidade__gt=0),
    empty_label='Selecione um livro',
    widget=autocomplete.ModelSelect2(url='livro-autocomplete')
  )
  aluno = forms.ModelChoiceField(
    queryset=Aluno.objects.all(),
    empty_label='Selecione um aluno',
    widget=autocomplete.ModelSelect2(url='aluno-autocomplete')
  )
  class Meta:
    model = Emprestimos
    fields = ['livro', 'aluno']

class AlunoForm(forms.ModelForm):
  TURMAS = [
    ('', 'Selecione uma turma'),
    ('1° Administração', '1° Administração'),
    ('2° Administração', '2° Administração'),
    ('3° Administração', '3° Administração'),
    ('1° Automação Industrial', '1° Automação Industrial'),
    ('2° Automação Industrial', '2° Automação Industrial'),
    ('3° Automação Industrial', '3° Automação Industrial'),
    ('1° Eletromecânica', '1° Eletromecânica'),
    ('2° Eletromecânica', '2° Eletromecânica'),
    ('3° Eletromecânica', '3° Eletromecânica'),
    ('1° Informática', '1° Informática'),
    ('2° Informática', '2° Informática'),
    ('3° Informática', '3° Informática'),
   ]

  turma = forms.ChoiceField(
    choices=TURMAS,
    widget=forms.Select(attrs={'class':'input'}),
    required=True,
  )

  class Meta:
    model = Aluno
    fields = ['nome', 'turma', 'telefone']
    widgets = {
    'nome': forms.TextInput(attrs={'placeholder': 'Nome do aluno', 'class': 'input'}),
    'turma': forms.TextInput(attrs={'placeholder': 'Turma', 'class': 'input'}),
    'telefone': forms.TextInput(attrs={'placeholder': 'Telefone', 'class': 'input'}),
    }