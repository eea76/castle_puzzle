from __future__ import unicode_literals

from django.db import models


class Painting(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    translation = models.CharField(max_length=100, null=True, blank=True)
    viewed = models.BooleanField(default=False)
    painting = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return str(self.name)


