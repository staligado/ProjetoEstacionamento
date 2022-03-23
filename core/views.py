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


def lista_movrotativos(request):
    mov_rot = MovRotativo.objects.all()
    form = MovrotativoForm()
    return render(request, 'core/lista_movrotativos.html', {'mov_rot': mov_rot, 'form': form})


def movrotativo_novo(request):
    form = MovrotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos')


def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    return render(request, 'core/lista_mensalistas.html', {'mensalistas': mensalistas, 'form': form})


def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')


def lista_movmensalistas(request):
    movmensalistas = MovMensalista.objects.all()
    form = MovmensalistaForm()
    return render(request, 'core/lista_movmensalistas.html', {'movmensalistas': movmensalistas, 'form': form})


def movmensalista_novo(request):
    form = MovmensalistaForm(request.POST or None)
    if form.is_valid:
        form.save()
    return redirect('core_lista_movmensalistas')

