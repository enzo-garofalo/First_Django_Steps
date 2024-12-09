from django import forms 
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the content', 'rows': 5}),
        }

# class ArticleCreateForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = ['title', 'body', 'author']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
#             'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the content', 'rows': 5}),
#             'author': forms.Select(attrs={'class': 'form-control'})
#         }
    
    