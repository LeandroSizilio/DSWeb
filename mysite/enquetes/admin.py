from django.contrib import admin
from .models import Pergunta, Alternativa, Rotulo, Autor

admin.site.register(Pergunta)
admin.site.register(Alternativa)
admin.site.register(Rotulo)
admin.site.register(Autor)