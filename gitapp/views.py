from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Ejercicio, Rutina, Usuario
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

# Vista para la página principal (index)
def index(request):
    return render(request, 'gitapp/index.html')

# Vista para agregar ejercicio
@csrf_protect
@login_required  # Solo usuarios autenticados pueden acceder a esta vista
def agregar_ejercicio(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        dificultad = request.POST.get('dificultad')
        # Creación del nuevo ejercicio
        Ejercicio.objects.create(nombre=nombre, descripcion=descripcion, dificultad=dificultad)
        return redirect('ejercicios')  # Redirige a la lista de ejercicios
    return render(request, 'gitapp/agregar_ejercicio.html')

# Vista para listar ejercicios
def ejercicios(request):
    ejercicios = Ejercicio.objects.all()
    return render(request, 'gitapp/ejercicios.html', {'ejercicios': ejercicios})

# Vista para agregar rutina
@csrf_protect
@login_required  # Solo usuarios autenticados pueden acceder a esta vista
def agregar_rutina(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        ejercicios_ids = request.POST.getlist('ejercicios')  # Lista de IDs de ejercicios seleccionados
        duracion = request.POST.get('duracion')
        # Creación de la rutina
        rutina = Rutina.objects.create(nombre=nombre, duracion=duracion)
        rutina.ejercicios.set(ejercicios_ids)  # Asociar ejercicios a la rutina
        return redirect('rutinas')  # Redirige a la lista de rutinas
    ejercicios = Ejercicio.objects.all()  # Obtener todos los ejercicios para la vista de agregar rutina
    return render(request, 'gitapp/agregar_rutina.html', {'ejercicios': ejercicios})

# Vista para listar rutinas
def rutinas(request):
    rutinas = Rutina.objects.all()
    return render(request, 'gitapp/rutinas.html', {'rutinas': rutinas})

# Vista para agregar usuario
@csrf_protect
@login_required  # Solo usuarios autenticados pueden acceder a esta vista
def agregar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        nivel_condicion = request.POST.get('nivel_condicion')
        rutinas_completadas = request.POST.get('rutinas_completadas')
        # Creación del nuevo usuario
        Usuario.objects.create(nombre=nombre, nivel_condicion_fisica=nivel_condicion, rutinas_completadas=rutinas_completadas)
        return redirect('usuarios')  # Redirige a la lista de usuarios
    return render(request, 'gitapp/agregar_usuario.html')

# Vista para listar usuarios
def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'gitapp/usuarios.html', {'usuarios': usuarios})
