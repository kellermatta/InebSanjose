from django.db import models

class Grado(models.Model):
    grado = models.CharField(max_length=60)

    def __unicode__(self):
        return self.grado


class Asignatura(models.Model):
    asignatura = models.CharField(max_length=100)
    grado = models.ForeignKey(Grado, related_name='asignaturas')


class Alumno(models.Model):
    codigo = models.CharField(max_length=10,blank=True,null=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    grado = models.ForeignKey(Grado, related_name="alumnos")