from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name = 'SUS_Pedidos', 
            fields = [
                ('id', models.AutoField(auto_created= True,
                                        primary_key = True, serialize= False, verbose_name= 'ID')),
            ('NumSUS', models.CharField(max_length = 18)),
            ('Inicio_Tratamento', models.DateField()),
            ('Medicamento', models.CharField(max_length = 50)),
            ('MG' , models.FloatField()),
            ('Qtd_De_Caixa', models.IntegerField()),
            ('Data_De_Envio', models.DateField()),
            ('Endereco', models.CharField(max_length = 50)),
            ('N' , models.IntegerField()),
            ('Complemento' , models.CharField(max_length = 20)),
            ('Bairro', models.CharField(max_length = 30)),
            ('Cidade', models.CharField(max_length = 20)),
            ('CEP', models.CharField(max_length = 9)),
            ('Discricao', models.CharField(max_length = 100)),

            ],
        ),
    ]

