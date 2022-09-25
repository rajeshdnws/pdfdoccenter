# Generated by Django 4.1.1 on 2022-09-25 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cmspage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Name')),
                ('image_name', models.CharField(blank=True, max_length=140, verbose_name='Banner Image')),
                ('banner_text', models.CharField(blank=True, max_length=200, verbose_name='Banner Desc')),
                ('slug', models.SlugField(allow_unicode=True, max_length=100)),
                ('meta_title', models.CharField(blank=True, max_length=200, verbose_name='Meta Title')),
                ('meta_desc', models.CharField(blank=True, max_length=200, verbose_name='Meta Description')),
                ('meta_keyword', models.CharField(blank=True, max_length=200, verbose_name='Meta Keyword')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]