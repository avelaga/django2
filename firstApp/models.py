from django.db import models

class Person(models.Model):
  name = models.CharField(max_length=50)
  career = models.CharField(max_length=50)
  numBitches = models.IntegerField()

  def __str__(self):
    return self.name + ": " + str(self.numBitches)

