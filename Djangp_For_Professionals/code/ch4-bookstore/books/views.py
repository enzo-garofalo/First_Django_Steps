from django.views import generic
from django.db.models import Q
from .models import Books

# Para listar objetos devemos usar List View!
class BooksListView(generic.ListView):
    model = Books
    context_object_name = "books_list"
    template_name = 'books/books_list.html'

class BookDetailView(generic.DetailView):
    model = Books
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

class SearchResultView(generic.ListView):
    model = Books
    context_object_name = 'books_list'
    template_name = 'books/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Books.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context