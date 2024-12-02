from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser 

# Essa classe cria o forms para meu user customizado
class CustomUserCreationForm(UserCreationForm):

    # Como eu estou usando AbstractUser como minha base, eu apenas add novos campos
    # Pela classe meta que sobrescreve sob a base dada por AbstractUser
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age',)

# Essa classe define o form criado acima
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields