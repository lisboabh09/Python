# Generated by Django 4.1.2 on 2022-10-24 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femini')], default='M', max_length=1),
        ),
    ]
