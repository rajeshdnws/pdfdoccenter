# Generated by Django 4.1.1 on 2022-09-25 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmspage',
            name='banner',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]