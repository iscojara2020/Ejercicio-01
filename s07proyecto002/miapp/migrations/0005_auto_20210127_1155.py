# Generated by Django 3.1.4 on 2021-01-27 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0004_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autor',
            old_name='Fecha_Nacimiento',
            new_name='fecha_nacimiento',
        ),
        migrations.RenameField(
            model_name='autor',
            old_name='Pais',
            new_name='pais',
        ),
    ]
