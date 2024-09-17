import re
from math import floor
from bazar.forms import *
from django.views import View
from bazar.models import Evento
from django.utils import timezone
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from bazar.forms import EventoForm, ItemFormSet
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


class IndexView(View):

    def get(self, request, *args, **kwargs):

        cliente = None

        if request.user.is_authenticated:
             
             cliente = Cliente.objects.get(user=request.user)

        eventos = Evento.objects.filter(data_fim__gt=timezone.now()).order_by('data_fim')

        contexto = {
            'cliente': cliente,
            'eventos': eventos
        }

        return render(request, 'index.html', context=contexto)
   

class CadastroView(View):

    def get(self, request,*args, **kwargs):

        form = ClienteForm()

        return render(request, "cadastro.html", {'form': form})
    
    def post(self, request, *args, **kwargs):
        
        form = ClienteForm(request.POST)

        if form.is_valid():

            login = form.cleaned_data['login']

            senha = form.cleaned_data['senha']

            user = User.objects.create_user(username=login, password=senha)

            cliente = form.save(commit=False)

            cliente.user = user

            cliente.save()

            return HttpResponseRedirect(reverse('bazar:login'))
        
        else:
            form = ClienteForm()

            return render(request, "cadastro.html", {'form': form}) 


class LogarView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):

        dados_requisicao = request.POST

        if dados_requisicao['login'] != '' and  dados_requisicao['senha'] != '':
            nome_login = dados_requisicao.get('login')

            senha = dados_requisicao.get('senha')

            usuario = authenticate(username=nome_login, password=senha)

            if usuario is not None:
                login(request, usuario)

                return redirect(reverse('bazar:index'))
            
            else:
                messages.error(request, 'O usuario não existe.')

                return render(request, 'login.html')
            
        else:
            messages.error(request, 'Insira os dados obrigatorios.')

            return render(request, 'login.html')


class LogoutView(View):
        
        @method_decorator(login_required)
        def post(self, request, *args, **kwargs):

            logout(request)

            return HttpResponseRedirect(reverse('bazar:index'))


class ItensEventoView(View):
        
        def get(self, request, *args, **kwargs): 

            id_evento = kwargs.get('id')

            evento = Evento.objects.get(id=id_evento)

            itens = Item.objects.filter(evento=evento)

            cliente = None

            if request.user.is_authenticated:

                user_cliente = request.user

                cliente = Cliente.objects.get(user=user_cliente)

            contexto = {
                'evento': evento,
                'itens': itens,
                'cliente': cliente,
            }

            return render(request, "ver_evento.html", context=contexto)
           

class EventoView(View):
        
        @method_decorator(login_required)
        def get(self, request, *args, **kwargs): 

            evento_form = EventoForm()

            item_formset = ItemFormSet(queryset=Item.objects.none())  # Nenhum item inicialmente

            contexto = {
                'evento_form': evento_form,
                'form_itens': item_formset,
            }

            return render(request, 'evento.html', context=contexto)

        
        @method_decorator(login_required)
        def post(self, request, *args, **kwargs):

            evento_form = EventoForm(request.POST, request.FILES)

            itens_forms = ItemFormSet(request.POST, request.FILES)


            if evento_form.is_valid() and itens_forms.is_valid():

                evento = evento_form.save() # salvo o evento

                # Salva os itens
                for form in itens_forms:
                    
                    item = form.save(commit=False)

                    item.evento = evento

                    item.save()

                evento.save()

                return HttpResponseRedirect(reverse('bazar:index'))
            
            else:

                return render(request, 'evento.html', context={'evento_form': evento_form, 'form_itens': itens_forms})


class ItensView(View):
        
        def get(self, request, *args, **kwargs): 

            itens = Item.objects.all()

            cliente = None

            if request.user.is_authenticated:

                user_cliente = request.user

                cliente = Cliente.objects.get(user=user_cliente)

            contexto = {
                'itens': itens,
                'cliente': cliente,
            }

            return render(request, "itens.html", context=contexto)
        

        def post(self, request, *args, **kwargs):

            dados_pesquisa = request.POST
            
            contexto = {}

            if 'pesquisa' in dados_pesquisa:

                pesquisa_item = dados_pesquisa.get('pesquisa')

                if pesquisa_item != '':

                    itens = Item.objects.filter(descricao__icontains=pesquisa_item)
                    
                    contexto['itens'] = itens

                else:

                    contexto['itens'] = Item.objects.all()

                contexto['status'] = 'sucesso'
                
            else:

                contexto['status'] = 'erro'

            return render(request, 'itens.html', context=contexto)


class ReservarView(View):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):

        item_id = kwargs.get('id')

        item = Item.objects.get(id=item_id)

        if not item.reservado:

            item.reservado = True

            item.save()

        referer_url = request.META.get('HTTP_REFERER', reverse('bazar:index'))

        return HttpResponseRedirect(referer_url)










