# Generated by Django 4.0.6 on 2022-07-14 15:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rents_history', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='renthistory',
            name='user',
            field=models.ManyToManyField(related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
