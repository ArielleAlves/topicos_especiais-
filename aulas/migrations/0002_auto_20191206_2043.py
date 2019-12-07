# Generated by Django 2.2.1 on 2019-12-06 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musica',
            name='descricao',
        ),
        migrations.AlterField(
            model_name='tipo',
            name='descricao',
            field=models.CharField(help_text='Ex: Teclado, Violao, Violino, Piano', max_length=50, verbose_name='Descrição'),
        ),
        migrations.DeleteModel(
            name='Cidade',
        ),
        migrations.DeleteModel(
            name='Estado',
        ),
    ]