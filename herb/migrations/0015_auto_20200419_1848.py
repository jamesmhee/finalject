# Generated by Django 3.0.3 on 2020-04-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herb', '0014_auto_20200419_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('NA', 'Not_Arrived'), ('AR', 'Arrived')], max_length=2),
        ),
    ]