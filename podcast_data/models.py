from django.db import models

import datetime

from django.db import models
from django.utils import timezone


class Avalanche_Accident(models.Model):
    Avalanche_Number = models.IntegerField()
    Name = models.CharField(max_length=500)
    Lat = models.DecimalField(max_digits=8, decimal_places=5)
    Long = models.DecimalField(max_digits=8, decimal_places=5)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.Name
