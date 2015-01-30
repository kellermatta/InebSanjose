from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from alumnos import views

router = routers.DefaultRouter()
router.register(r'alumnos', views.AlumnoViewsets)
router.register(r'grados',views.GradoViewsets)
router.register(r'asignaturas', views.AsignaturaViewsets)
router.register(r'asistencias', views.AsistenciaViewset)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'colegio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^token-auth/$',obtain_auth_token)
    
)


