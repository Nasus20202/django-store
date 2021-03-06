# Generated by Django 3.1.3 on 2020-12-08 20:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20201202_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=64)),
                ('surname', models.CharField(default='', max_length=64)),
                ('email', models.CharField(default='', max_length=128)),
                ('address', models.CharField(default='', max_length=64)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 12, 8, 20, 58, 25, 168993, tzinfo=utc))),
                ('cost', models.IntegerField(default=0)),
                ('products', models.TextField(default='')),
            ],
        ),
    ]
