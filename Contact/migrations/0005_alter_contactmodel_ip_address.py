# Generated by Django 5.1.3 on 2024-11-25 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0004_contactmodel_ip_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, default='', null=True, verbose_name='Kullanıcı Ip Adresi'),
        ),
    ]
