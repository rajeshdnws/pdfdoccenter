# Generated by Django 4.1.1 on 2022-09-25 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_cmspage_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cmspage',
            name='banner_text',
        ),
        migrations.AlterField(
            model_name='cmspage',
            name='image_name',
            field=models.CharField(blank=True, max_length=140, verbose_name='Banner alt'),
        ),
    ]
