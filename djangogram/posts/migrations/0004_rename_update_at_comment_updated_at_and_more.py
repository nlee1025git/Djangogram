# Generated by Django 5.0.6 on 2024-06-02 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_alter_comment_posts_alter_post_image_likes"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="update_at",
            new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="post",
            old_name="update_at",
            new_name="updated_at",
        ),
    ]