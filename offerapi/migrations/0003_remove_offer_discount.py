# Generated by Django 4.0.5 on 2022-06-10 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offerapi', '0002_rename_course_offer_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='discount',
        ),
    ]
