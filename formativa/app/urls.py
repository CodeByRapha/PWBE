from django.urls import path
from .views import (LoginView, UsuarioListCreate, UsuarioRetrieveUpdateDestroy, 
                    ReservaAmbienteListCreate, ReservaAmbienteRetrieveUpdateDestroy, 
                    ReservaAmbienteProfessorList, DisciplinaListCreate, 
                    DisciplinaRetrieveUpdateDestroy, DisciplinaProfessorList, SalaListCreate, 
                    SalaRetrieveUpdateDestroy)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


#urls
urlpatterns = [
    #Login
    # path('login/', LoginView.as_view()),

    #Usuario
    path('usuario/', UsuarioListCreate.as_view()),
    path('usuario/<int:pk>/', UsuarioRetrieveUpdateDestroy.as_view()),

    #Reserva
    path('reservas/',ReservaAmbienteListCreate.as_view()),
    path('reservas/<int:pk>/', ReservaAmbienteRetrieveUpdateDestroy.as_view()),
    path('professor/reservas/', ReservaAmbienteProfessorList.as_view()),

    #Disciplina
    path('disciplina/', DisciplinaListCreate.as_view()),
    path('disciplina/<int:pk>/', DisciplinaRetrieveUpdateDestroy.as_view()),
    path('professor/disciplinas/', DisciplinaProfessorList.as_view()),

    #Sala
    path('salas/', SalaListCreate.as_view()),
    path('salas/<int:pk>/', SalaRetrieveUpdateDestroy.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]