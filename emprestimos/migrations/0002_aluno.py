# Generated by Django 4.2.16 on 2024-11-25 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('turma', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=200)),
            ],
        ),
    ]
