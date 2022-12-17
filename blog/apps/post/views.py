from django.shortcuts import render, redirect
from .models import *
from .forms import PostForm


# Create your views here.

#PANTALLA DE INICIO
def inicio(request):
    listadoNoticias = Post.objects.all()        
    return render(request,'post/index.html',{"noticias":listadoNoticias})
#--------------------------------


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


#PANTALLA DE AGREGAR NOTICIA
def agregarNoticia(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('index')
    else:
        post_form = PostForm()
    return render(request,'post/agregar_noticia.html',{'post_form':post_form})


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
def aspirantes(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('inicio')
    else:
        post_form = PostForm()
    return render(request,'post/aspirantes.html',{'post_form':post_form})

