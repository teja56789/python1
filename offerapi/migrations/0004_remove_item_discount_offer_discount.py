# Generated by Django 4.0.5 on 2022-06-10 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerapi', '0003_remove_offer_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='discount',
        ),
        migrations.AddField(
            model_name='offer',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]
