from django.db import models


class Vacina(models.Model):
    nome = models.CharField('Nome', max_length=50)
    dose = models.DecimalField('Dose',max_digits=5, decimal_places=2, default=0)
    descricao = models.TextField('Descricao', max_length=100) 
    
    class Meta:
        verbose_name = 'Vacina'
        verbose_name_plural = 'Vacinas'
        ordering =['id']

    def __str__(self):
        return f'{self.id} - {self.name}'
