# Generated by Django 4.0.5 on 2022-06-26 01:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0010_compra'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='status',
            field=models.IntegerField(choices=[(1, 'Carrinho'), (2, 'Realizado'), (3, 'Pago'), (4, 'Entregue')], default=1),
        ),
        migrations.AddField(
            model_name='compra',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='compras', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]