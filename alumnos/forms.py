from django.forms import ModelForm
from django import forms
from .models import Artistas

class ArtistasForm(forms.ModelForm):
    class Meta:
        model = Artistas 
        #fields = ['ID', 'Nombre_artista', 'descripcion', 'img'] 
   
        fields = '__all__' 

