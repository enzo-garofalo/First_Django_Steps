from django.db import models
from django.contrib.auth.models import User  # Importa o modelo User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE 
    )
    body = models.TextField()

    def __str__(self):
        return self.title
    
    """
     O método `get_absolute_url` é uma prática recomendada no Django para definir uma URL
     canônica para cada instância de um modelo. Ele retorna o caminho absoluto (URL) que 
     aponta para um objeto específico, permitindo que outras partes do código (ou mesmo 
     o navegador do usuário) saibam para onde redirecionar após uma ação bem-sucedida 
     como a criação ou edição de um objeto.
    """
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
    
    """ 
    Por que usar `get_absolute_url`?
    1. Flexibilidade: Mesmo que a estrutura das URLs do projeto mude no futuro, 
       o `get_absolute_url` garante que os links para objetos permaneçam consistentes.
    2. Boas práticas: Facilita a navegação e mantém o código mais organizado e reutilizável.
    3. Integração: Muitos componentes do Django, como templates e CBVs (Class-Based Views), 
       esperam que este método esteja presente para gerar URLs automaticamente.
    """
    
