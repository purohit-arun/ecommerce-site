# Generated by Django 3.2.4 on 2021-07-30 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20210728_1408'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]