from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome
    

class Filme(models.Model):
    titulo = models.CharField(max_length=255)
    ano = models.IntegerField()
    descricao = models.TextField()
    
    def __str__(self):
        return self.titulo


class Avaliacao(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nota = models.FloatField()
    comentario = models.TextField()

    def __str__(self):
        return f'{self.filme} {self.nota}'
