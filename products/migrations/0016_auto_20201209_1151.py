# Generated by Django 3.1.3 on 2020-12-09 10:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20201208_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 9, 10, 51, 8, 788319, tzinfo=utc)),
        ),
    ]
