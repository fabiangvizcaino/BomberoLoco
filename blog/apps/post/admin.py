from django.contrib import admin
from .models import * 

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    ordering = ('id','nombre','activado','fecha_creacion')
    search_fields = ('id','nombre','activado','fecha_creacion')
    list_display = ('id','nombre','activado','fecha_creacion')
    list_filter = ('activado',)

class PostAdmin(admin.ModelAdmin):
    ordering = ('id','resumen','texto','imagen','categoria','publicado','fecha_creacion','usuario')
    search_fields = ('id','resumen','texto','imagen','categoria__nombre','publicado','fecha_creacion')
    list_display = ('titulo','resumen','imagen','categoria','publicado','fecha_creacion','usuario')
    list_filter = ('categoria__nombre','publicado')

class EventoAdmin(admin.ModelAdmin):
    ordering = ('id','resumen','descripcion','imagen','categoria','publicado','fecha_evento','modalidad','arancel','usuario')
    search_fields = ('id','resumen','descripcion','imagen','categoria__nombre','publicado','modalidad','fecha_evento')
    list_display = ('titulo','resumen','imagen','categoria','publicado','fecha_evento','usuario')
    list_filter = ('categoria__nombre','publicado')


class ComentarioAdmin(admin.ModelAdmin):
    ordering = ('id','post__titulo','usuario','comentario','fecha_post','publicado')
    search_fields = ('id','post__titulo','usuario__nombre','comentario','fecha_post','publicado')
    list_display = ('comentario','post','fecha_post','usuario')
    list_filter = ('post__titulo','publicado')


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Comentario, ComentarioAdmin)
