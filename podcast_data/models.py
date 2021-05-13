from django.db import models

import datetime

from django.db import models
from django.utils import timezone


class Avalanche_Accident(models.Model):
    Avalanche_Number = models.IntegerField()
    Name = models.CharField(max_length=1000, default='INPUT NAME')
    Date = models.CharField(max_length=100, default='INPUT DATE')
    State = models.CharField(max_length=100, default='INPUT STATE')
    Lat = models.DecimalField(max_digits=50, decimal_places=10, default=9999)
    Long = models.DecimalField(max_digits=50, decimal_places=10, default=9999)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.Name

