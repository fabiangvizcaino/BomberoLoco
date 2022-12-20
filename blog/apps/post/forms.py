from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import fields
from django.forms.forms import Form
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','resumen','texto','imagen','categoria','usuario']


class PostForme(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo','resumen','descripcion','lugar','modalidad','arancel','imagen','categoria','usuario']

        
    