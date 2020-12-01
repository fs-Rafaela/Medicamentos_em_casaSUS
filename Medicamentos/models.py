from django.db import models

#Ira Cadastra todos os medicamentos disponiveis

class Medicamentos(models.Model):
    Codigo_Medicamento = models.CharField(max_length = 14)
    MG = models.FloatField()
    Medicamento = models.CharField(max_length = 20)
    Indicacao = models.CharField(max_length = 20)
    Descricao = models.CharField(max_length = 50)

    def __str__(self):
        return self.Codigo_Medicamento

