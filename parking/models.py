from django.db import models

# Create your models here.
class Parking(models.Model):
    slotID = models.IntegerField(default=0)
    timeIn = models.DateTimeField()
    timeOut = models.DateTimeField(null=True)