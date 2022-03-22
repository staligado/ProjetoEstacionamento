from django.forms import ModelForm
from .models import Mensalista, MovMensalista, Pessoa, Veiculo, MovRotativo


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'


class MovrotativoForm(ModelForm):
    class Meta:
        model = MovRotativo
        fields= ['checkin','checkout','valor_hora','veiculo','pago']


class MensalistaForm(ModelForm):
    class Meta:
        model = Mensalista
        fields= ['veiculo','inicio','valor_mes']


class MovmensalistaForm(ModelForm):
    class Meta:
        model= MovMensalista
        fields= ['mensalista','dt_pgto','total']