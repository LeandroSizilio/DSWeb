from django.shortcuts import render, get_object_or_404
from django.views import View
from models import Bazar

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'bazar/index.html')

class BazarView(View):
    def get(self, request, *args, **kwargs):
        id_bazar = kwargs ['pk']
        bazar = get_object_or_404(Bazar, pk=id_bazar)
        contexto = {'bazar': bazar}
        return render(request, 'bazar/bazar.html', contexto)