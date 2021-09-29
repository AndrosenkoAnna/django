from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    test = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    slug = models.SlugField()
    text = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )


class Tag(models.Model):
    title = models.CharField(max_length=100)
    posts = models.ManyToManyField(Post, related_name='tags')

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
