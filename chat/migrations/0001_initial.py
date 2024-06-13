# Generated by Django 5.0.6 on 2024-05-30 00:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carreras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ap_pat', models.CharField(max_length=100)),
                ('ap_mat', models.CharField(max_length=100)),
                ('usu', models.CharField(max_length=50)),
                ('passw', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
                ('status', models.BooleanField(default=True)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.carreras')),
            ],
        ),
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt_mensaje', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.persona')),
            ],
        ),
    ]
