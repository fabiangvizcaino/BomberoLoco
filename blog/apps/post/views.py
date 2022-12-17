from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
from .forms import PostForm
import datetime

# Create your views here.

#PANTALLA DE INICIO
# def inicio(request):
#     listadoNoticias = Post.objects.all()        
#     return render(request,'post/index.html',{"noticias":listadoNoticias})
# #--------------------------------






#PANTALLA DE INICIO
def inicio(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('inicio')
    else:
        post_form = PostForm()
    return render(request,'post/index.html',{'post_form':post_form})


#PANTALLA MOSTRAR NOTICIAS - INICIO
class inicio(View):
    template_name = 'post/index.html'

    def get(self, request):
        categorias = Categoria.objects.all()
        noticias = Post.objects.all()    
        eventos = Evento.objects.all()
        contador = Evento.objects.count()
        context = {
           'noticias': noticias,
           'categorias': categorias,
           'eventos': eventos,
           'contador': contador
        }
        return render(request, self.template_name, context)


    def post(self, request):
        categorias = Categoria.objects.all()
        eventos = Evento.objects.all()
        contador = Evento.objects.count()
        cate = request.POST.get('categoria', None)
        fecha = request.POST.get('fecha', None)
        if cate and fecha:
            noticias = Post.objects.filter(categoria__nombre=cate, fecha_creacion=fecha)
        elif cate:
            noticias = Post.objects.filter(categoria__nombre=cate)
        elif fecha:
            noticias = Post.objects.filter(fecha_creacion=fecha)
        context = {
           'noticias': noticias,
           'categorias': categorias,
           'eventos': eventos,
           'contador': contador           
        }
        return render(request, self.template_name, context)


#FUNCION LEER NOTICIA
def leerPost(request, id):
    if request.method=='GET':
        post = Post.objects.get(id=id)
        context = {
            'post': post
        }
    return render(request,'post/posteo.html', context)


#PANTALLA DE LOGUEO
def logueo(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('index')
    else:
        post_form = PostForm()
    return render(request,'post/login.html',{'post_form':post_form})


#PANTALLA REGISTRACION
def registro(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('index')
    else:
        post_form = PostForm()
    return render(request,'post/register.html',{'post_form':post_form})


#PANTALLA MISION
def mision(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('inicio')
    else:
        post_form = PostForm()
    return render(request,'post/mision.html',{'post_form':post_form})


#PANTALLA VISION
def vision(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('inicio')
    else:
        post_form = PostForm()
    return render(request,'post/vision.html',{'post_form':post_form})


#PANTALLA OBJETIVOS
def objetivo(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('inicio')
    else:
        post_form = PostForm()
    return render(request,'post/objetivos.html',{'post_form':post_form})


#PANTALLA NOSOTROS
def nosotros(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('inicio')
    else:
        post_form = PostForm()
    return render(request,'post/nosotros.html',{'post_form':post_form})



# #PANTALLA DE AGREGAR NOTICIA
def agregarNoticia(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('index')
    else:
        post_form = PostForm()
    return render(request,'post/agregar_noticia.html',{'post_form':post_form})









#PANTALLA NOSOTROS
def MostrarPost(View):
    
    template_name = 'post/posteos.html'
    
    def get(self, request):
        posteos = Post.objects.all()
        categorias = Categoria.objects.all()
        context = {
            'posteos':posteos, 
            'categorias':categorias
        }
        return render (request, self.template_name, context)
    
    def post(self, request):
        Categoria = Categoria.objects.all()
        cate = request.Post.get('categoria', None)
        fecha = request.Post.get('fecha', None)
        if cate and fecha:
            posteos = Post.objects.filter(categoria__nombre=cate, fecha_creacion=fecha)
        elif cate:
            posteos = Post.objects.filter(categoria__nombre=cate)        
        elif fecha:
            posteos = Post.objects.filter(fecha_creacion=fecha)
        
#PANTALLA CONTACTO
def contacto(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('inicio')
    else:
        post_form = PostForm()
    return render(request,'post/contacto.html',{'post_form':post_form})


#PANTALLA ASPIRANTES
def participa(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('inicio')
    else:
        post_form = PostForm()
    return render(request,'post/participa.html',{'post_form':post_form})

#PANTALLA PROYECTOS
def proyectos(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('inicio')
    else:
        post_form = PostForm()
    return render(request,'post/proyectos.html',{'post_form':post_form})

#PANTALLA DOCUMENTOS
def documentos(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('inicio')
    else:
        post_form = PostForm()
    return render(request,'post/documentos.html',{'post_form':post_form})

#PANTALLA DONACIONES
def donaciones(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('inicio')
    else:
        post_form = PostForm()
    return render(request,'post/donaciones.html',{'post_form':post_form})



#PANTALLA DE AGREGAR EVENTO
def agregarEvento(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('index')
    else:
        post_form = PostForm()
    return render(request,'post/agregar_evento.html',{'post_form':post_form})



#VISTA AGREGAR NOTICIA
# class agregarNoticia(View):
#     template_name = 'post/agregar_noticia.html'

#     def get(self, request):
#         categorias = Categoria.objects.all()        
#         return render(request, self.template_name, {'categorias': categorias})

#     def post(self, request):
        
#         titulo = request.POST.get('titulo', None)
#         resumen = request.POST.get('resumen', None)
#         texto = request.POST.get('texto', None)
#         imagen = request.POST.get('imagen', None)
#         categoria = request.POST.get('categoria', None)
#         usuario = request.POST.get('usuario', None)        
#         #fecha_alta = datetime.datetime.today()
                
#         context = {
#            'titulo': titulo,           
#            'resumen': resumen,
#            'texto': texto,
#            'imagen': imagen,
#            'categoria': categoria,
#            'usuario': usuario
#         }

#         return render(request, self.template_name, context)


