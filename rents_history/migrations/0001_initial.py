# Generated by Django 4.0.6 on 2022-07-15 17:06

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rent_accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentHistory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rent_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent_accounts', to='rent_accounts.rentaccount')),
            ],
        ),
    ]
