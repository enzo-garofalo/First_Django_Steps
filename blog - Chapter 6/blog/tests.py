# The `BlogTests` class contains test methods to ensure the functionality and representation of the
# Post model, as well as testing ListView and DetailView in Django.
# We need to test our model and views now. 
# We want to ensure that the Post model works as
# expected, including its str representation. 
# And we want to test both ListView and DetailView.


# The lines you provided are importing necessary modules and classes for testing Django applications
# using Django's built-in testing framework. Here's what each import statement does:
from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post

# This class likely contains unit tests for a blog application.
class BlogTests(TestCase):

    def setUp(self):
        """
        The `setUp` function creates a test user and a post for testing purposes.
        """
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='Test Title',
            body='Body test content',
            author=self.user,
        )
    
    def test_string_representation(self):
        """
        The function `test_string_representation` tests the string representation of a `Post` object by
        comparing it to the post's title.
        """
        post = Post(title='A simple title')
        self.assertEqual(str(post), post.title)
    
    def test_post_content(self):
        """
        The function `test_post_content` tests the title, author, and body content of a post object.
        """
        self.assertEqual(f'{self.post.title}', 'Test Title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Body test content')
    
    def test_post_list_view(self):
        """
        The `test_post_list_view` function tests the response status code, content, and template used for
        the home page view.
        """
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'Body test content')
        self.assertTemplateUsed(res, 'home.html')

    def test_post_detail_view(self):
        """
        The function `test_post_detail_view` tests the response status code, content, and template used for
        a post detail view in a Django application.
        """
        res = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')

        self.assertEqual(res.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

        self.assertContains(res, 'Test Title')
        self.assertTemplateUsed(res, 'post_detail.html')

