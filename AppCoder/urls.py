from re import template
from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home),
    path('cursos/', cursos),
    path('entregables/', entregables),
    path('estudiantes/', estudiantes),
    path('profesores/', profesores),
    path('api_estudiantes/', api_estudiantes),
    path('buscar_estudiante/', buscar_estudiante),
    path('create_estudiantes/', create_estudiantes),
    path('read_estudiantes/', read_estudiantes),
    path('delete_estudiantes/<estudiante_id>', delete_estudiantes),
    path('update_estudiantes/<estudiante_id>', update_estudiantes),
    path('login/', login_request),
    path('registro/', registro),
    path('logout/', LogoutView.as_view (template_name = 'home.html'), name="Logout" ),
    path('perfil/', perfilView),
    path('perfil/editarPerfil/', editarPerfil),
    path('perfil/changepass/', changepass),
    path('perfil/changeAvatar/', AgregarAvatar),

]
