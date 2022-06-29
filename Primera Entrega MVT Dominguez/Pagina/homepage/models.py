from django.db import models

# Create your models here.

class Familiar(models.Model):
  name = models.CharField(max_length=250)
  rollno = models.CharField(max_length=250)

  def __str__(self):
      return self.name