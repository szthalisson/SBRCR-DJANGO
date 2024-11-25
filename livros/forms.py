from django import forms
from .models import Livro

class PesquisaForm(forms.Form):
  pesquisa = forms.CharField(max_length=100, label='', required=False)

class LivroForm(forms.ModelForm):
  class Meta:
    model = Livro
    fields = ['titulo', 'autor', 'quantidade']
    labels = {'titulo': '', 'autor': '', 'quantidade': ''}
    widgets = {
      'titulo': forms.TextInput(attrs={'placeholder': 'Nome do livro', 'class': 'input'}),
      'autor': forms.TextInput(attrs={'placeholder': 'Autor', 'class': 'input'}),
      'quantidade': forms.NumberInput(attrs={'placeholder': 'Quantidade', 'class': 'input'}),
    }
    