# Generated by Django 4.1.3 on 2022-12-07 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billetera', '0009_remove_billetera_ahorro_id'),
        ('ahorros', '0002_alter_ahorro_cantidad_dinero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inversion',
            name='ahorro_id',
        ),
        migrations.DeleteModel(
            name='Ahorro',
        ),
        migrations.DeleteModel(
            name='Inversion',
        ),
    ]
