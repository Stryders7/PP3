#from django.conf.urls import url
from django.urls import path
from  . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import artistas_list, artistas_create, artistas_update, artistas_delete

urlpatterns = [
    path('', artistas_list, name='artistas_list'),
    path('create/', artistas_create, name='artistas_create'),
    path('update/<int:pk>/', artistas_update, name='artistas_update'),
    path('delete/<int:pk>/', artistas_delete, name='artistas_delete'),
]


urlpatterns = [
   path('', views.index,name='index'),
   path('nosotros/', views.nosotros, name='nosotros'),
   path('alfredo/', views.alfredo,name='alfredo'),
   path('antonia/', views.antonia,name='antonia'),
   path('artistas/', views.artistas,name='artistas'),
   path('formulario/', views.formulario,name='formulario'),
   path('jorge/', views.jorge,name='jorge'),
   path('jose sanhueza/', views.josesanhueza,name='jose sanhueza'),
   path('marcelo/', views.marcelo,name='marcelo'),
   path('registro/', views.registro,name='registro'),
   path('santiago/', views.santiago,name='santiago'),
 ] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
   path('agregarArticulo/', views.Add_Articulo),
   path('edicionArticulo/<codigo>', views.Edicion_Articulo),
   path('editarArticulo/', views.Edit_Articulo),
   path('eliminarArticulo/<codigo>', views.Del_Articulo)
'''











'''
from django.contrib import admin
from django.urls import path
from .views import 
urlpatterns = [
    
   
]

'''