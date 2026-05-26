class Adotante(models.Model):
    cpf = models.CharField(
        'CPF',
        max_length=14
    )

    endereco = models.CharField(
        'Endereço',
        max_length=255
    )

    data_nascimento = models.DateField(
        'Data de Nascimento'
    )

    possui_outro_animal = models.BooleanField(
        'Possui outro animal?',
        default=False
    )

    class Meta:
        verbose_name = 'Adotante'
        verbose_name_plural = 'Adotantes'
        ordering = ['id']

    def __str__(self):
    return self.cpf
