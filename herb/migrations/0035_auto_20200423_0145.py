# Generated by Django 3.0.3 on 2020-04-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herb', '0034_auto_20200423_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('NA', 'Not_Arrived'), ('AR', 'Arrived')], max_length=2),
        ),
    ]
