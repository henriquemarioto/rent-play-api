# Generated by Django 4.0.6 on 2022-07-18 12:40

from django.db import migrations

from platforms.serializers import PlatformSerializer


def create_initial_platforms(apps, schema_editor):
    platforms = [
        {
            "name": "Steam",
            "image_url": "https://logodownload.org/wp-content/uploads/2018/01/steam-logo.png",
            "platform_api_id": 1,
            "icon": "FaSteam",
        },
        {
            "name": "PlayStation Store",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/PlayStation_Store.png/640px-PlayStation_Store.png",
            "platform_api_id": 3,
            "icon": "FaPlaystation",
        },
        {
            "name": "Xbox Store",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Xbox_one_logo.svg/1024px-Xbox_one_logo.svg.png",
            "platform_api_id": 2,
            "icon": "FaXbox",
        },
        {
            "name": "Nintendo Store",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e9/Nintendo_eShop_logo.png",
            "platform_api_id": 6,
            "icon": "SiNintendoswitch",
        },
        {
            "name": "Epic Games",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Epic_Games_logo.svg/1200px-Epic_Games_logo.svg.png",
            "platform_api_id": 11,
            "icon": "SiEpicgames",
        },
    ]

    for platform in platforms:
        print(platform)
        serializer = PlatformSerializer(data=platform)
        serializer.is_valid(raise_exception=True)
        serializer.save()



class Migration(migrations.Migration):
    dependencies = [
        ("platforms", "0002_platform_icon"),
    ]

    operations = [
        migrations.RunPython(create_initial_platforms)
    ]