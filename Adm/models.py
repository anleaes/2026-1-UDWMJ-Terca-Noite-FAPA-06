class Adm(models.Model):
    nivel_acesso = models.CharField(
        'Nível de Acesso',
        max_length=50
    )

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'
        ordering = ['id']

    def cadastrar_animal(self):
        

    def aprovar_adocao(self):
        

    def reprovar_adocao(self):
        

    def gerenciar_usuarios(self):
        

    def gerar_relatorios(self):
        

    def __str__(self):
        return self.nivel_acesso
