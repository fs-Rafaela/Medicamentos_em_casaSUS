from django.db import models
from random import choices



# Classe para cadastrar os pacientes que receberam os medicamentos em sua residencia!

class Pacientes(models.Model):

    Sexo_choices = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    Nome = models.CharField(max_length = 80)
    Cpf = models.CharField(max_length = 14) 
    Data_Nascimento = models.DateField()
    Sexo = models.CharField(max_length = 1, choices=Sexo_choices)
    Hospital = models.CharField(max_length = 100)
    Doenca = models.CharField(max_length = 50)
    Tel = models.CharField(max_length = 14)
    

    def __str__(self):
        return self.Cpf

