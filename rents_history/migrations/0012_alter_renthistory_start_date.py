# Generated by Django 4.0.6 on 2022-07-19 22:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rents_history', '0011_alter_renthistory_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renthistory',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 19, 19, 42, 35, 569619)),
        ),
    ]
