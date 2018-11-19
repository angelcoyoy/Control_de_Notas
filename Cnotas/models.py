from django.db import models
from django.contrib import admin

class Materia(models.Model):

    nombre  =   models.CharField(max_length=30)
    docente = models.CharField(max_length=30)
    creditos  =   models.CharField(max_length=30)

    def __str__(self):

        return self.nombre

class Grado(models.Model):

    nombre    = models.CharField(max_length=60)
    semestre    = models.CharField(max_length=60)
    seccion    = models.CharField(max_length=60)
    jornada    = models.CharField(max_length=60)
    anio      = models.IntegerField()
    materias   = models.ManyToManyField(Materia, through='Asignacion')


class Asignacion (models.Model):

    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)

class ActuacionInLine(admin.TabularInline):

    model = Asignacion
#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.
    extra = 1

class MateriaAdmin(admin.ModelAdmin):

    inlines = (AsignacionInLine,)


class GradoAdmin (admin.ModelAdmin):

    inlines = (AsignacionInLine,)
