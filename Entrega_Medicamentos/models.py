from django.db import models

class Entrega_Medicamentos(models.Model):
    NumSUS_Paciente = models.CharField(max_length = 18) 
    Matricula_Entregador = models.IntegerField()
    Data_Da_Entrega = models.DateField()
    Hora_Da_Entrega = models.TimeField()

    def __str__(self):
        return self.NumSUS_Paciente

