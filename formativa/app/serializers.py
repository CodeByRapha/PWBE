from rest_framework import serializers  # Importa classes do Django REST Framework para criação de serializers
from .models import Usuario, Disciplina, ReservaAmbiente, Sala # Importa os modelos do sistema
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer # Importa serializer específico para autenticação com JWT


# Serializer para o modelo Usuario, que transforma objetos Usuario em JSON e vice-versa
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

# Serializer para o modelo Disciplina
class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

# Serializer para o modelo Sala
class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'

# Serializer para o modelo ReservaAmbiente
class ReservaAmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaAmbiente
        fields = '__all__'

# Serializer para o modelo LoginSerializer
class LoginSerializer(TokenObtainPairSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)
    # Chama a validação padrão do JWT, que gera os tokens de acesso e refresh
    def validate(self, attrs):
        data = super().validate(attrs)

         # Adiciona dados personalizados do usuário à resposta do login
        data['user'] = {
            'username': self.user.username,
            'email': self.user.email,
            'tipo': self.user.tipo  # Campo personalizado do modelo Usuario
        }
        return data # Retorna os tokens + dados do usuário

