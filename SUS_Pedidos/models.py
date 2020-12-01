from django.db import models


# Cadastro dos pedidos dos medicamentos dos pacientes
class SUS_Pedidos(models.Model):
    NumSUS = models.CharField(max_length = 18)
    Inicio_Tratamento = models.DateField()
    Medicamento = models.CharField(max_length = 50)
    MG = models.FloatField()
    Qtd_De_Caixa = models.IntegerField()
    Data_De_Envio = models.DateField()
    Endereco = models.CharField(max_length = 50)
    N = models.IntegerField()
    Complemento = models.CharField(max_length = 20)
    Bairro = models.CharField(max_length = 30)
    Cidade = models.CharField(max_length = 20)
    CEP = models.CharField(max_length = 9)
    Discricao = models.CharField(max_length = 100)

    def __str__ (self):
        return self.NumSUS


