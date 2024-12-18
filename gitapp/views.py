from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Ejercicio, Rutina, Usuario
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm


# Vista para la página principal (index)
def index(request):
    return render(request, 'gitapp/index.html')

# Vista de login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Autenticación del usuario
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirige al index después de login
    else:
        form = AuthenticationForm()
    return render(request, 'gitapp/login.html', {'form': form})

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

# Vista para listar usuarios
def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'gitapp/usuarios.html', {'usuarios': usuarios})

@csrf_protect
@login_required
def editar_usuario(request, usuario_id):
    # Obtiene el usuario que se va a editar
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    if request.method == 'POST':
        # Obtiene los datos del formulario
        nombre = request.POST.get('nombre')
        nivel_condicion = request.POST.get('nivel_condicion')
        rutinas_completadas_ids = request.POST.getlist('rutinas_completadas')  # Obtiene las rutinas seleccionadas
        
        # Actualiza los detalles del usuario
        usuario.nombre = nombre
        usuario.nivel_condicion_fisica = nivel_condicion
        usuario.save()  # Guarda los cambios en el usuario
        
        # Actualiza las rutinas completadas
        usuario.rutinas_completadas.set(rutinas_completadas_ids)  # Asigna las rutinas completadas
        
        return redirect('usuarios')  # Redirige a la lista de usuarios
    
    # Si es un GET, mostramos el formulario con los datos actuales
    rutinas = Rutina.objects.all()
    return render(request, 'gitapp/editar_usuario.html', {'usuario': usuario, 'rutinas': rutinas})

# Vista para agregar un nuevo usuario
@csrf_protect
@login_required
def agregar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        nivel_condicion = request.POST.get('nivel_condicion')
        rutinas_completadas_ids = request.POST.getlist('rutinas_completadas')  # Obtienes los ids de las rutinas completadas
        
        # Crear el nuevo usuario
        usuario = Usuario.objects.create(
            nombre=nombre,
            nivel_condicion_fisica=nivel_condicion
        )
        
        # Asignar las rutinas completadas
        usuario.rutinas_completadas.set(rutinas_completadas_ids)  # Asigna las rutinas completadas
        
        return redirect('usuarios')  # Redirige a la lista de usuarios
    
    # Obtener todas las rutinas para mostrarlas en el formulario
    rutinas = Rutina.objects.all()
    return render(request, 'gitapp/agregar_usuario.html', {'rutinas': rutinas})

# Vista para eliminar un usuario
@login_required
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuarios')  # Redirige a la lista de usuarios
    return render(request, 'gitapp/eliminar_usuario.html', {'usuario': usuario})

def editar_ejercicio(request, ejercicio_id):
    ejercicio = get_object_or_404(Ejercicio, id=ejercicio_id)
    
    if request.method == 'POST':
        ejercicio.nombre = request.POST.get('nombre')
        ejercicio.descripcion = request.POST.get('descripcion')
        ejercicio.dificultad = request.POST.get('dificultad')
        ejercicio.save()
        return redirect('ejercicios')
    
    return render(request, 'gitapp/editar_ejercicio.html', {'ejercicio': ejercicio})

# Vista para eliminar ejercicio
def eliminar_ejercicio(request, ejercicio_id):
    ejercicio = get_object_or_404(Ejercicio, id=ejercicio_id)
    if request.method == 'POST':
        ejercicio.delete()
        return redirect('ejercicios')
    return render(request, 'gitapp/eliminar_ejercicio.html', {'ejercicio': ejercicio})

# Vista para editar rutina
def editar_rutina(request, rutina_id):
    rutina = get_object_or_404(Rutina, id=rutina_id)
    ejercicios = Ejercicio.objects.all()
    if request.method == 'POST':
        rutina.nombre = request.POST.get('nombre')
        rutina.duracion = request.POST.get('duracion')
        rutina.ejercicios.set(request.POST.getlist('ejercicios'))
        rutina.save()
        return redirect('rutinas')
    return render(request, 'gitapp/editar_rutina.html', {'rutina': rutina, 'ejercicios': ejercicios})

# Vista para eliminar rutina
def eliminar_rutina(request, rutina_id):
    rutina = get_object_or_404(Rutina, id=rutina_id)
    if request.method == 'POST':
        rutina.delete()
        return redirect('rutinas')
    return render(request, 'gitapp/eliminar_rutina.html', {'rutina': rutina})

# Vista personalizada para el logout
def logout_view(request):
    logout(request)  # Cierra la sesión
    return redirect('login')  # Redirige a la página de login