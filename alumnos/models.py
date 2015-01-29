from django.db import models
from django.contrib.auth.models import User

class Grado(models.Model):
    grado = models.CharField(max_length=60)

    def __unicode__(self):
        return self.grado


class Profesor(models.Model):
	profesor = models.OneToOneField(User)


class Asignatura(models.Model):
    asignatura = models.CharField(max_length=100)
    grado = models.ForeignKey(Grado, related_name='asignaturas')
    profesor = models.ForeignKey(Profesor, related_name='asignaturas')




class Alumno(models.Model):
    codigo = models.CharField(max_length=10,blank=True,null=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    grado = models.ForeignKey(Grado, related_name="alumnos")


class Asistencia(models.Model):
	fecha = models.DateField()
	alumno = models.ForeignKey(Alumno, related_name='asistencias')
	asignatura = models.ForeignKey(Asignatura, related_name='asistencias')
	grado = models.ForeignKey(Grado, related_name='asistencias')
	asistencia = models.IntegerField()