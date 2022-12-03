# Generated by Django 3.2.14 on 2022-12-03 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tienda', '0005_auto_20221120_1829'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'db_table': 'pedidos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DetalleArticulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('articulo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.articulo')),
                ('pedido_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.pedido')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Detalle Articulos',
                'db_table': 'detallearticulos',
                'ordering': ['id'],
            },
        ),
    ]
