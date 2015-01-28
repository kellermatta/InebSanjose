from rest_framework import serializers
from alumnos.models import Alumno,Grado,Asignatura

class AlumnoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alumno


class GradoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grado


class AsignaturaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asignatura