from django.shortcuts import render, redirect
from .models import Artistas
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

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
    return render(request, "alumno/login.html")

def salir (request):
    logout(request)
    return redirect('/')

def artistas_list(request):
    artistas = artistas.objects.all()
    messages.success(request, '¡artistas Listados!')
    return render(request, 'artistas_list.html', {'artistas': artistas})


def artistas_create(request):
    if request.method == 'POST':
        nombre_artista = request.POST['nombre_artistas']
        descripcion = request.POST['descripcion']
        img = request.POST['img']
        artistas = artistas(nombre_artista=nombre_artista, descripcion=descripcion, img=img)
        artistas.save()
        messages.success(request, '¡Artista Registrado!')
        return redirect('artistas_list')
    return render(request, 'artistas_create.html')


def artistas_update(request, pk):
    artistas = artistas.objects.get(pk=pk)
    if request.method == 'POST':
        artistas.nombre_artista = request.POST['nombre_artista']
        artistas.descripcion = request.POST['descripcion']
        artistas.img = request.POST['img']
        artistas.save()
        messages.success(request, '¡Artistas Actualizado!')
        return redirect('artistas_list')
    return render(request, 'artistas_update.html', {'artistas': artistas})


def artistas_delete(request, pk):
    artistas = artistas.objects.get(pk=pk)
    artistas.delete()
    messages.success(request, '¡Artista Eliminado!')
    return redirect('artistas_list')

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