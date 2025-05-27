from rest_framework.permissions import BasePermission # importa a classe base para criação de permissões personalizadas no Django rest framework

# permissão personalizada que permite acesso apenas a usuários com tipo "Gestor"
class IsGestor(BasePermission):
    message = "Este recurso só é acessível por um Gestor"  # Mensagem retornada caso a permissão seja negada
    def has_permission(self, request, view):  # Método que verifica se o usuário tem permissão para acessar a view
        return request.user.is_authenticated and request.user.tipo == 'G' # retorna true se o usuário estiver autenticado e for do tipo 'G' (Gestor)

# Permissão personalizada que permite acesso apenas a usuários com tipo "Professor"
class IsProfessor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.tipo == 'P'
    
# oermissão personalizada que permite acesso se o usuário for Gestor ou o "dono"   
class IsDonoOuGestor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.tipo == 'G':
            return True
        return obj.professor == request.user
        