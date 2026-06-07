from django.db import models

class Animal(models.Model):
    nome = models.CharField('Nome', max_length=50)
    foto = models.ImageField('Foto', upload_to='photos')
    especie = models.CharField(Especie, max_length=50)
    raca = models.CharField('Raça', max_length=100)
    sexo = models.CharField('Sexo', max_length=1, choices=[('M','Masculino'),('F','Feminino')])
    descricao = models.TextField('Descricao', max_length=200)
    data_inscricao = models.DateField('Data de inscricao', auto_now=False, auto_now_add=False)
    disponivel = models.BooleanField('Disponivel', default=False)
    
    
    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'
        ordering =['id']

    def __str__(self):
        return f'{self.name}'
