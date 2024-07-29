from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Pergunta, Alternativa
from django.shortcuts import render, get_object_or_404
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        enquetes = Pergunta.objects.order_by('-data_pub')[:10]
        contexto = {'pergunta_list': enquetes}
        return render(request, 'enquetes/index.html', contexto)


class DetalhesView(View):
    template = 'enquetes/pergunta_detail.html'

    def resposta(self, request, pergunta, error):
        contexto = {'pergunta': pergunta, 'error':error}
        return render(request, self.template, contexto)



    def get(self, request, *args, **kwargs):
        pergunta_id = kwargs['pk']
        pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
        return self.resposta(request, pergunta, None)

    def post(self, request, *args, **kwargs):
        pergunta_id = kwargs['pk']
        pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
        try:
            id_alternativa = request.POST['escolha']
            alt = pergunta.alternativa_set.get(pk=id_alternativa)
        except (KeyError, Alternativa.DoesNotExist):
            error = 'Você precisa selecionar uma alternativa.'
            return self.resposta(request, pergunta, error)
        else:
            alt.quant_votos += 1
            alt.save()
            return HttpResponseRedirect(reverse(
                'enquetes:resultado', args=(pergunta.id,)
            ))

class ResultadoView(View):
    def get(self, request, *args, **kwargs):
        pergunta_id = kwargs['pk']
        pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
        contexto = {'pergunta': pergunta}
        return render(request, 'enquetes/resultado.html', contexto)

