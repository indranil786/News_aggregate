# Generated by Django 3.0.6 on 2020-05-18 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200518_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='description',
            field=models.TextField(default='NULL'),
        ),
    ]
