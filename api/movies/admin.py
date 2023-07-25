from django.contrib import admin
from .models import Usuario, Filme, Avaliacao


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade')


class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano')


class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('filme', 'usuario', 'nota')


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Filme, FilmeAdmin)
admin.site.register(Avaliacao, AvaliacaoAdmin)


