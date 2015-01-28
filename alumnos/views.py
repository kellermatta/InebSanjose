from django.shortcuts import render
from rest_framework import viewsets
from alumnos.models import Alumno, Grado, Asignatura
from rest_framework.response import Response
from alumnos.serializers import AlumnoSerializer, GradoSerializer, AsignaturaSerializer
from rest_framework.decorators import detail_route, list_route

class AlumnoViewsets(viewsets.ModelViewSet):
	queryset = Alumno.objects.all()
	serializer_class = AlumnoSerializer


	def list(self, request):
		queryset = Alumno.objects.all()
		serializer = AlumnoSerializer(queryset, many=True)
    	
		return Response(serializer.data)


class GradoViewsets(viewsets.ModelViewSet):

    queryset = Grado.objects.all()
    serializer_class = GradoSerializer

    def retrieve(self, request, pk):
		queryset = Alumno.objects.filter(grado=pk)
		serializer = AlumnoSerializer(queryset, many=True)
    	
		return Response(serializer.data)



class AsignaturaViewsets(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    serializer_class = AlumnoSerializer
# Create your views here.


# Create your views here.
