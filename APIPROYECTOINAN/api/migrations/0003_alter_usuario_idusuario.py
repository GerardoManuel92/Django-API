# Generated by Django 4.2.5 on 2023-10-19 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_usuario_usuario_has_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='idUsuario',
            field=models.AutoField(db_column='idUsuario', primary_key=True, serialize=False),
        ),
    ]
