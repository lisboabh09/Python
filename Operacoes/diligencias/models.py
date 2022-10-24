from django.db import models

from enderecos.models import Endereco
from pessoas.models import Pessoa


# Create your models here.
class Diligencia (models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    data_realizacao = models.DateField (null=False, blank=False)
    mandado = models.FileField (upload_to='mandados/', null=True, blank=True)
    relatorio = models.FileField(upload_to='relatório/', null=True, blank=True)
    dinheiro_apreendido = models.DecimalField (max_digits=15, decimal_places=2)
    obs = models.TextField()
    # ForeignKey muitos para um, ondelete, se apagar um o outro tbm é apagado
    local = models.ForeignKey(Endereco, blank=False, null=False, on_delete=models.CASCADE)
        #ManyToManyField muitos para muitos
    pessoa = models.ManyToManyField (Pessoa, blank=True)

    class Meta:
        verbose_name = 'Diligência'
        verbose_name_plural = 'Diligências'

    def __str__(self):
        return self.nome


