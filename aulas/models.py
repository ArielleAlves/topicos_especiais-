from django.db import models

# Importar o modelo User
from django.contrib.auth.models import User

# Create your models here.




class Tipo(models.Model):
    descricao = models.CharField(
        max_length=50, verbose_name="Descrição", help_text="Ex: Teclado, Violao, Violino, Piano")

    def __str__(self):
        return "{}".format(self.descricao)


class Estilo(models.Model):
    descricao = models.CharField(
        max_length=50, verbose_name="Descrição", help_text="Ex: Sertanejo, Clássica, Internacional, MPB")

    def __str__(self):
        return "{}".format(self.descricao)

    # Configurar algumas coisas dessa classe, como nome, plural, ordenação, etc
    # https://docs.djangoproject.com/en/2.2/ref/models/options/
    class Meta:
        verbose_name = "Estilo"


class Musica(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    estilo = models.ForeignKey(
    Estilo, on_delete=models.PROTECT, verbose_name="Estilo")
    nome = models.CharField(max_length=50, null=True, blank=True, help_text="Nome da Música?")
    autor = models.CharField(max_length=50, null=True, blank=True, help_text="Nome do autor?")
    ano = models.CharField(max_length=5)

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}/{}".format(self.estilo, self.tipo)
