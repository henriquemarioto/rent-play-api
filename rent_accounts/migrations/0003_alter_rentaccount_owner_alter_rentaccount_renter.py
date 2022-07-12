# Generated by Django 4.0.6 on 2022-07-12 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rent_accounts', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentaccount',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rentaccount',
            name='renter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='renter', to=settings.AUTH_USER_MODEL),
        ),
    ]
