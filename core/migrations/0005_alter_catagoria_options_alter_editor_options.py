# Generated by Django 4.0.5 on 2022-06-25 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_catagoria_options_alter_editor_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catagoria',
            options={'verbose_name_plural': 'Categoria'},
        ),
        migrations.AlterModelOptions(
            name='editor',
            options={'verbose_name_plural': 'Editor'},
        ),
    ]
