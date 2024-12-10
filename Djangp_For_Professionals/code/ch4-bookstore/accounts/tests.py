from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from .views import SignUpView

class CustomUserTests(TestCase):
     def test_create_user(self):
          User = get_user_model()
          user = User.objects.create_user(
               username='enzo', email='enzo.garofalo07@gmail.com', password='simworx10'
          )
          self.assertEqual(user.username, "enzo")
          self.assertEqual(user.email, 'enzo.garofalo07@gmail.com')
          self.assertTrue(user.is_active)
          self.assertFalse(user.is_staff)
          self.assertFalse(user.is_superuser)
     
     def test_create_superuser(self):
          User = get_user_model()
          admin_user = User.objects.create_superuser(
               username="superadmin", email="superadmin@email.com", password="testpass123"
          )
          self.assertEqual(admin_user.username, "superadmin")
          self.assertEqual(admin_user.email, "superadmin@email.com")
          self.assertTrue(admin_user.is_active)
          self.assertTrue(admin_user.is_staff)
          self.assertTrue(admin_user.is_superuser)

class SignUpPageTests(TestCase):
     def setUp(self):
          url = reverse('signup')
          self.res = self.client.get(url)
     
     def test_signup_template(self):
          self.assertEqual(self.res.status_code, 200)
          self.assertTemplateUsed(self.res, 'registration/signup.html')
          self.assertContains(self.res, 'Sign Up')
          self.assertNotContains(self.res, 'Hi there! I should not be here!')

     def test_signup_form(self):
          form = self.res.context.get('form')
          self.assertIsInstance(form, CustomUserCreationForm)
          self.assertContains(self.res, 'csrfmiddlewaretoken')
     
     def test_signup_view(self):
          view = resolve('/accounts/signup/')
          self.assertEqual(view.func.__name__, SignUpView.as_view().__name__)
