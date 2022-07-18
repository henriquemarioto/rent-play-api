# Generated by Django 4.0.6 on 2022-07-15 17:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('game_api_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('image_url', models.URLField(max_length=255)),
                ('release_date', models.DateField()),
            ],
        ),
    ]
