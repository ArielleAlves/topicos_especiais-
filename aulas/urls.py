#módulo do Django para criar urls
from django.urls import path

#Importe todas as suas classes do views.py
from .views import *

urlpatterns = [
    #path(
    # 'caminho/da/url',
    # ClasseLaDoView

    path('', PaginaInicialView.as_view(), name="index"),
    path('partitura/', PartituraView.as_view(), name="partitura"),
    path('videoAula/', videoAulaView.as_view(), name="videoAula"),
    path('curriculo/', curriculoView.as_view(), name="curriculo"),


    # URLS de Tipo de instrumento
    path('cadastrar/tipo/', TipoCreate.as_view(), name="cadastrar-tipo"),
    path('editar/tipo/<int:pk>/', TipoUpdate.as_view(), name="editar-tipo"),
    path('excluir/tipo/<int:pk>/', TipoDelete.as_view(), name="excluir-tipo"),
    path('listar/tipo/', TipoList.as_view(), name="listar-tipos"),

    # URLS dos Estilos Musicais
    path('cadastrar/estilo/', EstiloCreate.as_view(), name="cadastrar-estilo"),
    path('editar/estilo/<int:pk>/', EstiloUpdate.as_view(), name="editar-estilo"),
    path('excluir/estilo/<int:pk>/', EstiloDelete.as_view(), name="excluir-estilo"),
    path('listar/estilo/', EstiloList.as_view(), name="listar-estilo"),

    # URLS de Musicas
    path('cadastrar/musica/', MusicaCreate.as_view(), name="cadastrar-musica"),
    path('editar/musica/<int:pk>/', MusicaUpdate.as_view(), name="editar-musica"),
    path('excluir/musica/<int:pk>/', MusicaDelete.as_view(), name="excluir-musica"),
    path('listar/musica/', MusicaList.as_view(), name="listar-musica"),
    path('ver/musica/<int:pk>/', MusicaDetalhes.as_view(), name="detalhar-musica"),

]
