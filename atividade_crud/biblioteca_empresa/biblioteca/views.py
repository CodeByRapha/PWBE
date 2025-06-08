from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm

# Lista todos os livros e permite filtrar via POST
def livro_read(request):
    if request.method == 'POST':
        livro = livro_filter(request)  # aplica filtro (busca por título, autor ou ano)
    else:
        livro = []
    livros = Livro.objects.all()  # lista completa de livros
    return render(request, 'livro_read.html', {'livros' : livros, 'livro' : livro})

# Cria um novo livro
def livro_create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST) # pega dados enviados do formulário
        if form.is_valid():
            form.save() # salva o livro no banco
            return redirect('livro_read') # volta para a lista de livros
    else:
        form = LivroForm() # formulário vazio para preencher
    return render(request, 'livro_form.html', {'form' : form})

# Atualiza um livro existente (pelo ID)
def livro_update(request, pk):
    livro = get_object_or_404(Livro, pk=pk) # busca o livro ou dá erro 404
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('livro_read')
    else:
        form = LivroForm(instance=livro) # formulário preenchido com os dados atuais
    return render(request, 'livro_form.html', {'form' : form})

# Deleta um livro (pelo ID), após confirmação
def livro_delete(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete() # deleta o livro do banco
        return redirect('livro_read')
    return render(request, 'confirmar_delete.html', {'livro' : livro})

# Função auxiliar para filtrar livros por título, autor ou ano
def livro_filter(request):
    filtro = request.POST.get('livro_filtro') # pega valor digitado pelo usuário
    print(filtro) # mostra no terminal (útil para debug)
    # faz busca no banco usando OR (título, autor OU ano)
    livro = Livro.objects.filter(titulo__icontains = filtro) | Livro.objects.filter(autores__icontains = filtro) | Livro.objects.filter(ano__icontains = filtro)
    return livro