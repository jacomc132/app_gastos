# Generated by Django 4.1.3 on 2022-12-07 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ahorros', '0001_initial'),
        ('billetera', '0006_rename_descripcion_gasto_gasto_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='billetera',
            name='ahorro_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ahorros.ahorro'),
        ),
    ]
