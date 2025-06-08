from django import forms
from .models import Livro

# cria um formulário baseado no modelo Livro
class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'