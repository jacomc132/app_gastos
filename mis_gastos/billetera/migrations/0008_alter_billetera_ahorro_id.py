# Generated by Django 4.1.3 on 2022-12-07 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ahorros', '0001_initial'),
        ('billetera', '0007_billetera_ahorro_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billetera',
            name='ahorro_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ahorros.ahorro'),
        ),
    ]
