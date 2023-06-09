from django.shortcuts import render, redirect
#from .models import Tb_Articulo
from django.contrib import messages


# Create your views here.

def alfredo(request):
    return render(request, "alfredo.html")

def antonia(request):
    return render(request, "antonia.html")

def artistas(request):
    return render(request, "artistas.html")

def formulario(request):
    return render(request, "formulario.html")

def index(request):
    return render(request, "alumnos/index.html")

def jorge(request):
    return render(request, "jorge.html")

def josesanhueza(request):
    return render(request, "jose sanhueza.html")

def marcelo(request):
    return render(request, "marcelo.html")

def nosotros(request):
    return render(request, "nosotros.html")

def registro(request):
    return render(request, "registro.html")

def santiago(request):
    return render(request, "santiago.html")

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