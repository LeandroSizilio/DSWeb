from django.views import View
from django.urls import reverse
from .models import Pergunta, Alternativa
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


class IndexView(View):
    def get(self, request, *args, **kwargs): # '*' tem ideia de coleção
        enquetes = Pergunta.objects.order_by('-data_pub')[:10]

        contexto = {'lista_perguntas': enquetes}

        return render(request, 'enquetes/index.html', contexto)


class DetalhesView(View): # sobrescrever o metodo get()
    template = 'enquetes/detalhes.html'

    def get(self, request, *args, **kwargs): # '*' tem ideia de coleção
        pergunta_id = kwargs['pergunta_id']

        pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

        contexto = {'pergunta': pergunta, 'error': None}

        return render(request,self.template, contexto)



    def post(self, request, *args, **kwargs):
        pergunta_id = kwargs['pergunta_id']

        pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

        try:
            id_alternativa = request.POST['escolha']

            alt = pergunta.alternativa_set.get(pk=id_alternativa)

        except (KeyError, Alternativa.DoesNotExist):
            erro = 'Você precisa selecionar uma alternativa',

            return self.resposta(request, pergunta, erro)

        else:
            alt.quant_votos += 1

            alt.save()

            return HttpResponseRedirect(reverse(
                'enquetes:resultado', args=(pergunta_id,)
            ))

    def reposta(self, request, pergunta, erro):
        contexto = {'pergunta': pergunta, 'error':erro}
        return render(request, self.template, contexto)


class ResultadoView(View): # sobrescrever o metodo get()
    def get(self, request, *args, **kwargs): # '*' tem ideia de coleção
        pergunta_id = kwargs['pergunta_id']

        pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

        contexto = {'pergunta': pergunta}

        return render(request, 'enquetes/resultado.html', contexto)


