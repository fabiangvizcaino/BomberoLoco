from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.urls import reverse_lazy
from .models import *
from .forms import PostForm, PostForme
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
        comentarios = Comentario.objects.filter(post=id)
        context = {
            'post': post,
            'comentarios':comentarios
        }
    return render(request, 'post/posteo.html', context)

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



#FUNCION DE AGREGAR EVENTO
def agregarEvento(request):
    if request.method == 'POST':
        post_form = PostForme(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('index')
    else:
        post_form = PostForme()
    return render(request,'post/agregar_evento.html',{'post_form':post_form})


@login_required
def comentar_Post(request):

    com = request.POST.get('comentario',None)
    usu = request.user
    noti = request.POST.get('id_post', None)
    postb = Post.objects.get(id = noti) 
    Comentario.objects.create(usuario = usu, post = postb, comentario = com, fecha_post = datetime.datetime.today(), publicado = True)

    return redirect(reverse_lazy('posteo', kwargs={'id': noti}))

#PANTALLA POLÍTICAS DE PRIVACIDAD
def politicas(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('inicio')
    else:
        post_form = PostForm()
    return render(request,'post/politicas.html',{'post_form':post_form})


#VISTA AGREGAR CATEGORIA
class agregarCategoria(View):
    template_name = 'post/agregar_categoria.html'

    def get(self, request):   
        return render(request, self.template_name, {'categorias': ''})

    def post(self, request):
        
        cate = request.POST.get('categoria', None)        
        fecha = datetime.datetime.today()        

        Categoria.objects.create(nombre=cate, activado=True, fecha_creacion=fecha)

        return render(request, self.template_name)


# #VISTA AGREGAR NOTICIA
# class agregarNoticia2(View):
#     template_name = 'post/agregar_noticia2.html'

#     def get(self, request):
#         categorias = Categoria.objects.all()        
#         return render(request, self.template_name, {'categorias': categorias})


#     def post(self, request):
        
#         titu = request.POST.get('titulo', None)
#         resu = request.POST.get('resumen', None)
#         text = request.POST.get('texto', None)
#         figura = request.POST.get('imagen', None)
#         nomcate = request.POST.get('categoria', None)
#         idcate = Categoria.objects.filter(nombre = nomcate)
#         fecha = datetime.datetime.today()
#         usu = request.POST.get('usuario', None)        
               
#         Post.objects.create(titulo=titu, resumen=resu, texto=text, imagen=figura, categoria=idcate, publicado=True, fecha_creacion=fecha, usuario=usu)

#         return render(request, self.template_name)
