from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone as django_timezone

from datetime import datetime
from pytz import timezone



class Browser(models.Model):
    name = models.CharField(max_length=1000, blank = True, null = True)

    def __str__(self):
        return self.name


class OperatingSystem(models.Model):
    name = models.CharField(max_length=1000, blank = True, null = True)

    def __str__(self):
        return self.name


class PageLoad(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    page = models.CharField(max_length=1000, null = True, blank = True)
    time_stamp = models.DateTimeField(blank = True, null = True)
    ip_address = models.CharField(max_length = 100, blank = True, null = True)
    browser = models.ForeignKey(Browser, blank = True, null = True, on_delete=models.CASCADE)
    operating_system = models.ForeignKey(OperatingSystem, blank = True, null = True, on_delete=models.CASCADE)

    def __str__(self):
        return self.page


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
    first_title = models.CharField(max_length=100, null=True, blank=True)
    first_title_timestamp = models.DateTimeField(blank=True, null=True, db_index=True, default=None)
    second_title = models.CharField(max_length=100, null=True, blank=True)
    second_title_timestamp = models.DateTimeField(blank=True, null=True, db_index=True, default=None)
    third_title = models.CharField(max_length=100, null=True, blank=True)
    third_title_timestamp = models.DateTimeField(blank=True, null=True, db_index=True, default=None)
    submission_timestamp = models.DateTimeField(default=django_timezone.now, db_index=True)

    def __str__(self):
        fmt = "%H:%M on %m-%d-%Y"
        timestamp = self.submission_timestamp
        now_pacific = timestamp.astimezone(timezone('US/Pacific'))
        timestamp = now_pacific.strftime(fmt)

        user = str(self.user).title()
        guess = str(self.guess).upper()
        if guess == 'VIVIDARIUM INTERVIGILIUM VIATOR':
            return f'SUCCESS: {user} got it at {timestamp}'
        else:
            return f'{user} tried: {guess} at {timestamp}'

