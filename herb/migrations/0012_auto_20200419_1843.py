# Generated by Django 3.0.3 on 2020-04-19 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herb', '0011_auto_20200419_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ordered',
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('NA', 'Not_Arrived'), ('AR', 'Arrived')], max_length=2),
        ),
    ]
