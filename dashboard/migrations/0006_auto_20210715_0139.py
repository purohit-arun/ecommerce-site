# Generated by Django 3.2.4 on 2021-07-14 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20210710_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='desc',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='slider',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]