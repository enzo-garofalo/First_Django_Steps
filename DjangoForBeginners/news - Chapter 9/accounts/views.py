from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

# Essa classe foi feita para criar novos user
# Ela herda da classe CreateView
class SignUpView(CreateView):
    # Definimos o forms a ser usado por essa classe
    form_class = CustomUserCreationForm
    # Aqui eu defini para onde o django deve redirecionar se login for bem efetuado
    success_url = reverse_lazy('home')
    # Aqui definimos qual template é usado para essa view
    template_name = 'registration/signup.html'