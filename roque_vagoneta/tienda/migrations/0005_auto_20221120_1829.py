# Generated by Django 3.2.14 on 2022-11-20 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_auto_20221117_1655'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articulo',
            options={'verbose_name': 'Articulo', 'verbose_name_plural': 'Articulos'},
        ),
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
    ]