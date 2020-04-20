# Generated by Django 3.0.3 on 2020-04-20 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herb', '0025_auto_20200420_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('AR', 'Arrived'), ('NA', 'Not_Arrived')], max_length=2),
        ),
    ]
