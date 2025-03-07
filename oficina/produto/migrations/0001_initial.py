# Generated by Django 4.2.15 on 2025-02-13 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fornecedor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('outras_despesas', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('custo_final', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lucro', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_venda', models.DecimalField(decimal_places=2, max_digits=10)),
                ('qtd_minima', models.IntegerField()),
                ('qtd_maxima', models.IntegerField()),
                ('qtd_atual', models.IntegerField()),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fornecedor.fornecedor', verbose_name='Fornecedor')),
            ],
        ),
    ]
