"""locations models"""

# Django
from django.db import models


class Location(models.Model):
    """Location Model"""
    name = models.CharField(max_length=25)
    coordinates = models.CharField(max_length=30)

    def __str__(self):
        """:return location's name"""
        return '{}'.format(self.name)