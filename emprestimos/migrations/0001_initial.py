# Generated by Django 5.1.3 on 2024-11-24 17:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno', models.TextField(max_length=200)),
                ('criadoEm', models.DateTimeField(auto_now_add=True)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livros.livro')),
            ],
        ),
    ]
