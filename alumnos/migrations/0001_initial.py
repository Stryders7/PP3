# Generated by Django 4.1.6 on 2023-06-16 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artistas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_artista', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='img')),
            ],
        ),
        migrations.CreateModel(
            name='Obras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('historia', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=20)),
                ('precio', models.IntegerField(verbose_name='precio')),
                ('tecnica', models.CharField(max_length=100)),
            ],
        ),
    ]
