# Generated by Django 5.0.6 on 2024-05-30 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_bio_user_first_name_user_followers_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="profile_photoe",
            new_name="profile_photo",
        ),
    ]
