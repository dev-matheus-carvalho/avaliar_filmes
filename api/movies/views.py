from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Usuario, Filme, Avaliacao
from .serializers import UsuarioSerializer, FilmeSerializer, AvaliacaoSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    @action(detail=False, methods=['GET'])
    def filmes_nao_avaliados(self, request):
        # Filtra os filmes que não foram avaliados (ou seja, não possuem avaliações)
        filmes_nao_avaliados = Filme.objects.exclude(avaliacao__isnull=False)

        serializer = FilmeSerializer(filmes_nao_avaliados, many=True)
        return Response(serializer.data)
