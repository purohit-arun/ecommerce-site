# Generated by Django 3.2.4 on 2021-08-01 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20210730_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='date_created',
        ),
        migrations.AddField(
            model_name='customer',
            name='Register_Date',
            field=models.DateTimeField(null=True),
        ),
    ]