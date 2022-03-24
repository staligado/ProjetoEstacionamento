from unicodedata import name
from django.urls import path
from .views import (
    home, 
    lista_pessoas, 
    lista_veiculos,
    lista_movrotativos,
    lista_mensalistas,
    lista_movmensalistas,
    movmensalista_novo,
    pessoa_novo,
    veiculo_novo,
    movrotativo_novo,
    mensalista_novo,
    movmensalista_novo,
    pessoa_update,
    veiculo_update,
    movrotativo_update,
    mensalista_update,
    movmensalista_update,
    pessoa_delete,
    veiculo_delete,
    )



urlpatterns = [
    path("", home, name='core_home'),
    path("pessoas/", lista_pessoas ,name='core_lista_pessoas'),
    path("pessoa-novo/", pessoa_novo ,name='core_pessoa_novo'),
    path("pessoa-update/<id>", pessoa_update , name='core_pessoa_update'),
    path("pessoa-delete/<id>", pessoa_delete, name='core_pessoa_delete'),
    path("veiculos/", lista_veiculos ,name='core_lista_veiculos'),
    path("veiculo-novo/", veiculo_novo ,name='core_veiculo_novo'),
    path("veiculo-update/<id>", veiculo_update, name='core_veiculo_update'),
    path("veiculo-delete/<id>", veiculo_delete, name='core_veiculo_delete'),
    path("mov-rot/", lista_movrotativos ,name='core_lista_movrotativos'),
    path("mov-rot-novo", movrotativo_novo, name='core_movrotativo_novo' ),
    path("mov-rot-update/<id>", movrotativo_update, name= 'core_movrotativo_update'),
    path("mensalistas/", lista_mensalistas ,name='core_lista_mensalistas'),
    path("mensalista-novo", mensalista_novo, name='core_mensalista_novo'),
    path("mensalista-update/<id>", mensalista_update, name='core_mensalista_update'),
    path("mov-mensalistas/", lista_movmensalistas ,name='core_lista_movmensalistas'),
    path('movmensalista-novo/', movmensalista_novo, name='core_movmensalista_novo'),
    path("movmensalista-update", movmensalista_update, name='core_movmensalista_update'),
]
