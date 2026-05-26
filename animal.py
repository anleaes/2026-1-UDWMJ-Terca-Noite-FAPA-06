from django.db import models

class Animal(models.Model):
    nome = models.CharField('Nome', max_length=50)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    raca = models.CharField('Raça', max_length=100)
    sexo = models.BooleanField('Sexo', default=False)
    descricao = models.TextField('Descricao', max_length=200)
    data_inscricao = models.DateField('Data de inscricao', auto_now=False, auto_now_add=False)
    disponivel = models.BooleanField('Disponivel', default=False)
    foto = models.ImageField('Foto', upload_to='photos')
    
    
    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'
        ordering =['id']

    def __str__(self):
        return f'{self.name}'
