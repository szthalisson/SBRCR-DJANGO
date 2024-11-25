from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('biblioteca.urls')),
    path('livros/', include('livros.urls')),
    path('emprestimos/', include('emprestimos.urls')),
    path('user/', include('user.urls')),
]
