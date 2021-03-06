# Generated by Django 3.0.3 on 2020-04-21 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herb', '0029_auto_20200421_1625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order_item',
            old_name='items',
            new_name='item',
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('AR', 'Arrived'), ('NA', 'Not_Arrived')], max_length=2),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='end_promotion',
            field=models.CharField(choices=[('NS', 'NOTSALE'), ('S', 'SALE')], max_length=2),
        ),
    ]
