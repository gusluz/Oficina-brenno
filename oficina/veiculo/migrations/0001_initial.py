# Generated by Django 4.2.15 on 2025-02-13 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('cor', models.CharField(max_length=100)),
                ('ano', models.CharField(max_length=4)),
                ('placa', models.CharField(max_length=8)),
                ('foto_veiculo', models.ImageField(blank=True, upload_to='images/', verbose_name='Foto do veiculo')),
                ('cliente_nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente', verbose_name='Nome do Cliente')),
            ],
            options={
                'verbose_name': 'Veiculo',
                'verbose_name_plural': 'Veiculos',
            },
        ),
    ]
