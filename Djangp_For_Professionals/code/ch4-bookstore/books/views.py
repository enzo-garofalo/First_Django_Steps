from django.views import generic
from .models import Books

class BooksListView(generic.TemplateView):
    model = Books
    print(Books.objects.all())
    template_name = 'books/books_list.html'