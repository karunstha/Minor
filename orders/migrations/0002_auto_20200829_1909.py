# Generated by Django 3.0.8 on 2020-08-29 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooditem', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='food_id',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='fooditem',
            field=models.ManyToManyField(to='fooditem.FoodItem'),
        ),
    ]
