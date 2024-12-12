from django.views import generic
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