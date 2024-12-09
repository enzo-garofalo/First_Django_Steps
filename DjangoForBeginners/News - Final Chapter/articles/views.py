from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin 
    )

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .forms import ArticleForm
from .models import Article



class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = Article
    # o form_class permite personalizar os campos
    form_class = ArticleForm
    template_name = 'article_edit.html'
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_new.html'

    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)


