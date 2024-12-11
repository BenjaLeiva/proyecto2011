from rest_framework import serializers
from .models import Ejercicio, Rutina, Usuario

class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = ['id', 'nombre', 'descripcion', 'dificultad']

class RutinaSerializer(serializers.ModelSerializer):
    ejercicios = EjercicioSerializer(many=True)

    class Meta:
        model = Rutina
        fields = ['id', 'nombre', 'ejercicios', 'duracion']

class UsuarioSerializer(serializers.ModelSerializer):
    rutinas_completadas = RutinaSerializer(many=True)

    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'nivel_condicion_fisica', 'rutinas_completadas']
