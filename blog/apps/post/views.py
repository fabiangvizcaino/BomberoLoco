from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.

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
            return redirect('inicio')
    else:
        post_form = PostForm()
    return render(request,'post/agregar_noticia.html',{'post_form':post_form})


#PANTALLA DE LOGUEO
def logueo(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('login')
    else:
        post_form = PostForm()
    return render(request,'post/login.html',{'post_form':post_form})


#PANTALLA REGISTRACION
def registro(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('inicio')
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
