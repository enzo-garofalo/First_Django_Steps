from django.contrib.auth import get_user_model
from django.test import TestCase

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
''