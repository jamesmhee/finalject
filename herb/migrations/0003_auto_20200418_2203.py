# Generated by Django 3.0.3 on 2020-04-18 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herb', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='quanlity',
            field=models.IntegerField(default=1),
        ),
    ]
