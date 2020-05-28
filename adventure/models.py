from __future__ import unicode_literals
from datetime import datetime
from pytz import timezone

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone as django_timezone


class Door(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name



class Chamber(models.Model):
    door = models.ForeignKey(Door, null=True, on_delete=models.CASCADE)
    heading = models.TextField(blank=True, null=True)
    count = models.CharField(max_length=1000, blank=True, null=True, default="0")
    initial_chamber = models.BooleanField(default=False, blank=True)
    result = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.heading


class Option(models.Model):
    text = models.TextField(null=True, blank=True)
    belonging_chamber = models.ForeignKey(Chamber, null=True, related_name='belonging_chamber', on_delete=models.CASCADE)
    count = models.CharField(max_length=1000, blank=True, null=True, default="0")
    next_chamber = models.ForeignKey(Chamber, null=True, on_delete=models.CASCADE)
    count = models.CharField(max_length=1000, blank=True, null=True, default="0")

    def __str__(self):
        text = str(self.text)
        count = str(self.count)

        return f'{text} ({count} hits)'



class PreviousOption(models.Model):
    previous_option = models.ForeignKey(Option, null=True, on_delete=models.CASCADE)
    previous_chamber = models.ForeignKey(Chamber, null=True, on_delete=models.CASCADE, related_name="previous_chamber")
    current_chamber = models.ForeignKey(Chamber, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.previous_option)


    def no_view_count(self):
        return str(self.previous_option).split('(')[0]
