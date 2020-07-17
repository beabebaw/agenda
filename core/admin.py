from django.contrib import admin
from core.models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulos', 'data_evento', 'data_criacao')
    list_filter = ('titulos', 'data_evento', 'usuario',)

admin.site.register(Evento, EventoAdmin)