from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Article():
    source = models.TextField()
    title = models.TextField()
    author = models.TextField()
    description = models.TextField()
    url = models.URLField()
    urlToImage = models.URLField()
    publishedAt = models.TextField()
    content = models.TextField()


class FavoriteList(TimeStampedModel):
    user = models.ForeignKey(User, related_name='favorites')
    articles = models.ManyToManyField('Article', blank=True)
