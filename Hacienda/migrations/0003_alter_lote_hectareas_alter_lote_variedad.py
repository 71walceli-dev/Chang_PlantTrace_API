# Generated by Django 4.2.1 on 2023-05-22 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hacienda', '0002_estacion_rename_codigo_hacienda_lote_codigo_lote_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lote',
            name='Hectareas',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='lote',
            name='Variedad',
            field=models.CharField(max_length=20, null=True),
        ),
    ]