from django.db import migrations, models


class Migration(migrations.Migration):


    initial = True

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name = 'Pacientes', 
            fields = [
                ('id', models.AutoField(auto_created= True,
                                        primary_key = True, serialize= False, verbose_name= 'ID')),
            ('Nome', models.CharField(max_length = 80)),
            ('Cpf', models.CharField(max_length = 14)),
            ('Data_Nascimento', models.DateField()),
            ('Sexo', models.CharField(max_length = 1, choices= 'Sexo_choices' )),
            ('Hospital', models.CharField(max_length = 100)),
            ('Doenca', models.CharField(max_length = 50)),
            ('Tel', models.CharField(max_length = 14)),
            

            ],
        ),
    ]
