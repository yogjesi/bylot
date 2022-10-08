from operator import mod
from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=10)
    table = models.IntegerField(null=True)

    def __str__(self):
        return self.name