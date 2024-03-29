# Generated by Django 4.1.3 on 2022-11-23 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billetera', '0003_gasto_categoria_id_ingreso_categoria_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='categoria_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billetera.categoria'),
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='categoria_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billetera.categoria'),
        ),
    ]
