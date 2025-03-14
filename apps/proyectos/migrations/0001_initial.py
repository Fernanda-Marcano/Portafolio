# Generated by Django 5.1.6 on 2025-03-05 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Nombre del Proyecto')),
                ('description', models.TextField(verbose_name='Descripción del Proyecto')),
                ('tecnology', models.CharField(max_length=200, verbose_name='Tecnología')),
                ('url', models.URLField(verbose_name='Url del Proyecto')),
                ('image', models.ImageField(default='img/default_img.png', upload_to='img/', verbose_name='Imagen del Proyecto')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'db_table': 'Proyectos',
                'ordering': ['id', 'created'],
            },
        ),
    ]
