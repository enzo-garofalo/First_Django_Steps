from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
     age = models.PositiveBigIntegerField(null=True, blank=True)








"""

AbstractBaseUser vs AbstractUser

AbstractBaseUser requires a very fine level of control and customization. We essentially
rewriteDjango.Thiscanbehelpful,butifwejustwantacustomusermodelthatcanbeupdated
with additional fields, the better choice is AbstractUser which subclasses AbstractBaseUser.
In other words, we write much less code and have less opportunity to mess things up. It’s the
better choice unless you really know what you’re doing with Django!

Note that we use both null and blank with our age field. These two terms are easy to confuse
but quite distinct:
     • null isdatabase-related.Whenafieldhasnull=True itcanstoreadatabaseentryasNULL, meaning no value.
     • blank is validation-related, if blank=True then a form will allow an empty value, whereas if blank=False then a value is required.
In practice, null and blank are commonly used together in this fashion so that a form allows an
empty value and the database stores that value as NULL.

"""