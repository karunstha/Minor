# Generated by Django 3.0.8 on 2020-08-30 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooditem', '0001_initial'),
        ('orders', '0003_order_table_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='fooditem',
            field=models.ManyToManyField(to='fooditem.FoodItem', verbose_name='FOOD'),
        ),
    ]
