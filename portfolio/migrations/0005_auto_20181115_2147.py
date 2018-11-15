# Generated by Django 2.0.2 on 2018-11-15 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20181115_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='more_information',
            field=models.URLField(blank=True, null=True, verbose_name='Más Información'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects', verbose_name='Imagen'),
        ),
    ]
