# Generated by Django 3.0.3 on 2020-06-16 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0004_auto_20200615_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='productimages/'),
        ),
    ]
