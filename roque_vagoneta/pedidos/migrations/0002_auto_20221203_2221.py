# Generated by Django 3.2.14 on 2022-12-03 22:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tienda', '0005_auto_20221120_1829'),
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DetalleArticulos',
            new_name='DetallePedido',
        ),
        migrations.AlterModelOptions(
            name='detallepedido',
            options={'ordering': ['id'], 'verbose_name': 'Detalle Pedido', 'verbose_name_plural': 'Detalle Pedido'},
        ),
        migrations.AlterModelTable(
            name='detallepedido',
            table='detallepedido',
        ),
    ]
