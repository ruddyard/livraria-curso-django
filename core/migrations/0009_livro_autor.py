# Generated by Django 4.0.5 on 2022-06-25 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_livro_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='autor',
            field=models.ManyToManyField(related_name='livros', to='core.autor'),
        ),
    ]
