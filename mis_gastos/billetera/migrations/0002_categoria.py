# Generated by Django 4.1.3 on 2022-11-21 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billetera', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=40)),
                ('billetera_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billetera.billetera')),
            ],
        ),
    ]
