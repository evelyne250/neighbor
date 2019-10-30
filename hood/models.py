from django.db import models

class NeighbourHood(models.Model):
    name = models.CharField(max_length =30)
    location = models.CharField(max_length =30)
    occupants = models.IntegerField()

    def __str__(self):
        return self.name
        