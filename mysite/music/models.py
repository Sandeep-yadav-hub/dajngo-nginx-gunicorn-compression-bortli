# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class RecordLabel(models.Model):
    name = models.CharField(max_length=560)


class MusicRelease(models.Model):
    title = models.CharField(max_length=560)
    release_date = models.DateField(auto_now_add=True)

class Artist(models.Model):
    name = models.CharField(max_length=560)
    label = models.ForeignKey(
        RecordLabel,
        related_name="artists",
        on_delete=models.SET_NULL,
        null=True
    )
    music_releases = models.ManyToManyField(
        MusicRelease, 
        related_name="artists",
        null=True
    )