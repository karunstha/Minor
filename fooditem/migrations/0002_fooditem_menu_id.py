# Generated by Django 3.0.8 on 2020-08-31 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20200831_1812'),
        ('fooditem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='menu_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.Menu'),
        ),
    ]
