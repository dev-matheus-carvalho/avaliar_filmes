from rest_framework import serializers
from .models import Usuario, Filme, Avaliacao

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'idade')


class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = ('id', 'titulo', 'ano', 'descricao')


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('id', 'filme', 'usuario', 'nota', 'comentario')