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
from django.urls import path
from apps.post.views import agregarNoticia, logueo, registro, vision, mision, objetivo, nosotros, inicio, contacto, participa


urlpatterns = [
    path('admin/', admin.site.urls),
    path('agregar_noticia/', agregarNoticia, name= 'agregar_noticia'),
    path('index/', inicio, name= 'index'),
    path('login/', logueo, name= 'login'),
    path('register/', registro, name= 'register'),
    path('vision/', vision, name= 'vision'),
    path('mision/', mision, name= 'mision'),
    path('objetivos/', objetivo, name= 'objetivos'),
    path('nosotros/', nosotros, name= 'nosotros'),   
    path('contacto/', contacto, name= 'contacto'),
    path('participa/', participa, name= 'participa'),
]
