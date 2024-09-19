from django import forms
from django.forms import DateTimeInput, modelformset_factory
from bazar.models import Evento, Item, Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'login', 'senha']
        widgets = {
            'senha': forms.PasswordInput()
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['descricao', 'preco', 'foto']
        widgets = {
            'preco': forms.TextInput(attrs={'placeholder': 'Digite o valor'}),
        }

ItemFormSet = modelformset_factory(Item, form=ItemForm, extra=3)  

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'banner', 'data_inicio', 'data_fim']
        widgets = {
            'data_inicio': DateTimeInput(attrs={'type': 'datetime-local'}),
            'data_fim': DateTimeInput(attrs={'type': 'datetime-local'}),
        }
