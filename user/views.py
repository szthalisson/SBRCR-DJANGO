from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def userLogin(request):
  if request.method != 'POST':
    form = AuthenticationForm()
  else:
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('livros')
    else:
      messages.error(request, 'Nome de usuário ou senha inválidos!')
  
  context = {'form': form}

  return render(request, 'user/login.html', context)

def userLogout(request):
  logout(request)
  return redirect('index')