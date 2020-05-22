from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone as django_timezone

from datetime import datetime
from pytz import timezone

class Painting(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    translation = models.CharField(max_length=100, null=True, blank=True)
    painting = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return str(self.name)


class UserPainting(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    painting = models.ForeignKey(Painting, null=True, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)

    def __str__(self):
        user = str(self.user).title()
        painting = str(self.painting).upper()

        return f'{user} viewed {painting}'


class Attempt(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    guess = models.CharField(max_length=100, null=True, blank=True)
    timestamp = models.DateTimeField(default=django_timezone.now, db_index=True)

    def __str__(self):
        fmt = "%H:%M on %m-%d-%Y"
        timestamp = self.timestamp
        now_pacific = timestamp.astimezone(timezone('US/Pacific'))
        timestamp = now_pacific.strftime(fmt)

        user = str(self.user).title()
        guess = str(self.guess).upper()

        return f'{user} tried: {guess} at {timestamp}'

