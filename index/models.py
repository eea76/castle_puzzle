from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


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
        return str(self.user).title() + ' viewed ' + str(self.painting).upper()


class Attempt(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    guess = models.CharField(max_length=100, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        return str(self.user).title() + ' tried: ' + str(self.guess).upper()

