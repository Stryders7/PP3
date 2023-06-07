"""
URL configuration for instituto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from alumnos import views

urlpatterns = [
    path('', views.home,name='home'),
    path('admin/', admin.site.urls),
    path('alfredo/', views.alfredo,name='alfredo'),
    path('antonia/', views.antonia,name='antonia'),
    path('artistas/', views.artistas,name='artistas'),
    path('formulario/', views.formulario,name='formulario'),
    path('index/', views.index,name='index'),
    path('jorge/', views.jorge,name='jorge'),
    path('jose sanhueza/', views.josesanhueza,name='jose sanhueza'),
    path('marcelo/', views.marcelo,name='marcelo'),
    path('nosotros/', views.nosotros,name='nosotros'),
    path('registro/', views.registro,name='registro'),
    path('santiago/', views.santiago,name='santiago'),
    
    path('agregarArticulo/', views.Add_Articulo),
    path('edicionArticulo/<codigo>', views.Edicion_Articulo),
    path('editarArticulo/', views.Edit_Articulo),
    path('eliminarArticulo/<codigo>', views.Del_Articulo)
]
