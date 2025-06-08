from django.urls import path
from . import views

# lista de rotas (URL patterns) para o app de livros
urlpatterns = [
    path('', views.livro_read, name='livro_read'),
    path('create/', views.livro_create, name='livro_create'),
    path('update/<int:pk>/', views.livro_update, name='livro_update'),
    path('delete/<int:pk>/', views.livro_delete, name='livro_delete'),
]