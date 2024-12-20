from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    # Página de inicio
    path('index/', views.index, name='index'),

    # Rutas de Ejercicios
    path('ejercicios/', views.ejercicios, name='ejercicios'),
    path('agregar_ejercicio/', views.agregar_ejercicio, name='agregar_ejercicio'),
    path('ejercicio/editar/<int:ejercicio_id>/', views.editar_ejercicio, name='editar_ejercicio'),
    path('ejercicio/eliminar/<int:ejercicio_id>/', views.eliminar_ejercicio, name='eliminar_ejercicio'),

    # Rutas de Rutinas
    path('rutinas/', views.rutinas, name='rutinas'),
    path('agregar_rutina/', views.agregar_rutina, name='agregar_rutina'),
    path('rutina/editar/<int:rutina_id>/', views.editar_rutina, name='editar_rutina'),
    path('rutina/eliminar/<int:rutina_id>/', views.eliminar_rutina, name='eliminar_rutina'),

    # Rutas de Usuarios
    path('usuarios/', views.usuarios, name='usuarios'),
    path('agregar_usuario/', views.agregar_usuario, name='agregar_usuario'),
    path('eliminar_usuario/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('usuarios/editar/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),

    # Rutas de login/logout
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
