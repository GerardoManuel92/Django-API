# Generated by Django 4.2.5 on 2023-09-21 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('idGenero', models.AutoField(db_column='idGenero', primary_key=True, serialize=False)),
                ('tipoGenero', models.TextField(db_column='tipoGenero')),
            ],
            options={
                'db_table': 'Generos',
            },
        ),
    ]
