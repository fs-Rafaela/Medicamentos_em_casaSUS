from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name = 'Entrega_Medicamentos', 
            fields = [
                ('id', models.AutoField(auto_created= True,
                                        primary_key = True, serialize= False, verbose_name= 'ID')),
            ('NumSUS_Paciente' , models.CharField(max_length = 18)), 
            ('Matricula_Entregador', models.IntegerField()),
            ('Data_Da_Entrega', models.DateField()),
            ('Hora_Da_Entrega', models.TimeField()),
            
            ],
        ),    
        
    ]
