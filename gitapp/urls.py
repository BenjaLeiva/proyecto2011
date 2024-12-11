from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ejercicios/', views.ejercicios, name='ejercicios'),
    path('agregar_ejercicio/', views.agregar_ejercicio, name='agregar_ejercicio'),
    path('rutinas/', views.rutinas, name='rutinas'),
    path('agregar_rutina/', views.agregar_rutina, name='agregar_rutina'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('agregar_usuario/', views.agregar_usuario, name='agregar_usuario'),
]
