# Generated by Django 4.1.7 on 2023-04-03 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cliente_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeuModelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='Data',
        ),
    ]
