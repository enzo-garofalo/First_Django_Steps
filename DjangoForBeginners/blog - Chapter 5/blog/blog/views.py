from django.shortcuts import render
from django.views.generic import ListView, DetailView
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
