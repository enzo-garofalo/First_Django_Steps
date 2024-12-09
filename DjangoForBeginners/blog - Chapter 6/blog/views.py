from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    UpdateView,
    DeleteView
    )
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

# O Django sabe qual post detalhar porque a URL passa o pk como parâmetro,
# e a DetailView utiliza isso para buscar o objeto correspondente 
# no banco de dados. 
# É uma integração elegante entre URLs, views e templates!
class BlogDetailView(DetailView):
    model = Post
    print(model)
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

"""
    reverse_lazy: É uma função que resolve URLs de forma preguiçosa 
    (ou seja, só no momento em que for realmente necessária).
    Isso é útil porque, quando o código é carregado, 
    algumas dependências ainda podem não estar disponíveis (como a definição da URL chamada 'home'), 
    especialmente em casos de CBVs.
    'home': É o nome de uma URL definida no seu arquivo de rotas (urls.py). 
    Essa URL provavelmente aponta para a página inicial do seu site.
"""

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')