# Generated by Django 3.0.3 on 2020-04-22 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('herb', '0030_auto_20200421_1629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='delevery_location',
            new_name='delivery_location',
        ),
    ]
