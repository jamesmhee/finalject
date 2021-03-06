# Generated by Django 3.0.3 on 2020-04-19 12:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('herb', '0020_remove_order_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='promotion',
            name='end_promotion',
            field=models.CharField(choices=[('S', 'SALE'), ('NS', 'NOTSALE')], max_length=2),
        ),
    ]
