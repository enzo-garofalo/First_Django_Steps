from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView

class HomePageTests(SimpleTestCase):
     def setUp(self):
          url = reverse("home")
          self.res = self.client.get(url)

     def test_url_exists_at_correct_location(self):
          self.assertEqual(self.res.status_code, 200)
     
     def test_homepage_url_name(self):
          res = self.client.get(reverse("home"))
          self.assertEqual(res.status_code, 200)

     def test_homepage_template(self):
          self.assertTemplateUsed(self.res, 'pages/home.html')
     
     def test_homepage_contains_correct_html(self):
        self.assertContains(self.res, 'home page')
     
     def test_homepage_does_not_contain_incorrect_html(self):
          self.assertNotContains(self.res, "Hi there I should not be here.")
     
     def test_homepage_url_resolves_homepageview(self):
          view = resolve("/")
          self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)