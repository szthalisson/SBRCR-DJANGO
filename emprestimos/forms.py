from django import forms
from .models import Emprestimos
from livros.models import Livro

class PesquisaForm(forms.Form):
  pesquisa = forms.CharField(max_length=100, label='', required=False)

class EmprestimoForm(forms.ModelForm):
    # Usando ModelChoiceField para o campo livro
    livro = forms.ModelChoiceField(queryset=Livro.objects.all(), empty_label="Selecione um livro", required=True)

    class Meta:
        model = Emprestimos
        fields = ['livro', 'aluno']

# class EmprestimoForm(forms.ModelForm):
#   livro = autocomplete_light.ChoiceField(
#     required=True,
#     label='',
#     widget=autocomplete_light.widgets.AutocompleteWidget(Livro)
#   )
#     model = Emprestimos
#     fields = ['livro', 'aluno']
#     labels = {'livro': '', 'aluno': ''}
#     # widgets = {
#     #   'aluno': forms.TextInput(attrs={'placeholder': 'Nome do livro', 'class': 'input'}),
#     #   'autor': forms.TextInput(attrs={'placeholder': 'Autor', 'class': 'input'}),
#     #   'quantidade': forms.NumberInput(attrs={'placeholder': 'Quantidade', 'class': 'input'}),
#     # }