# Generated by Django 3.0 on 2019-12-17 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191214_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='diagonal',
            field=models.FloatField(verbose_name='Діагональ'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='matrix',
            field=models.CharField(max_length=20, verbose_name='Тип матриці'),
        ),
    ]
