from django.db import models

class AdocaoDeAnimais(models.Model):
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE)
    adocao = models.ForeignKey('Adocao', on_delete=models.CASCADE)
    numero_de_animais = models.IntegerField('Numero de Animais', default=0)

    class Meta:
        verbose_name = 'Adocao de Animais'
        verbose_name_plural = 'Adocoes de Animais'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.animal}'
