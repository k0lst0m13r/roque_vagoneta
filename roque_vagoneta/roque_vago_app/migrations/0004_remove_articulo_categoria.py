# Generated by Django 3.2.14 on 2022-08-05 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roque_vago_app', '0003_articulo_precio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='categoria',
        ),
    ]
