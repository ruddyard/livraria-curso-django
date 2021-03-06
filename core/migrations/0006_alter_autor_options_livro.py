# Generated by Django 4.0.5 on 2022-06-25 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_catagoria_options_alter_editor_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name_plural': 'Autor'},
        ),
        migrations.CreateModel(
            name='livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=32)),
                ('quantidade', models.IntegerField()),
                ('preco', models.BooleanField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='livro', to='core.catagoria')),
            ],
        ),
    ]
