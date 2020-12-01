from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name = 'Medicamentos', 
            fields = [
                ('id', models.AutoField(auto_created= True,
                                        primary_key = True, serialize= False, verbose_name= 'ID')),
            ('Codigo_Medicamento', models.CharField(max_length = 14)),
            ('MG' , models.FloatField()),
            ('Medicamento', models.CharField(max_length = 20)),
            ('Indicacao', models.CharField(max_length = 20)),
            ('Descricao', models.CharField(max_length = 50)),

            ],
        ),
    ]
