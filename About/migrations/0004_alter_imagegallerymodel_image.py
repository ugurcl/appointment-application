# Generated by Django 5.1.3 on 2024-11-24 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0003_imagegallerymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagegallerymodel',
            name='image',
            field=models.ImageField(upload_to='upload/gallery/%Y/%m/%d', verbose_name='Resim'),
        ),
    ]
