from django import views
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [

    path('', inicioView.as_view(), name = 'inicio'),
    path('login/', loginPagina.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(template_name='app/logout.html'), name='logout'),
    path('registro/', registroPagina.as_view(), name = 'registro'),
    path('edicionPerfil/', usuarioEdicion.as_view(), name = 'editar_perfil'),
    path('passwordCambio/', cambioPassword.as_view(), name = 'cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),

    path('listaHoodies/', hoodiesList.as_view(), name='hoodiess'),
    path('listaCamisas/', camisasList.as_view(), name='camisass'),
    path('listaZapatos/', zapatosList.as_view(), name='zapatoss'),
    path('listaPantalones/', pantalonesList.as_view(), name='pantaloness'),
    path('listaBoxers/', boxersList.as_view(), name='boxers'),
    path('listaPulseras/', pulserasList.as_view(), name='pulserass'),
    path('listaGorras/', gorrasList.as_view(), name='gorrass'),

    path('hoodiesDetalle/<int:pk>/', hoodiesDetail.as_view(), name='hoodies'),
    path('camisasDetalle/<int:pk>/', camisasDetail.as_view(), name='camisas'),
    path('zapatosDetalle/<int:pk>/', zapatosDetail.as_view(), name='zapatos'),
    path('pantalonesDetalle/<int:pk>/', pantalonesDetail.as_view(), name='pantalones'),
    path('boxerDetalle/<int:pk>/', boxersDetail.as_view(), name='boxer'),
    path('pulserasDetalle/<int:pk>/', pulserasDetail.as_view(), name='pulseras'),
    path('gorrasDetalle/<int:pk>/', gorrasDetail.as_view(), name='gorras'),

    path('hoodiesEdicion/<int:pk>/', hoodiesUpdate.as_view(), name='hoodies_editar'),
    path('camisasEdicion/<int:pk>/', camisasUpdate.as_view(), name='camisas_editar'),
    path('zapatosEdicion/<int:pk>/', zapatosUpdate.as_view(), name='zapatos_editar'),
    path('pantalonesEdicion/<int:pk>/', pantalonesUpdate.as_view(), name='pantalones_editar'),
    path('boxerEdicion/<int:pk>/', boxersUpdate.as_view(), name='boxer_editar'),
    path('pulserasEdicion/<int:pk>/', pulserasUpdate.as_view(), name='boxer_editar'),
    path('gorrasEdicion/<int:pk>/', gorrasUpdate.as_view(), name='gorras_editar'),


    path('hoodiesBorrado/<int:pk>/', hoodiesDelete.as_view(), name='hoodies_eliminar'),
    path('camisasBorrado/<int:pk>/', camisasDelete.as_view(), name='camisas_eliminar'),
    path('zapatosBorrado/<int:pk>/', zapatosDelete.as_view(), name='zapatos_eliminar'),
    path('pantalonesBorrado/<int:pk>/', pantalonesDelete.as_view(), name='pantalones_eliminar'),
    path('boxerBorrado/<int:pk>/', boxerDelete.as_view(), name='boxer_eliminar'),
    path('pulserasBorrado/<int:pk>/', pulserasDelete.as_view(), name='pulseras_eliminar'),
    path('gorrasBorrado/<int:pk>/', gorrasDelete.as_view(), name='gorras_eliminar'),

    path('prendaCreacion/', crearPrenda.as_view(), name='nuevo'),

    path('hoodiesDetalle/<int:pk>/comentario/', comentarioPagina.as_view(), name='comentario'),
    path('camisasDetalle/<int:pk>/comentario/', comentarioPagina.as_view(), name='comentario'),
    path('zapatosDetalle/<int:pk>/comentario/', comentarioPagina.as_view(), name='comentario'),
    path('pantalonesDetalle/<int:pk>/comentario/', comentarioPagina.as_view(), name='comentario'),
    path('boxerDetalle/<int:pk>/comentario/', comentarioPagina.as_view(), name='comentario'),
    path('pulserasDetalle/<int:pk>/comentario/', comentarioPagina.as_view(), name='comentario'),
    path('gorrasDetalle/<int:pk>/comentario/', comentarioPagina.as_view(), name='comentario'),
]