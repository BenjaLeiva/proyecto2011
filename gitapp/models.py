from django.db import models

class Ejercicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    dificultad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Rutina(models.Model):
    nombre = models.CharField(max_length=100)
    ejercicios = models.ManyToManyField(Ejercicio)
    duracion = models.DurationField()

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    nivel_condicion_fisica = models.CharField(max_length=50)
    rutinas_completadas = models.ManyToManyField(Rutina)

    def __str__(self):
        return self.nombre
