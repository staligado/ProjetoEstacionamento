import re
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MensalistaForm, MovmensalistaForm, PessoaForm, VeiculoForm, MovrotativoForm
from .models import (
    Mensalista, 
    Pessoa, 
    Veiculo, 
    MovRotativo, 
    Mensalista,
    MovMensalista,
)


@login_required
def home(request):
    context = {'mensagem': 'Ola Mundo'}
    return render(request, 'core/index.html', context)

@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    return render(request, 'core/lista_pessoas.html', {'pessoas': pessoas, 'form': form})


@login_required
def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


@login_required
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


@login_required
def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)

    if request.method == "POST":
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': pessoa})


@login_required
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    return render(request, 'core/lista_veiculos.html', {'veiculos': veiculos, 'form': form})


@login_required
def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


@login_required
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


@login_required
def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)

    if request.method == "POST":
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': veiculo})


@login_required
def lista_movrotativos(request):
    mov_rot = MovRotativo.objects.all()
    form = MovrotativoForm()
    return render(request, 'core/lista_movrotativos.html', {'mov_rot': mov_rot, 'form': form})


@login_required
def movrotativo_novo(request):
    form = MovrotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos')


@login_required
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


@login_required
def movrotativo_delete(request, id):
    mov_rot = MovRotativo.objects.get(id=id)

    if request.method == "POST":
        mov_rot.delete()
        return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': mov_rot})


@login_required
def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    return render(request, 'core/lista_mensalistas.html', {'mensalistas': mensalistas, 'form': form})


@login_required
def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')


@login_required
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


@login_required
def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)

    if request.method == "POST":
        mensalista.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj':mensalista})
    

@login_required
def lista_movmensalistas(request):
    mov_mensalistas = MovMensalista.objects.all()
    form = MovmensalistaForm()
    return render(request, 'core/lista_movmensalistas.html', {'mov_mensalistas': mov_mensalistas, 'form': form})


@login_required
def movmensalista_novo(request):
    form = MovmensalistaForm(request.POST or None)
    if form.is_valid:
        form.save()
    return redirect('core_lista_movmensalistas')


@login_required
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


@login_required
def movmensalista_delete(request, id):
    mov_mensalista = MovMensalista.objects.get(id=id)

    if request.method == "POST":
        mov_mensalista.delete()
        return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj':mov_mensalista})