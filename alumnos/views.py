from django.shortcuts import render, redirect
from .models import Artistas
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import JsonResponse
from datetime import datetime




def alfredo(request):
    return render(request, "alumnos/alfredo.html")

def antonia(request):
    return render(request, "alumnos/antonia.html")

def artistas(request):
    return render(request, "alumnos/artistas.html")

def formulario(request):
    return render(request, "alumnos/formulario.html")

def index(request):
    return render(request, "alumnos/index.html")

def jorge(request):
    return render(request, "alumnos/jorge.html")

def josesanhueza(request):
    return render(request, "alumnos/jose sanhueza.html")

def marcelo(request):
    return render(request, "alumnos/marcelo.html")

def nosotros(request):
    return render(request, "alumnos/nosotros.html")

def registro(request):
    return render(request, "alumnos/registro.html")

def santiago(request):
    return render(request, "alumnos/santiago.html")

# gestion de usuarios

def artistas_list(request):
    artistas = Artistas.objects.all()
    messages.success(request, '¡artistas Listados!')
    return render(request, 'alumnos/artistas_list.html', {'artistas': artistas})


def artistas_create(request):
    if request.method == 'POST':
        ID_artista = request.POST['ID_artista']
        nombre_artista = request.POST['nombre_artista']
        descripcion = request.POST['descripcion']
        img = request.FILES['img']
        artistas = Artistas(nombre_artista=nombre_artista, descripcion=descripcion, img=img, ID_artista=ID_artista)
        artistas.save()
        messages.success(request, '¡Artista Registrado!')
        return redirect('artistas_list')
    return render(request, 'alumnos/artistas_create.html')


def artistas_update(request):
    artistas = Artistas.objects.all()
    if request.method == 'POST':
        artistas = Artistas.objects.get(ID_artista=request.POST['ID_artista'])
        artistas.nombre_artista = request.POST['nombre_artista']
        artistas.descripcion = request.POST['descripcion']
        artistas.img = request.FILES['img']
        artistas.save()
        messages.success(request, '¡Artista Actualizado!')
        return redirect('artistas_list')
    return render(request, 'alumnos/artistas_update.html')


def artistas_delete(request):
    artistas = Artistas.objects.all()
    if request.method == 'POST':
        ID_artista = request.POST['ID_artista']
        artista = Artistas.objects.get(ID_artista=ID_artista)
        artista.delete()
        messages.success(request, '¡Artista Eliminado!')
        return redirect('artistas_list')
    return render(request, 'alumnos/artistas_delete.html', {'artistas': artistas})



#Funcion para registrar usuario
def register_view(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.create_user(
                    username=request.POST['username'],
                    password =request.POST['password1'])
                    user.save()
                    login(request, user)
                    return redirect('index')
                except IntegrityError:
                    return render(request, 'registration/register.html', {
                    'form': UserCreationForm,
                    "error" : 'Usuario ya existe'
                })
            
        return render(request, 'registration/register.html', {
                    'form': UserCreationForm,
                    "error" : 'La contraseña no coincide'
                })

#Funcion para loguearse
def login_view(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html',{
        'form': AuthenticationForm
    })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'registration/login.html',{
                'form': AuthenticationForm,
                'error': 'Username o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('index')

#Funcion para cerrar sesion
def logout_view(request):
    logout(request)
    return redirect('index')


#Funcion de API

def obtener_hora(request):
    hora_actual = datetime.now().strftime("%H:%M:%S")
    data = {
        'hora': hora_actual,
    }
    return JsonResponse(data)