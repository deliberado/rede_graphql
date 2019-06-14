from django.contrib import admin
from .models import Comentario, Publicacao


@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):
    pass

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    pass
