"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # adicionei as urls para fazer login e signUp
    path('accounts/', include('django.contrib.auth.urls')), 
    path('articles/', include('articles.urls')),
    path('', include('pages.urls'))
]

""" 
Linha: path('accounts/', include('django.contrib.auth.urls'))

O que faz:
Inclui as URLs padrão do sistema de autenticação do Django.
Essas URLs são fornecidas pelo django.contrib.auth e lidam com operações comuns de autenticação, como login, logout, alteração de senha e recuperação de senha.

Linha: path('', TemplateView.as_view(template_name='home.html'), name='home')

O que faz:
Define a URL raiz (/) como uma página que usa o template home.html.
A classe TemplateView exibe um template estático sem necessidade de lógica extra na view.

Por que usar:
Isso é útil para páginas iniciais simples, como uma homepage, onde não há necessidade de manipular dados ou interações complexas.


"""