# Generated by Django 3.1.3 on 2020-11-02 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enderecos', '0001_initial'),
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diligencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('data_realizacao', models.DateField()),
                ('mandado', models.FileField(blank=True, null=True, upload_to='mandados/')),
                ('relatorio', models.FileField(blank=True, null=True, upload_to='relatorios/')),
                ('dinheiro_apreendido', models.DecimalField(decimal_places=2, max_digits=15)),
                ('obs', models.TextField()),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enderecos.endereco')),
                ('pessoa', models.ManyToManyField(blank=True, to='pessoas.Pessoa')),
            ],
        ),
    ]
