# Generated by Django 4.0.6 on 2022-07-15 17:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rents_history', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renthistory',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='renthistory',
            name='start_date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
