# Generated by Django 4.1.3 on 2022-12-07 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billetera', '0008_alter_billetera_ahorro_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billetera',
            name='ahorro_id',
        ),
    ]
