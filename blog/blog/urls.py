"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from apps.post.views import *
from apps.usuarios.views import *
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView



urlpatterns = [
    path('accounts/login/', Login.as_view(), name= 'login'),
    path('logout/', logoutUsuario, name='logout'),
    path('registro/', RegistroUsuario.as_view(), name='registro'),    
    path('admin/', admin.site.urls),    
    path('',(inicio.as_view()), name='index'),    
    path('register/', registro, name= 'register'),    
    path('vision/', vision, name= 'vision'),
    path('mision/', mision, name= 'mision'),
    path('objetivos/', objetivo, name= 'objetivos'),
    path('nosotros/', nosotros, name= 'nosotros'),   
    path('contacto/', contacto, name= 'contacto'),
    path('participa/', participa, name= 'participa'),
    path('proyectos/', proyectos, name= 'proyectos'),
    path('documentos/', documentos, name= 'documentos'),
    path('donaciones/', donaciones, name= 'donaciones'),
    path('agregar_noticia/', agregarNoticia, name= 'agregar_noticia'),    
    #path('agregar_noticia2/',(agregarNoticia2.as_view()), name='agregar_noticia2'),
    path('agregar_evento/', agregarEvento, name= 'agregar_evento'),
    re_path('leer_post/(?P<id>\d+)/$', leerPost, name='posteo'),
    path('comentar/', comentar_Post, name='comentar'),
    path('politicas/', politicas, name= 'politicas'),
    path('index/',(inicio.as_view()), name='index2'),
    path('agregar_categoria/',(agregarCategoria.as_view()), name='agregar_categoria'),
  

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

