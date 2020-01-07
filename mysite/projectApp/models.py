from django.db import models

class Status(models.Model):
    def __str__(self):
        return self.nome

    codigo = models.CharField(max_length=50, blank=False, null=False)
    nome = models.CharField(max_length=50, blank=False, null=False)

class Maquina(models.Model):
    def __str__(self):
        return self.nome

    nome = models.CharField(max_length=50, blank=True, null=False)
    status_id = models.ForeignKey(Status,models.DO_NOTHING, blank=False, null=False)
