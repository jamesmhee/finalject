# Generated by Django 3.0.3 on 2020-04-26 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herb', '0040_auto_20200426_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='end_promotion',
            field=models.CharField(choices=[('S', 'SALE'), ('NS', 'NOTSALE')], max_length=2),
        ),
    ]
