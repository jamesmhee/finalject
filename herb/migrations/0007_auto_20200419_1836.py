# Generated by Django 3.0.3 on 2020-04-19 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herb', '0006_order_item_buy_by_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
        migrations.RemoveField(
            model_name='order_item',
            name='buy_by_user',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='herb.Order_Item'),
        ),
        migrations.AddField(
            model_name='order',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='promotion',
            name='end_promotion',
            field=models.CharField(choices=[('S', 'SALE'), ('NS', 'NOTSALE')], max_length=2),
        ),
    ]
