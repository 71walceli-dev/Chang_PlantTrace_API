# Generated by Django 4.2.1 on 2024-01-07 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hacienda', '0039_lote_fechasiembra'),
    ]

    operations = [
        migrations.AddField(
            model_name='lote',
            name='Edad',
            field=models.IntegerField(null=True),
        ),
    ]
