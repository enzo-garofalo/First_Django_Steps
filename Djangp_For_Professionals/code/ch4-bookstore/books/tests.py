from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Books, Review
# Create your tests here.

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user( # new
            username="reviewuser",
            email="reviewuser@email.com",
            password="testpass123",
        )
        cls.book = Books.objects.create(
            title = 'Harry Potter',
            author = 'JK Rowling',
            price = '25.00'
        )

        cls.review = Review.objects.create( # new
            book=cls.book,
            author=cls.user,
            review="An excellent review",
        )
    
    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Harry Potter')
        self.assertEqual(f'{self.book.author}', 'JK Rowling')
        self.assertEqual(f'{self.book.price}', '25.00')
    
    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "books/book_detail.html")
    
    def test_book_list_view(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "books/books_list.html")
    
    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Harry Potter")
        self.assertContains(response, "An excellent review") # new
        self.assertTemplateUsed(response, "books/book_detail.html")