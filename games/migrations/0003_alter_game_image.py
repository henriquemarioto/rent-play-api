# Generated by Django 4.0.6 on 2022-07-13 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_alter_game_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.URLField(max_length=255),
        ),
    ]
