from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'        
        self.fields['password'].widget.attrs['class'] = 'form-control'

        
class ResgistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
        ]
        labels = {
            'username': 'Usuario',
            'first_name': 'Nombre/s',
            'last_name': 'Apellido/s',
            'email': 'Email',
        }


class ResetPasswordForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ingrese un usuario',
        'class': 'form-cpntrol',
        'autocomplete': 'off'
    }))

    