from django.db import models

class Historico(models.Model):
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField('Descricao')
    realizado_por = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Historico'
        verbose_name_plural = 'Historicos'
        ordering = ['-data']

    def __str__(self):
        return f'{self.id} - {self.animal}'
