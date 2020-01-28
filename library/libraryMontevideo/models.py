# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=64)
    is_female = models.BooleanField()
    ocupation = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return (self.name +' '+ self.last_name)

class Book(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=264)
    pages = models.SmallIntegerField()
    author = models.ManyToManyField(Author)
    topic = models.CharField(max_length=264)

    def __str__(self):
        return self.name
