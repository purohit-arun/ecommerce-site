# Generated by Django 3.2 on 2021-04-18 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='img'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default='0'),
        ),
    ]
