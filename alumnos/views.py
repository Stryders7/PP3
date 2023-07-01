from django.shortcuts import render, redirect
from .models import Artistas
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

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
def login (request):
    return render(request, "alumnos/login.html")

def salir (request):
    logout(request)
    return redirect('/')

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

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Mostrar mensaje de error de inicio de sesión
            pass
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('registration/login')
    return render(request, 'registration/register.html')

'''
def home(request):
     articuloListados = Tb_Articulo.objects.all()
     messages.success(request, '¡Articulos Listados!')
     return render(request, "gestionArticulos.html", {"articulos": articuloListados})

def Add_Articulo(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    stock = request.POST['numStock']
    articulo = Tb_Articulo.objects.create(
        codigo=codigo, nombre=nombre, stock=stock)
    messages.success(request, '¡Artículo Registrado!')
    return redirect('/')

def Edit_Articulo(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    stock = request.POST['numStock']
    articulo = Tb_Articulo.objects.get(codigo=codigo)
    articulo.nombre = nombre
    articulo.creditos = stock
    articulo.save()
    messages.success(request, '¡Artículo Actualizado!')
    return redirect('/')

def Del_Articulo(request, codigo):
    articulo = Tb_Articulo.objects.get(codigo=codigo)
    articulo.delete()
    messages.success(request, '¡Artículo Eliminado!')
    return redirect('/')

def Edicion_Articulo(request, codigo):
    articulo = Tb_Articulo.objects.get(codigo=codigo)
    return render(request, "edicionArticulo.html", {"articulo": articulo})
'''