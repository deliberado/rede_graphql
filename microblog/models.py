from django.db import models
from django.contrib.auth.models import User


class Publicacao(models.Model):
    texto = models.TextField('Texto',max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, verbose_name="Autor", on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

    def __str__(self):
        return "Post numero: {}".format(self.pk)

class Comentario(models.Model):
    autor = models.ForeignKey(User, verbose_name="Autor", on_delete=models.DO_NOTHING)
    publicacao = models.ForeignKey(Publicacao, related_name="comentario", on_delete=models.CASCADE)
    texto = models.TextField(verbose_name="Deixe um comentário:")
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    def __unicode__(self):
        return "Comentario do post numero: {}".format(self.publicacao.pk)
