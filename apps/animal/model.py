from django.db import models
from especies.models import Especie

class Animal(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=200)
    raca = models.CharField('Raça', max_length=100)
    sexo = models.CharField('Sexo', max_length=1, choices=[('M','Masculino'),('F','Feminino')])
    photo = models.ImageField('Foto', upload_to='photos')
    disponivel = models.BooleanField('Disponivel', default=False)
    data_resgate = models.DateField('Data de resgate', auto_now=False, auto_now_add=False)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'
        ordering =['id']

    def __str__(self):
        return f'{self.name}'
