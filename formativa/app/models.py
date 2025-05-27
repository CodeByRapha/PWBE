from django.db import models # Importa as funcionalidades de modelagem do Django
from django.contrib.auth.models import AbstractUser # Importa a classe base de usuário personalizável do Django

# Modelo de usuário personalizado
class Usuario(AbstractUser):
    # Define as opções de tipo de usuário
    TIPO_CHOICES = [
        ('G', 'Gestor'),
        ('P', 'Professor'),
    ]
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, default='P') # Campo adicional para indicar o tipo do usuário (Gestor ou Professor)
    ni = models.IntegerField(unique=True)  # Número de identificação único
    telefone = models.CharField(max_length=20, blank=True, null=True) # Telefone do usuário
    data_nascimento = models.DateField()  # Data de nascimento do usuário 
    data_contratacao = models.DateField()  # Data de contratação do usuário

    # Define quais campos são obrigatórios além do username e password
    REQUIRED_FIELDS = ['ni', 'data_nascimento', 'data_contratacao']

    # Representação em string do usuário, exibindo nome de usuário e tipo
    def __str__(self):
        return f'{self.username} ({self.get_tipo_display()})'
    
# Modelo para representar uma disciplina
class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    descricao = models.TextField(blank=True, null=True)
    # relacionamento com o professor responsável (apenas usuários do tipo 'Professor' podem ser selecionados)
    professor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'tipo': 'P'}) #null = pode ser nulo blank = nao pode passsar em branco. Limita as escolhas apenas para usuários com tipo 'P'
    
    # Retorna o nome da disciplina 
    def __str__(self):
        return self.nome


# Modelo para representar uma sala
class Sala(models.Model):
    nome = models.CharField(max_length=100)
    capacidade_alunos = models.IntegerField()

    def __str__(self):
        return self.nome # Exibe o nome da sala como representação em string

# Modelo para representar uma reserva de ambiente
class ReservaAmbiente(models.Model):
    # Define os períodos disponíveis para reserva
    PERIODO_CHOICES = [
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('N', 'Noite'),
    ]

    data_inicio = models.DateField()
    data_termino = models.DateField()
    periodo = models.CharField(max_length=1, choices=PERIODO_CHOICES, default='M') # Período do dia em que a reserva é válida
    sala_reservada = models.ForeignKey(Sala, on_delete=models.CASCADE)  # Sala que está sendo reservada
    professor = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'tipo': 'P'})  # Professor que está fazendo a reserva
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    # Representação em string da reserva com nome da sala, período e intervalo de datas
    def __str__(self):
        return f'{self.sala_reservada} - {self.get_periodo_display()} ({self.data_inicio} a {self.data_termino})'
    