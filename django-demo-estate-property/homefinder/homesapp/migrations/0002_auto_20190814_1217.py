# Generated by Django 2.2.4 on 2019-08-14 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='age',
            field=models.CharField(default='NA', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='direction',
            field=models.CharField(default='NA', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='floor',
            field=models.CharField(default='NA', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='image_url',
            field=models.CharField(default='NA', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='postadress',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='price',
            field=models.CharField(default='NA', max_length=200),
            preserve_default=False,
        ),
    ]
