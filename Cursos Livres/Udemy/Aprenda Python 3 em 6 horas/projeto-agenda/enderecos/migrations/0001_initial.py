# Generated by Django 3.1.3 on 2020-11-02 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('numero', models.IntegerField()),
                ('cep', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
    ]
