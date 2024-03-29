# Generated by Django 4.1.3 on 2022-12-07 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ahorros', '0003_remove_inversion_ahorro_id_delete_ahorro_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ahorro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ahorro', models.CharField(max_length=40)),
                ('fecha_creacion', models.DateTimeField(verbose_name='date published')),
                ('cantidad_dinero', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Inversion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_inversion', models.CharField(max_length=60)),
                ('tipo_inversion', models.CharField(max_length=50)),
                ('ahorro_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ahorros.ahorro')),
            ],
        ),
    ]
