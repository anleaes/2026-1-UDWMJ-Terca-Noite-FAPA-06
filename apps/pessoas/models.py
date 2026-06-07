from django.db import models

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail',null=False, blank=False)
    telefone = models.CharField('Telefone', max_length=20)
    endereco = models.CharField('Endereco', max_length=200)  
    data_cadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['id']

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
