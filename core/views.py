import re
from django.shortcuts import render, redirect
from .forms import MensalistaForm, MovmensalistaForm, PessoaForm, VeiculoForm, MovrotativoForm
from .models import (
    Mensalista, 
    Pessoa, 
    Veiculo, 
    MovRotativo, 
    Mensalista,
    MovMensalista,
)


def home(request):
    context = {'mensagem': 'Ola Mundo'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    return render(request, 'core/lista_pessoas.html', {'pessoas': pessoas, 'form': form})


def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form 

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)


def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)

    if request.method == "POST":
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': pessoa})


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    return render(request, 'core/lista_veiculos.html', {'veiculos': veiculos, 'form': form})


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)


def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)

    if request.method == "POST":
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': veiculo})


def lista_movrotativos(request):
    mov_rot = MovRotativo.objects.all()
    form = MovrotativoForm()
    return render(request, 'core/lista_movrotativos.html', {'mov_rot': mov_rot, 'form': form})


def movrotativo_novo(request):
    form = MovrotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos')


def movrotativo_update(request, id):
    data = {}
    mov_rot = MovRotativo.objects.get(id=id)
    form = MovrotativoForm(request.POST or None, instance=mov_rot)
    data['mov_rot'] = mov_rot
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/update_movrotativo.html', data)


def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    return render(request, 'core/lista_mensalistas.html', {'mensalistas': mensalistas, 'form': form})


def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')


def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/update_mensalista.html', data)


def lista_movmensalistas(request):
    mov_mensalista = MovMensalista.objects.all()
    form = MovmensalistaForm()
    return render(request, 'core/lista_movmensalistas.html', {'mov_mensalista': mov_mensalista, 'form': form})


def movmensalista_novo(request):
    form = MovmensalistaForm(request.POST or None)
    if form.is_valid:
        form.save()
    return redirect('core_lista_movmensalistas')


def movmensalista_update(request, id):
    data ={}
    mov_mensalista = MovMensalista.objects.get(id=id)
    form = MovmensalistaForm(request.POST or None, instance=mov_mensalista)
    data['mov_mensalista'] = mov_mensalista
    data['form'] = form

    if request.method == "POST":
        if form.is_valid:
            form.save()
            return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/update_movmensalista.html', data)

