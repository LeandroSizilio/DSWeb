from django.contrib import admin
from .models import Pergunta, Alternativa, Autor, Rotulo

admin.site.register(Pergunta)
admin.site.register(Alternativa)
admin.site.register(Autor)
admin.site.register(Rotulo)