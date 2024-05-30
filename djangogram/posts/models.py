from email.mime import image
from operator import mod
from django.db import models
from djangogram.users import models as user_model

# Create your models here.
class TimeStamedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Post(TimeStamedModel):
    author = models.ForeignKey(
                user_model.User,
                null=True,
                on_delete=models.CASCADE,
                related_name="post_author"
            )
    image = models.ImageField(blank=False)
    caption = models.TextField(blank=False)
    image_likes = models.ManyToManyField(user_model.User, related_name="post_image_likes")

class Comment(TimeStamedModel):
    author = models.ForeignKey(
                user_model.User,
                null=True,
                on_delete=models.CASCADE,
                related_name="comment_author"
            )
    posts = models.ForeignKey(
                Post,
                null=True,
                on_delete=models.CASCADE,
                related_name="comment_author"
            )
    contents = models.TextField(blank=True)
