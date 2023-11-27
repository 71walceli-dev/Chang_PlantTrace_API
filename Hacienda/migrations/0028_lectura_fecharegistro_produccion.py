# Generated by Django 4.2.1 on 2023-11-26 23:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Hacienda', '0027_lectura_total_planta_circunferencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='lectura',
            name='FechaRegistro',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qq', models.DecimalField(decimal_places=4, max_digits=8)),
                ('Fecha', models.DateField()),
                ('FechaRegistro', models.DateField(auto_now_add=True)),
                ('Activo', models.BooleanField(default=True)),
                ('Usuario', models.TextField(default='Admin', max_length=100, null=True)),
                ('Id_Lote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hacienda.lote')),
            ],
        ),
    ]
