class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', unique=True)
    senha = models.CharField('Senha', max_length=255)
    telefone = models.CharField('Telefone', max_length=20)
    data_cadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['id']

    def _str_(self):
        return self.nome

    # Método para atualizar dados
    def atualizar_dados(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.save()

    # Método para alterar senha
    def alterar_senha(self, nova_senha):
        self.senha = nova_senha
        self.save()
